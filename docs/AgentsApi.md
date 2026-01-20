# hipai_client.AgentsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_agent_api_agents_id_delete**](AgentsApi.md#delete_agent_api_agents_id_delete) | **DELETE** /api/agents/{id} | Delete Agent
[**list_agents_api_agents_list_get**](AgentsApi.md#list_agents_api_agents_list_get) | **GET** /api/agents/list | List Agents
[**load_agent_api_agents_id_get**](AgentsApi.md#load_agent_api_agents_id_get) | **GET** /api/agents/{id} | Load Agent
[**upsert_agent_api_agents_post**](AgentsApi.md#upsert_agent_api_agents_post) | **POST** /api/agents/ | Upsert Agent

# **delete_agent_api_agents_id_delete**
> Message delete_agent_api_agents_id_delete(id)

Delete Agent

Deletes an Agent Config. Admin only.

### Example
```python
from __future__ import print_function
import time
import hipai_client
from hipai_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = hipai_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = hipai_client.AgentsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Delete Agent
    api_response = api_instance.delete_agent_api_agents_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->delete_agent_api_agents_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_agents_api_agents_list_get**
> ApiAgentsModelsListResponse list_agents_api_agents_list_get()

List Agents

### Example
```python
from __future__ import print_function
import time
import hipai_client
from hipai_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = hipai_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = hipai_client.AgentsApi(hipai_client.ApiClient(configuration))

try:
    # List Agents
    api_response = api_instance.list_agents_api_agents_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->list_agents_api_agents_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiAgentsModelsListResponse**](ApiAgentsModelsListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_agent_api_agents_id_get**
> AgentConfigObject load_agent_api_agents_id_get(id)

Load Agent

### Example
```python
from __future__ import print_function
import time
import hipai_client
from hipai_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = hipai_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = hipai_client.AgentsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Load Agent
    api_response = api_instance.load_agent_api_agents_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->load_agent_api_agents_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**AgentConfigObject**](AgentConfigObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_agent_api_agents_post**
> AgentConfigObject upsert_agent_api_agents_post(body)

Upsert Agent

### Example
```python
from __future__ import print_function
import time
import hipai_client
from hipai_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2PasswordBearer
configuration = hipai_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = hipai_client.AgentsApi(hipai_client.ApiClient(configuration))
body = hipai_client.AgentConfigObject() # AgentConfigObject | 

try:
    # Upsert Agent
    api_response = api_instance.upsert_agent_api_agents_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->upsert_agent_api_agents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentConfigObject**](AgentConfigObject.md)|  | 

### Return type

[**AgentConfigObject**](AgentConfigObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

