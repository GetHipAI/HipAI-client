# hipai_client.SimpleHipAIClient

The SimpleHipAIClient is a simplified client which wraps the broader functionality of hipai_client. For specific function annotations and behavior please see [documentation in the client code](../hipai_client/simple_client.py).

## Usage examples

Below are examples of interacting with and managing core HipAI functionality via the SimpleHipAIClient

### LLM Configuration setup

For performance and cost purposes it is often necessary to specify and set your own OpenAI API Token so that it can be used for graph construction and agent chat completions. Your LLM config can be set and updated like so:

```python
from hipai_client import SimpleHipAIClient

# creation
client = SimpleHipAIClient(access_token=HIPAI_API_TOKEN)
llm_config = client.upsert_llm_config(name="my llm config", token=OPENAI_API_TOKEN)

# update
llm_config.name = "different name"
client.upsert_llm_config(llm_config)

#removal
client.delete_llm_config(llm_config.id)
```

### Isolation Group setup

In order to insulate data and operations, it can be helpful to create and assign a distinct isolation group. This can be achieved like so:

```python
from hipai_client import SimpleHipAIClient

# creation
client = SimpleHipAIClient(access_token=HIPAI_API_TOKEN)
group = client.create_group(name="group 1")

# removal
client.delete_group(group.id)
```

### Creating a Document-based Data Context

Data Contexts represent the combination of data from multiple Connection Configurations where each Connection Configuration describes a distinct data source. For creating and updating a Document based Data Context, a single Connection Configuration with the `documents` schema can be used to host many uploaded documents and can manage incremental updates. A Document based Data Context can be built and updated like so:

```python
from hipai_client import SimpleHipAIClient
import os

llm_config_id = None  # specify an LLM Config id here if you'd like to use one
group_id = None  # specify a Group id here if you'd like to assign the data context to a Isolation Group 
file_path = "./test.pdf"  # specify a local PDF file that you would like to upload her


# creation
client = SimpleHipAIClient(access_token=HIPAI_API_TOKEN)

connection_config = client.upsert_connection_config(name="document config", conn_schema='documents', group_id=group_id)
with open(file_path, "rb") as f:
    client.upload_file(os.path.basename(file_path), f, "application/pdf", connection_config)

data_context = client.upsert_data_context(name="document data context", group_id=group_id, llm_config_id=llm_config_id, connection_config_ids=[connection_config.id], build=True)

# check data context status
is_ready = client.load_data_context(data_context.id).status == "ready"

# update and rebuild
added_file_path = "./test2.pdf"
data_context = client.load_data_context(data_context.id)
connection_config = client.load_connection_configuration(connection_configuration.id)

with open(added_file_path, "rb") as f:
    client.upload_file(os.path.basename(added_file_path), f, "application/pdf", connection_config)

data_context = client.upsert_data_context(data_context, build=True)
```

### Creating and Chatting with an Agent

In order to create an Agent you must first build a Data Context and confirm that it is in a `ready` or `rebuilding` state. Once your data context is ready you can configure and chat with your agent like so:

```python
from hipai_client import SimpleHipAIClient

llm_config_id = None  # specify an LLM Config id here if you'd like to use one
group_id = None  # specify a Group id here if you'd like to assign the data context to a Isolation Group
status = "active"  # set this to inactive if you want to limit access to admins only.

# creation
agent = client.upsert_agent(name="agent 1", status='active', data_context_id=data_context.id, llm_config_id=llm_config_id, group_id=group_id)

# chat
chat_response, _, _ = client.chat("my question or prompt", agent_api_key=agent.api_key, group_id=group_id)

# update
agent.name = "different agent name"
client.upsert_agent(agent)

# removal
client.delete_agent(agent.id)
```


