# hipai_client.DataContextsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**data_context_upsert_data_contexts_post**](DataContextsApi.md#data_context_upsert_data_contexts_post) | **POST** /data-contexts/ | Data Context Upsert
[**get_list_data_contexts_list_get**](DataContextsApi.md#get_list_data_contexts_list_get) | **GET** /data-contexts/list | Get List
[**load_data_contexts_get**](DataContextsApi.md#load_data_contexts_get) | **GET** /data-contexts/ | Load

# **data_context_upsert_data_contexts_post**
> DataContextResponse data_context_upsert_data_contexts_post(body)

Data Context Upsert

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
body = hipai_client.ConnectionConfigRequest() # ConnectionConfigRequest | 

try:
    # Data Context Upsert
    api_response = api_instance.data_context_upsert_data_contexts_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataContextsApi->data_context_upsert_data_contexts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionConfigRequest**](ConnectionConfigRequest.md)|  | 

### Return type

[**DataContextResponse**](DataContextResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_data_contexts_list_get**
> ApiDataContextsModelsListResponse get_list_data_contexts_list_get()

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
api_instance = hipai_client.DataContextsApi(hipai_client.ApiClient(configuration))

try:
    # Get List
    api_response = api_instance.get_list_data_contexts_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataContextsApi->get_list_data_contexts_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiDataContextsModelsListResponse**](ApiDataContextsModelsListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_data_contexts_get**
> DataContextResponse load_data_contexts_get(body)

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
api_instance = hipai_client.DataContextsApi(hipai_client.ApiClient(configuration))
body = hipai_client.LoadRequest() # LoadRequest | 

try:
    # Load
    api_response = api_instance.load_data_contexts_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DataContextsApi->load_data_contexts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LoadRequest**](LoadRequest.md)|  | 

### Return type

[**DataContextResponse**](DataContextResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

