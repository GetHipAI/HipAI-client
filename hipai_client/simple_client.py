from __future__ import absolute_import

from typing import Any, Dict, List, Literal, Optional, TypeAlias, Union
from uuid import UUID
from hipai_client.models import (
    ConnectionConfigObject,
    DataContextObject,
    AgentConfigObject,
    ModelConfigObject,
    ChatCompletionRequest,
    GroupIsolationObject,
    UserPublic,
)
from requests_toolbelt.multipart.encoder import MultipartEncoder
from enum import Enum
from multiprocessing.pool import ApplyResult

import hipai_client
import json
import requests
import secrets

DEFAULT_PRODUCTION_API_HOST = "https://api.gethip.ai"


class DataContextStatuses(Enum):
    """
    Status values for :class:`~hipai_client.models.DataContextObject` lifecycle.

    This enum is used for convenience when constructing or inspecting data contexts.

    Examples
    --------
    >>> from hipai_client.models import DataContextObject
    >>> dc = DataContextObject(status=DataContextStatuses.READY.value)
    >>> DataContextStatuses.READY.is_ready(dc)
    True
    >>> dc.status = DataContextStatuses.DRAFT.value
    >>> DataContextStatuses.READY.is_ready(dc)
    False
    """

    QUEUED = "queued"
    DRAFT = "draft"
    READY = "ready"
    PREPARING = "preparing"
    REBUILDING = "rebuilding"

    def is_ready(self, data_context: DataContextObject):
        """
        Return ``True`` if the provided data context is in the ``READY`` state.

        Parameters
        ----------
        data_context : hipai_client.models.DataContextObject
            The data context to check.

        Returns
        -------
        bool
            ``True`` when ``data_context.status`` equals ``DataContextStatuses.READY.value``.

        Examples
        --------
        >>> from hipai_client.models import DataContextObject
        >>> dc = DataContextObject(status="ready")
        >>> DataContextStatuses.READY.is_ready(dc)
        True
        """
        return data_context.status == self.READY


class ConnectionConfigurationSchemas(Enum):
    """
    String schema identifiers supported by :class:`~hipai_client.models.ConnectionConfigObject`.

    This enum mirrors the allowed literal values in :data:`ConnectionSchema`.

    Examples
    --------
    >>> ConnectionConfigurationSchemas.MYSQL.value
    'mysql'
    >>> ConnectionConfigurationSchemas.DOCUMENT.value
    'documents'
    """

    DOCUMENT = "documents"
    MYSQL = "mysql"
    POSTGRESQL = "postgresql"
    SNOWFLAKE = "snowflake"
    SQLITE = "sqlite"


ConnectionSchema: TypeAlias = Literal["documents", "mysql", "postgresql", "snowflake", "sqlite"]
"""
Allowed values for ``conn_schema`` passed to :func:`instantiate_connection_config`
and :meth:`SimpleHipAIClient.upsert_connection_config`.

Examples
--------
>>> schema = "postgresql"
>>> schema in ("documents", "mysql", "postgresql", "snowflake", "sqlite")
True
"""


class AgentStatuses(Enum):
    """
    Status values for :class:`~hipai_client.models.AgentConfigObject`.

    Examples
    --------
    >>> AgentStatuses.ACTIVE.value
    'active'
    >>> AgentStatuses.INACTIVE.value
    'inactive'
    """

    ACTIVE = "active"
    INACTIVE = "inactive"


AgentStatus: TypeAlias = Literal["active", "inactive"]
"""
Allowed values for agent status.

Examples
--------
>>> status = "active"
>>> status in ("active", "inactive")
True
"""


def instantiate_connection_config(
    conn_schema: ConnectionSchema,
    name: str,
    hostname_path: str = "",
    graph_id: Optional[Union[str, UUID]] = None,
    group_id: Optional[Union[str, UUID]] = None,
    username: Optional[str] = None,
    password: Optional[str] = None,
    port: Optional[int] = None,
    database: Optional[str] = None,
    parameters: Optional[str] = None,
    account: Optional[str] = None,
    warehouse: Optional[str] = None,
    role: Optional[str] = None,
    sf_schema: Optional[str] = None,
    **kwargs,
) -> ConnectionConfigObject:
    """
    Construct a :class:`hipai_client.models.ConnectionConfigObject` from convenience parameters.

    This helper centralizes validation and object construction for different connection schemas.

    Parameters
    ----------
    conn_schema : ConnectionSchema
        The connection type. Must be one of ``"documents"``, ``"mysql"``, ``"postgresql"``,
        ``"snowflake"``, or ``"sqlite"``.
    name : str
        Human-friendly name for the connection configuration.
    hostname_path : str, optional
        For database connections this is typically the hostname (and sometimes path).
        For ``"sqlite"`` it should be the path to the database file.
        For ``"documents"`` this may be unused/empty depending on the server.
    graph_id : str or uuid.UUID, optional
        Optional graph/data-context identifier to associate with the connection configuration.
    group_id : str or uuid.UUID, optional
        Optional group isolation identifier to associate with the configuration.
    username : str, optional
        Database username (required for ``"mysql"``, ``"postgresql"``, and ``"snowflake"``).
    password : str, optional
        Database password (required for ``"mysql"``, ``"postgresql"``, and ``"snowflake"``).
    port : int, optional
        Database port (optional for ``"mysql"``/``"postgresql"``).
    database : str, optional
        Database name (required for ``"mysql"`` and ``"postgresql"``).
    parameters : str, optional
        Optional connection string parameters (driver-specific).
    account : str, optional
        Snowflake account identifier (required for ``"snowflake"``).
    warehouse : str, optional
        Snowflake warehouse (required for ``"snowflake"``).
    role : str, optional
        Snowflake role (required for ``"snowflake"``).
    sf_schema : str, optional
        Snowflake schema name (required for ``"snowflake"``).
    **kwargs
        Any additional fields supported by :class:`hipai_client.models.ConnectionConfigObject`.

    Returns
    -------
    hipai_client.models.ConnectionConfigObject
        A validated connection config instance.

    Raises
    ------
    ValueError
        If required fields for the selected schema are missing.

    Examples
    --------
    Create a documents connection:

    >>> cfg = instantiate_connection_config(
    ...     conn_schema="documents",
    ...     name="Docs Uploads",
    ...     group_id="00000000-0000-0000-0000-000000000000",
    ... )
    >>> cfg.conn_schema
    'documents'

    Create a PostgreSQL connection:

    >>> cfg = instantiate_connection_config(
    ...     conn_schema="postgresql",
    ...     name="Warehouse",
    ...     hostname_path="db.example.com",
    ...     username="analytics",
    ...     password="secret",
    ...     database="prod",
    ...     port=5432,
    ... )
    >>> cfg.conn_schema
    'postgresql'
    """
    if isinstance(group_id, UUID):
        group_id = str(group_id)
    if isinstance(graph_id, UUID):
        graph_id = str(graph_id)
    if conn_schema == ConnectionConfigurationSchemas.DOCUMENT.value:
        return ConnectionConfigObject(
            conn_schema=conn_schema,
            name=name,
            hostname_path=hostname_path,
            group_id=group_id,
            graph_id=graph_id,
            **kwargs,
        )
    elif conn_schema in [
        ConnectionConfigurationSchemas.MYSQL.value,
        ConnectionConfigurationSchemas.POSTGRESQL.value,
    ]:
        if None in [hostname_path, username, password, database] or len(hostname_path) == 0:
            raise ValueError(
                f"Connection Configurations with schema '{conn_schema}' require "
                "hostname_path, username, password, and database fields."
            )
        return ConnectionConfigObject(
            conn_schema=conn_schema,
            name=name,
            hostname_path=hostname_path,
            group_id=group_id,
            graph_id=graph_id,
            username=username,
            password=password,
            port=port,
            database=database,
            parameters=parameters,
            **kwargs,
        )
    elif conn_schema == ConnectionConfigurationSchemas.SQLITE.value:
        if hostname_path is None or len(hostname_path) == 0:
            raise ValueError(
                f"Connection Configurations with schema '{conn_schema}' requires the hostname_path field."
            )
        return ConnectionConfigObject(
            conn_schema=conn_schema,
            name=name,
            hostname_path=hostname_path,
            group_id=group_id,
            graph_id=graph_id,
            **kwargs,
        )
    elif conn_schema == ConnectionConfigurationSchemas.SNOWFLAKE.value:
        if None in [role, sf_schema, warehouse, account, username, password]:
            raise ValueError(
                f"Connection Configurations with schema '{conn_schema}' require role, sf_schema, "
                "warehouse, account, username, and password fields."
            )
        return ConnectionConfigObject(
            conn_schema=conn_schema,
            name=name,
            hostname_path=hostname_path,
            group_id=group_id,
            graph_id=graph_id,
            role=role,
            sf_schema=sf_schema,
            warehouse=warehouse,
            account=account,
            username=username,
            password=password,
            **kwargs,
        )
    else:
        raise ValueError(f"conn_schema, '{conn_schema}', is not a support connection schema.")


class SimpleHipAIClient:
    """
    Lightweight wrapper around the autogenerated ``hipai_client`` OpenAPI client.

    This class focuses on a few common CRUD/upsert workflows and provides a higher-level`chat` helper.

    Parameters
    ----------
    access_token : str
        Bearer token used to authenticate requests.
    hostname : str, optional
        Base API host. Defaults to :data:`DEFAULT_PRODUCTION_API_HOST`.

    Attributes
    ----------
    conf : hipai_client.Configuration
        OpenAPI client configuration (host, access token, etc.).
    client : hipai_client.ApiClient
        Underlying OpenAPI API client instance.

    Examples
    --------
    >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
    >>> # Create a group
    >>> group = client.create_group(name="My Group")
    """

    def __init__(self, access_token: str, hostname: str = DEFAULT_PRODUCTION_API_HOST):
        """
        Initialize the client wrapper.

        Parameters
        ----------
        access_token : str
            Bearer token used to authenticate requests.
        hostname : str, optional
            Base API host URL.
        """
        self.conf = hipai_client.Configuration()
        self.conf.access_token = access_token
        self.conf.host = hostname
        self.client = hipai_client.ApiClient(self.conf)

    def create_group(
        self,
        group: Optional[GroupIsolationObject] = None,
        name: Optional[str] = None,
        async_req: bool = False,
        **kwargs,
    ) -> Union[GroupIsolationObject, ApplyResult]:
        """
        Create (or upsert) a group isolation object.

        You can either provide an already-constructed :class:`~hipai_client.models.GroupIsolationObject`
        or provide a ``name`` (and optional extra fields) and the object will be created for you.

        Parameters
        ----------
        group : hipai_client.models.GroupIsolationObject, optional
            A pre-constructed group object to upsert.
        name : str, optional
            Name used to construct a group object when ``group`` is not provided.
        async_req : bool, optional
            When ``True``, returns a :class:`multiprocessing.pool.ApplyResult` for async execution.
        **kwargs
            Additional fields passed to :class:`~hipai_client.models.GroupIsolationObject`
            when constructing one.

        Returns
        -------
        hipai_client.models.GroupIsolationObject or multiprocessing.pool.ApplyResult
            The created/upserted group or an async result handle.

        Examples
        --------
        Create using a name:

        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> group = client.create_group(name="Analytics Team")
        >>> group.name
        'Analytics Team'

        Create using an explicit object:

        >>> group_obj = GroupIsolationObject(name="Research Team")
        >>> group = client.create_group(group=group_obj)
        """
        assert group is not None or name is not None, "#create_group requires either a GroupIsolationObject or a name passed."
        group = group or GroupIsolationObject(name=name, **kwargs)
        return hipai_client.GroupsApi(self.client).upsert_group_api_groups_post(group, async_req=async_req)

    def upsert_llm_config(
        self,
        config: Optional[ModelConfigObject] = None,
        name: Optional[str] = None,
        token: Optional[str] = None,
        model_name: Optional[str] = "gpt-5.2",
        async_req: bool = False,
        **kwargs,
    ) -> Union[ModelConfigObject, ApplyResult]:
        """
        Create or update an LLM model configuration.

        Provide either a full :class:`~hipai_client.models.ModelConfigObject` or enough fields
        to construct one (``name``, ``token``, and ``model_name``).

        Parameters
        ----------
        config : hipai_client.models.ModelConfigObject, optional
            Pre-built model config object. If provided, takes precedence.
        name : str, optional
            Used to construct the config when ``config`` is not provided.
        token : str, optional
            Provider/API token used by the backend for the model configuration.
        model_name : str, optional
            Model identifier/name (defaults to ``"gpt-5.2"``).
        async_req : bool, optional
            When ``True``, returns a :class:`multiprocessing.pool.ApplyResult`.
        **kwargs
            Additional fields passed into :class:`~hipai_client.models.ModelConfigObject`
            when constructing one.

        Returns
        -------
        hipai_client.models.ModelConfigObject or multiprocessing.pool.ApplyResult
            The created/updated model config (or async result).

        Examples
        --------
        Create (no ``config`` passed):

        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> llm = client.upsert_llm_config(name="OpenAI Default", token="PROVIDER_TOKEN", model_name="gpt-5.2")
        >>> llm.name
        'OpenAI Default'

        Update (provide an existing object with an id and modified fields):

        >>> existing = client.list_llm_configs()[0]
        >>> existing.name = "OpenAI Default (Updated)"
        >>> updated = client.upsert_llm_config(config=existing)
        """
        assert config is not None or (name is not None and token is not None and model_name is not None), \
            "#upsert_llm_config requires either a ModelConfigObject or name, token, and model_name so that a ModelConfigObject can be constructed"
        if config is None:
            config = ModelConfigObject(name=name, token=token, model_name=model_name, **kwargs)
        return hipai_client.ModelConfigsApi(self.client).upsert_model_config_api_model_configs_post(config, async_req=async_req)

    def upsert_connection_config(
        self,
        connection_config: Optional[ConnectionConfigObject] = None,
        conn_schema: Optional[ConnectionSchema] = None,
        name: Optional[str] = None,
        hostname_path: str = "",
        graph_id: Optional[Union[str, UUID]] = None,
        group_id: Optional[Union[str, UUID]] = None,
        username: Optional[str] = None,
        password: Optional[str] = None,
        port: Optional[int] = None,
        database: Optional[str] = None,
        parameters: Optional[str] = None,
        account: Optional[str] = None,
        warehouse: Optional[str] = None,
        role: Optional[str] = None,
        sf_schema: Optional[str] = None,
        async_req: bool = None,
        **kwargs,
    ) -> Union[ConnectionConfigObject, ApplyResult]:
        """
        Create or update a connection configuration.

        You can either pass a fully-formed :class:`~hipai_client.models.ConnectionConfigObject`
        or pass convenience parameters (``conn_schema`` and ``name`` plus schema-specific fields),
        which will be validated and converted via :func:`instantiate_connection_config`.

        Parameters
        ----------
        connection_config : hipai_client.models.ConnectionConfigObject, optional
            Pre-built connection config object. If provided, it will be upserted directly.
        conn_schema : ConnectionSchema, optional
            Schema used when constructing a config (e.g. ``"postgresql"`` or ``"documents"``).
        name : str, optional
            Name used when constructing a config.
        hostname_path : str, optional
            Host/path for the connection (schema-dependent).
        graph_id : str or uuid.UUID, optional
            Optional graph/data-context id association.
        group_id : str or uuid.UUID, optional
            Optional group id association.
        username : str, optional
            Username for DB connections (required for some schemas).
        password : str, optional
            Password for DB connections (required for some schemas).
        port : int, optional
            DB port (optional for some schemas).
        database : str, optional
            DB name (required for mysql/postgresql).
        parameters : str, optional
            Additional connection parameters.
        account : str, optional
            Snowflake account (required for snowflake).
        warehouse : str, optional
            Snowflake warehouse (required for snowflake).
        role : str, optional
            Snowflake role (required for snowflake).
        sf_schema : str, optional
            Snowflake schema (required for snowflake).
        async_req : bool, optional
            When ``True``, returns a :class:`multiprocessing.pool.ApplyResult`.
        **kwargs
            Additional fields passed to the config object constructor.

        Returns
        -------
        hipai_client.models.ConnectionConfigObject or multiprocessing.pool.ApplyResult
            The created/updated connection configuration (or async result).

        Examples
        --------
        Create (documents):

        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> created = client.upsert_connection_config(conn_schema="documents", name="Uploads", group_id="GROUP_ID")
        >>> created.conn_schema
        'documents'

        Create (postgresql):

        >>> created = client.upsert_connection_config(
        ...     conn_schema="postgresql",
        ...     name="Warehouse",
        ...     hostname_path="db.example.com",
        ...     username="analytics",
        ...     password="secret",
        ...     database="prod",
        ...     port=5432,
        ... )

        Update (fetch, modify, upsert):

        >>> existing = client.list_connection_configs()[0]
        >>> existing.name = "Warehouse (Updated)"
        >>> updated = client.upsert_connection_config(connection_config=existing)
        """
        assert connection_config is not None or (conn_schema is not None and name is not None), \
            "#upsert_connection_config requires either a valid ConnectionConfigObject or conn_schema and name parameters."
        connection_config = connection_config or instantiate_connection_config(
            conn_schema,
            name,
            hostname_path,
            graph_id,
            group_id,
            username,
            password,
            port,
            database,
            parameters,
            account,
            warehouse,
            role,
            sf_schema,
            **kwargs,
        )
        return hipai_client.ConnectionConfigsApi(self.client).upsert_connection_config_api_connection_configs_post(
            connection_config, async_req=async_req
        )

    def upsert_data_context(
        self,
        data_context: Optional[DataContextObject] = None,
        name: Optional[str] = None,
        llm_config_id: Optional[Union[str, UUID]] = None,
        group_id: Optional[Union[str, UUID]] = None,
        connection_config_ids: Optional[List[str]] = None,
        build: bool = False,
        async_req: bool = False,
        **kwargs,
    ) -> Union[DataContextObject, ApplyResult]:
        """
        Create or update a data context.

        A data context typically references a model configuration and one or more
        connection configurations. When ``build=True``, the data context is created in a
        queued state so the backend can build/index it.

        Parameters
        ----------
        data_context : hipai_client.models.DataContextObject, optional
            Pre-built data context object to upsert.
        name : str, optional
            Name used when constructing a data context.
        llm_config_id : str or uuid.UUID, optional
            Associated LLM config id.
        group_id : str or uuid.UUID, optional
            Group isolation id to associate.
        connection_config_ids : list[str], optional
            Connection config ids referenced by this data context.
        build : bool, optional
            If ``True``, sets status to ``queued`` (to trigger building). Otherwise uses ``draft``.
        async_req : bool, optional
            When ``True``, returns a :class:`multiprocessing.pool.ApplyResult`.
        **kwargs
            Additional fields passed to :class:`~hipai_client.models.DataContextObject`
            when constructing one.

        Returns
        -------
        hipai_client.models.DataContextObject or multiprocessing.pool.ApplyResult
            The created/updated data context (or async result).

        Examples
        --------
        Create (draft):

        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> dc = client.upsert_data_context(
        ...     name="Customer Support",
        ...     llm_config_id="LLM_ID",
        ...     group_id="GROUP_ID",
        ...     connection_config_ids=["CONN_ID_1", "CONN_ID_2"],
        ...     build=False,
        ... )

        Create and trigger build:

        >>> dc = client.upsert_data_context(
        ...     name="Customer Support",
        ...     llm_config_id="LLM_ID",
        ...     group_id="GROUP_ID",
        ...     connection_config_ids=["CONN_ID_1"],
        ...     build=True,
        ... )
        >>> dc.status in ("queued", "preparing", "ready", "rebuilding", "draft")
        True

        Update (modify existing object):

        >>> existing = client.list_data_contexts()[0]
        >>> existing.name = "Customer Support (Updated)"
        >>> updated = client.upsert_data_context(data_context=existing)
        """
        assert data_context is not None or name is not None, \
            "#upsert_data_context requires either a valid DataContextObject or a name parameter passed."
        if isinstance(llm_config_id, UUID):
            llm_config_id = str(llm_config_id)
        if isinstance(group_id, UUID):
            group_id = str(group_id)
        data_context = data_context or DataContextObject(
            name=name,
            llm_config_id=llm_config_id,
            group_id=group_id,
            config_ids=connection_config_ids,
            status=DataContextStatuses.QUEUED.value if build else DataContextStatuses.DRAFT.value,
            **kwargs,
        )
        return hipai_client.DataContextsApi(self.client).upsert_data_context_api_data_contexts_post(
            data_context, async_req=async_req
        )

    def upsert_agent(
        self,
        agent: Optional[AgentConfigObject] = None,
        name: Optional[str] = None,
        status: Optional[AgentStatus] = None,
        data_context_id: Optional[Union[str, UUID]] = None,
        llm_config_id: Optional[Union[str, UUID]] = None,
        group_id: Optional[Union[str, UUID]] = None,
        async_req: bool = False,
        **kwargs,
    ) -> Union[AgentConfigObject, ApplyResult]:
        """
        Create or update an agent configuration.

        Provide either a full :class:`~hipai_client.models.AgentConfigObject` or enough fields
        to construct one (``name``, ``status``, and ``data_context_id``).

        Parameters
        ----------
        agent : hipai_client.models.AgentConfigObject, optional
            Pre-built agent config object.
        name : str, optional
            Agent name used when constructing an agent config.
        status : AgentStatus, optional
            Agent status (``"active"`` or ``"inactive"``).
        data_context_id : str or uuid.UUID, optional
            Data context (graph) id to associate with the agent.
        llm_config_id : str or uuid.UUID, optional
            Optional LLM config id override for the agent.
        group_id : str or uuid.UUID, optional
            Group isolation id to associate.
        async_req : bool, optional
            When ``True``, returns a :class:`multiprocessing.pool.ApplyResult`.
        **kwargs
            Additional fields passed to :class:`~hipai_client.models.AgentConfigObject`
            when constructing one.

        Returns
        -------
        hipai_client.models.AgentConfigObject or multiprocessing.pool.ApplyResult
            The created/updated agent config (or async result).

        Examples
        --------
        Create:

        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> agent = client.upsert_agent(
        ...     name="Support Agent",
        ...     status="active",
        ...     data_context_id="DATA_CONTEXT_ID",
        ...     llm_config_id="LLM_ID",
        ...     group_id="GROUP_ID",
        ... )

        Update:

        >>> existing = client.list_agents()[0]
        >>> existing.status = "inactive"
        >>> updated = client.upsert_agent(agent=existing)
        """
        assert agent is not None or (name is not None and status is not None and data_context_id is not None), \
            "#upsert_agent requires either a valid AgentConfigObject or a valid name, status, and data_context_id to be passed."
        if isinstance(llm_config_id, UUID):
            llm_config_id = str(llm_config_id)
        if isinstance(data_context_id, UUID):
            data_context_id = str(data_context_id)
        if isinstance(group_id, UUID):
            group_id = str(group_id)
        agent = agent or AgentConfigObject(
            name=name,
            status=status,
            graph_id=data_context_id,
            llm_config_id=llm_config_id,
            group_id=group_id,
            **kwargs,
        )
        return hipai_client.AgentsApi(self.client).upsert_agent_api_agents_post(agent, async_req=async_req)

    def upload_file(
        self,
        file_name: str,
        file: Any,
        file_mime_type: str,
        connection_config: ConnectionConfigObject,
    ):
        """
        Upload a document to a ``documents`` connection config using multipart/form-data.

        Notes
        -----
        The Swagger/OpenAPI autogenerated upload code can be inefficient or incorrect for large
        files (e.g., > 1MB). This method uses :mod:`requests` and
        :class:`requests_toolbelt.multipart.encoder.MultipartEncoder` directly.

        Parameters
        ----------
        file_name : str
            Name to assign to the file on upload (e.g., ``"handbook.pdf"``).
        file : Any
            A file-like object opened in binary mode (must be readable).
        file_mime_type : str
            MIME type for the file (e.g., ``"application/pdf"``).
        connection_config : hipai_client.models.ConnectionConfigObject
            The documents connection configuration to associate with the upload.

        Returns
        -------
        requests.Response
            The HTTP response from the upload endpoint.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> conn = client.upsert_connection_config(conn_schema="documents", name="Uploads")
        >>> with open("handbook.pdf", "rb") as f:
        ...     resp = client.upload_file(
        ...         file_name="handbook.pdf",
        ...         file=f,
        ...         file_mime_type="application/pdf",
        ...         connection_config=conn,
        ...     )
        >>> resp.status_code in (200, 201, 202, 204)
        True
        """
        encoded_data = MultipartEncoder(
            fields={
                "request": json.dumps(connection_config.to_dict()),
                "file": (file_name, file, file_mime_type),
            }
        )
        headers = {
            "Authorization": f"Bearer {self.conf.access_token}",
            "Accept": "application/json",
            "Content-Type": encoded_data.content_type,
        }
        return requests.post(
            f"{self.conf.host}//api/connection-configs/document-upload",
            data=encoded_data,
            headers=headers,
        )

    def load_connection_config(self, id: Union[UUID, str], **kwargs) -> ConnectionConfigObject:
        """
        Load a connection configuration by id.

        Parameters
        ----------
        id : uuid.UUID or str
            Connection config id.
        **kwargs
            Additional keyword arguments passed through to the underlying OpenAPI call.

        Returns
        -------
        hipai_client.models.ConnectionConfigObject
            The loaded connection configuration.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> cfg = client.load_connection_config("CONN_ID")
        """
        if isinstance(id, UUID):
            id = str(id)
        return hipai_client.ConnectionConfigsApi(self.client).load_connection_config_api_connection_configs_id_get(
            id, **kwargs
        )

    def load_data_context(self, id: Union[UUID, str], **kwargs) -> DataContextObject:
        """
        Load a data context by id.

        Parameters
        ----------
        id : uuid.UUID or str
            Data context id.
        **kwargs
            Additional keyword arguments passed through to the underlying OpenAPI call.

        Returns
        -------
        hipai_client.models.DataContextObject
            The loaded data context.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> dc = client.load_data_context("DATA_CONTEXT_ID")
        """
        if isinstance(id, UUID):
            id = str(id)
        return hipai_client.DataContextsApi(self.client).load_data_context_api_data_contexts_id_get(id, **kwargs)

    def load_agent(self, id: Union[UUID, str], **kwargs) -> AgentConfigObject:
        """
        Load an agent by id.

        Parameters
        ----------
        id : uuid.UUID or str
            Agent id.
        **kwargs
            Additional keyword arguments passed through to the underlying OpenAPI call.

        Returns
        -------
        hipai_client.models.AgentConfigObject
            The loaded agent configuration.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> agent = client.load_agent("AGENT_ID")
        """
        if isinstance(id, UUID):
            id = str(id)
        return hipai_client.AgentsApi(self.client).load_agent_api_agents_id_get(id, **kwargs)

    def list_llm_configs(self, group_id: Optional[Union[str, UUID]] = None):
        """
        List LLM model configurations (optionally filtered by group).

        Parameters
        ----------
        group_id : str or uuid.UUID, optional
            Group isolation id to filter results.

        Returns
        -------
        list[hipai_client.models.ModelConfigObject]
            A list of model configs.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> configs = client.list_llm_configs(group_id="GROUP_ID")
        >>> isinstance(configs, list)
        True
        """
        if isinstance(group_id, UUID):
            group_id = str(group_id)
        return [ModelConfigObject(**model_config) for model_config in hipai_client.ModelConfigsApi(self.client).list_model_configs_api_model_configs_list_post(
            hipai_client.GroupRequest(group_id=group_id)
        ).data]

    def list_connection_configs(self, group_id: Optional[Union[str, UUID]] = None):
        """
        List connection configurations (optionally filtered by group).

        Parameters
        ----------
        group_id : str or uuid.UUID, optional
            Group isolation id to filter results.

        Returns
        -------
        list[hipai_client.models.ConnectionConfigObject]
            A list of connection configs.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> conns = client.list_connection_configs(group_id="GROUP_ID")
        >>> isinstance(conns, list)
        True
        """
        if isinstance(group_id, UUID):
            group_id = str(group_id)
        return [ConnectionConfigObject(**config) for config in hipai_client.ConnectionConfigsApi(self.client).list_connection_configs_api_connection_configs_list_post(
            hipai_client.ApiConnectionConfigsModelsListRequest(group_id=group_id)
        ).data]

    def list_data_contexts(self, group_id: Optional[Union[str, UUID]] = None, only_ready: bool = False):
        """
        List data contexts (optionally filtered by group), optionally limited to ready/active contexts.

        Note
        ----
        This method passes ``only_ready`` through as ``only_active`` to the backend request object.

        Parameters
        ----------
        group_id : str or uuid.UUID, optional
            Group isolation id to filter results.
        only_ready : bool, optional
            If ``True``, request only ready/active data contexts (backend-dependent).

        Returns
        -------
        list[hipai_client.models.DataContextObject]
            A list of data contexts.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> dcs = client.list_data_contexts(group_id="GROUP_ID", only_ready=True)
        >>> isinstance(dcs, list)
        True
        """
        if isinstance(group_id, UUID):
            group_id = str(group_id)
        return [DataContextObject(**context) for context in hipai_client.DataContextsApi(self.client).list_data_contexts_api_data_contexts_list_post(
            hipai_client.ApiDataContextsModelsListRequest(group_id=group_id, only_active=only_ready)
        ).data]

    def list_groups(self):
        """
        List groups for company.

        Returns
        -------
        list[hipai_client.models.GroupIsolationObject]
            A list of groups.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> agents = client.list_groups()
        >>> isinstance(agents, list)
        True
        """
        return [GroupIsolationObject(**group) for group in hipai_client.GroupsApi(self.client).list_groups_api_groups_list_get().data]

    def list_users(self):
        """
        List users.

        Returns
        -------
        list[hipai_client.models.UserPublic]
            A list of users.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> users = client.list_users()
        >>> isinstance(users, list)
        True
        """
        return [UserPublic(**user) for user in hipai_client.TeamApi(self.client).list_team_members_api_team_members_get().data]

    def list_agents(self, group_id: Optional[Union[str, UUID]] = None):
        """
        List agent configurations (optionally filtered by group).

        Parameters
        ----------
        group_id : str or uuid.UUID, optional
            Group isolation id to filter results.

        Returns
        -------
        list[hipai_client.models.AgentConfigObject]
            A list of agents.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> agents = client.list_agents(group_id="GROUP_ID")
        >>> isinstance(agents, list)
        True
        """
        if isinstance(group_id, UUID):
            group_id = str(group_id)
        return [AgentConfigObject(**agent) for agent in hipai_client.AgentsApi(self.client).list_agents_api_agents_list_post(
            hipai_client.GroupRequest(group_id=group_id)
        ).data]

    def chat(
        self,
        prompt: str,
        agent_api_key: str,
        group_id: Optional[Union[str, UUID]] = None,
        ongoing: Optional[List[Dict[str, str]]] = None,
    ):
        """
        Send a chat completion request and return the assistant response plus updated message history.

        This helper maintains an in-memory message list for multi-turn conversations. Pass an existing
        ``ongoing`` message list to continue a conversation; otherwise a new list is created.

        Parameters
        ----------
        prompt : str
            User message content to send to the chat endpoint.
        agent_api_key : str
            Agent API key used to route the request.
        group_id : str or uuid.UUID, optional
            Optional group isolation id.
        ongoing : list[dict[str, str]], optional
            Existing list of messages of the form ``{"role": "...", "content": "..."}``.
            If provided, the new user prompt and assistant response are appended.

        Returns
        -------
        tuple
            ``(response_content, messages, response)`` where:

            * ``response_content`` is the assistant's text content.
            * ``messages`` is the updated messages list.
            * ``response`` is the full OpenAPI response object.

        Examples
        --------
        Start a conversation:

        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> text, messages, raw = client.chat(prompt="Hello!", agent_api_key="AGENT_KEY")
        >>> isinstance(text, str)
        True

        Continue the conversation:

        >>> text2, messages, raw2 = client.chat(prompt="Tell me a joke.", agent_api_key="AGENT_KEY", ongoing=messages)
        """
        if isinstance(group_id, UUID):
            group_id = str(group_id)
        messages = ongoing or []
        messages.append({"role": "user", "content": prompt})
        request = ChatCompletionRequest(messages=messages, agent_api_key=agent_api_key, group_id=group_id)
        response = hipai_client.ChatApi(self.client).completions_api_chat_completions_post(request)
        response_content = response.choices[0]["message"]["content"]
        messages.append({"role": "assistant", "content": response_content})
        return response_content, messages, response

    def delete_llm_config(self, id: Optional[Union[str, UUID]]):
        """
        Delete an LLM model configuration by id.

        Parameters
        ----------
        id : str or uuid.UUID, optional
            Model config id to delete.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> client.delete_llm_config("LLM_ID")
        """
        if isinstance(id, UUID):
            id = str(id)
        hipai_client.ModelConfigsApi(self.client).delete_model_config_api_model_configs_id_delete(id)

    def delete_group(self, id: Optional[Union[str, UUID]]):
        """
        Delete a group by id.

        Parameters
        ----------
        id : str or uuid.UUID, optional
            Group id to delete.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> client.delete_group("GROUP_ID")
        """
        if isinstance(id, UUID):
            id = str(id)
        hipai_client.GroupsApi(self.client).delete_group_api_groups_id_delete(id)

    def delete_connection_config(self, id: Optional[Union[str, UUID]]):
        """
        Delete a connection configuration by id.

        Parameters
        ----------
        id : str or uuid.UUID, optional
            Connection config id to delete.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> client.delete_connection_config("CONN_ID")
        """
        if isinstance(id, UUID):
            id = str(id)
        hipai_client.ConnectionConfigsApi(self.client).delete_connection_config_api_connection_configs_id_delete(id)

    def delete_data_context(self, id: Optional[Union[str, UUID]]):
        """
        Delete a data context by id.

        Parameters
        ----------
        id : str or uuid.UUID, optional
            Data context id to delete.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> client.delete_data_context("DATA_CONTEXT_ID")
        """
        if isinstance(id, UUID):
            id = str(id)
        hipai_client.DataContextsApi(self.client).delete_data_context_api_data_contexts_id_delete(id)

    def delete_agent(self, id: Optional[Union[str, UUID]]):
        """
        Delete an agent by id.

        Parameters
        ----------
        id : str or uuid.UUID, optional
            Agent id to delete.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> client.delete_agent("AGENT_ID")
        """
        if isinstance(id, UUID):
            id = str(id)
        hipai_client.AgentsApi(self.client).delete_agent_api_agents_id_delete(id)

    def add_new_user(self, email: str, first_name: str = "", last_name: str = "", is_admin: bool = False):
        """
        Add a new User.

        Parameters
        ----------
        email : str
            The email of the user.
        first_name : str, optional
            The user's first name.
        last_name : str, optional
            The user's last name.
        is_admin : bool, optional
            Defaults to False, when ``True`` adds the user as an admin (otherwise the user is added as a member).

        Returns
        -------
        hipai_client.models.UserPublic
            The added User.

        Examples
        --------

        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> user = client.add_new_user(name="test@gmail.com", first_name="John", last_name="Smith", is_admin=True)
        >>> user.first_name
        'John'
        """
        new_user = UserPublic(email=email, first_name=first_name, last_name=last_name, permission_group="admin" if is_admin else "member")
        return hipai_client.TeamApi(self.client).upsert_team_member_api_team_members_upsert_post(new_user)

    def remove_user(self, id: Union[str, UUID]):
        """
        remove a user by id.

        Parameters
        ----------
        id : str or uuid.UUID, optional
            User id to remove.

        Examples
        --------
        >>> client = SimpleHipAIClient(access_token="YOUR_TOKEN")
        >>> client.remove_user("AGENT_ID")
        """
        if isinstance(id, UUID):
            id = str(id)
        return hipai_client.TeamApi(self.client).remove_team_member_api_team_members_user_id_delete(id)
