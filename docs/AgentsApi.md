# hipai_client.AgentsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_config_upsert_agents_post**](AgentsApi.md#agent_config_upsert_agents_post) | **POST** /agents/ | Agent Config Upsert
[**get_list_agents_list_get**](AgentsApi.md#get_list_agents_list_get) | **GET** /agents/list | Get List
[**load_agents_get**](AgentsApi.md#load_agents_get) | **GET** /agents/ | Load

# **agent_config_upsert_agents_post**
> AgentConfigResponse agent_config_upsert_agents_post(body)

Agent Config Upsert

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
    # Agent Config Upsert
    api_response = api_instance.agent_config_upsert_agents_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->agent_config_upsert_agents_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AgentConfigObject**](AgentConfigObject.md)|  | 

### Return type

[**AgentConfigResponse**](AgentConfigResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_agents_list_get**
> ApiAgentsModelsListResponse get_list_agents_list_get()

Get List

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
    # Get List
    api_response = api_instance.get_list_agents_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->get_list_agents_list_get: %s\n" % e)
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

# **load_agents_get**
> AgentConfigResponse load_agents_get(body)

Load

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
body = hipai_client.LoadRequest() # LoadRequest | 

try:
    # Load
    api_response = api_instance.load_agents_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AgentsApi->load_agents_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoadRequest**](LoadRequest.md)|  | 

### Return type

[**AgentConfigResponse**](AgentConfigResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

