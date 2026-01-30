# hipai_client.DataContextsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**build_logs_api_data_contexts_logs_id_get**](DataContextsApi.md#build_logs_api_data_contexts_logs_id_get) | **GET** /api/data-contexts/logs/{id} | Build Logs
[**delete_data_context_api_data_contexts_id_delete**](DataContextsApi.md#delete_data_context_api_data_contexts_id_delete) | **DELETE** /api/data-contexts/{id} | Delete Data Context
[**list_data_contexts_api_data_contexts_list_post**](DataContextsApi.md#list_data_contexts_api_data_contexts_list_post) | **POST** /api/data-contexts/list | List Data Contexts
[**load_data_context_api_data_contexts_id_get**](DataContextsApi.md#load_data_context_api_data_contexts_id_get) | **GET** /api/data-contexts/{id} | Load Data Context
[**load_graph_api_data_contexts_graph_id_get**](DataContextsApi.md#load_graph_api_data_contexts_graph_id_get) | **GET** /api/data-contexts/graph/{id} | Load Graph
[**upsert_data_context_api_data_contexts_post**](DataContextsApi.md#upsert_data_context_api_data_contexts_post) | **POST** /api/data-contexts/ | Upsert Data Context

# **build_logs_api_data_contexts_logs_id_get**
> ListResponseLogs build_logs_api_data_contexts_logs_id_get(id)

Build Logs

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
api_instance = hipai_client.DataContextsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Build Logs
    api_response = api_instance.build_logs_api_data_contexts_logs_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataContextsApi->build_logs_api_data_contexts_logs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**ListResponseLogs**](ListResponseLogs.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_data_context_api_data_contexts_id_delete**
> Message delete_data_context_api_data_contexts_id_delete(id)

Delete Data Context

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
api_instance = hipai_client.DataContextsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Delete Data Context
    api_response = api_instance.delete_data_context_api_data_contexts_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataContextsApi->delete_data_context_api_data_contexts_id_delete: %s\n" % e)
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

# **list_data_contexts_api_data_contexts_list_post**
> ApiDataContextsModelsListResponse list_data_contexts_api_data_contexts_list_post(body)

List Data Contexts

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
api_instance = hipai_client.DataContextsApi(hipai_client.ApiClient(configuration))
body = hipai_client.ApiDataContextsModelsListRequest() # ApiDataContextsModelsListRequest | 

try:
    # List Data Contexts
    api_response = api_instance.list_data_contexts_api_data_contexts_list_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataContextsApi->list_data_contexts_api_data_contexts_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiDataContextsModelsListRequest**](ApiDataContextsModelsListRequest.md)|  | 

### Return type

[**ApiDataContextsModelsListResponse**](ApiDataContextsModelsListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_data_context_api_data_contexts_id_get**
> DataContextObject load_data_context_api_data_contexts_id_get(id)

Load Data Context

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
api_instance = hipai_client.DataContextsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Load Data Context
    api_response = api_instance.load_data_context_api_data_contexts_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataContextsApi->load_data_context_api_data_contexts_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**DataContextObject**](DataContextObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_graph_api_data_contexts_graph_id_get**
> GraphObject load_graph_api_data_contexts_graph_id_get(id)

Load Graph

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
api_instance = hipai_client.DataContextsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Load Graph
    api_response = api_instance.load_graph_api_data_contexts_graph_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataContextsApi->load_graph_api_data_contexts_graph_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**GraphObject**](GraphObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_data_context_api_data_contexts_post**
> DataContextObject upsert_data_context_api_data_contexts_post(body)

Upsert Data Context

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
api_instance = hipai_client.DataContextsApi(hipai_client.ApiClient(configuration))
body = hipai_client.DataContextObject() # DataContextObject | 

try:
    # Upsert Data Context
    api_response = api_instance.upsert_data_context_api_data_contexts_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataContextsApi->upsert_data_context_api_data_contexts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DataContextObject**](DataContextObject.md)|  | 

### Return type

[**DataContextObject**](DataContextObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

