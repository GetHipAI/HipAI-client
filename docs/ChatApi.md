# hipai_client.ChatApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_chat_post**](ChatApi.md#chat_chat_post) | **POST** /chat/ | Chat
[**get_list_chat_list_get**](ChatApi.md#get_list_chat_list_get) | **GET** /chat/list | Get List
[**load_chat_load_get**](ChatApi.md#load_chat_load_get) | **GET** /chat/load | Load

# **chat_chat_post**
> ChatResponse chat_chat_post(body)

Chat

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
api_instance = hipai_client.ChatApi(hipai_client.ApiClient(configuration))
body = NULL # object | 

try:
    # Chat
    api_response = api_instance.chat_chat_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_chat_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 

### Return type

[**ChatResponse**](ChatResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_list_chat_list_get**
> ApiChatModelsListResponse get_list_chat_list_get(body)

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
api_instance = hipai_client.ChatApi(hipai_client.ApiClient(configuration))
body = hipai_client.ListRequest() # ListRequest | 

try:
    # Get List
    api_response = api_instance.get_list_chat_list_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_list_chat_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ListRequest**](ListRequest.md)|  | 

### Return type

[**ApiChatModelsListResponse**](ApiChatModelsListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_chat_load_get**
> LoadResponse load_chat_load_get(body)

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
api_instance = hipai_client.ChatApi(hipai_client.ApiClient(configuration))
body = NULL # object | 

try:
    # Load
    api_response = api_instance.load_chat_load_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->load_chat_load_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**object**](object.md)|  | 

### Return type

[**LoadResponse**](LoadResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

