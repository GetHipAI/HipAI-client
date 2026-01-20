# hipai_client.ChatApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_api_chat_post**](ChatApi.md#chat_api_chat_post) | **POST** /api/chat/ | Chat
[**get_list_api_chat_list_get**](ChatApi.md#get_list_api_chat_list_get) | **GET** /api/chat/list | Get List
[**load_api_chat_load_post**](ChatApi.md#load_api_chat_load_post) | **POST** /api/chat/load | Load
[**streaming_completions_api_chat_completions_stream_post**](ChatApi.md#streaming_completions_api_chat_completions_stream_post) | **POST** /api/chat/completions/stream | Streaming Completions

# **chat_api_chat_post**
> ChatResponse chat_api_chat_post(body)

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
    api_response = api_instance.chat_api_chat_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->chat_api_chat_post: %s\n" % e)
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

# **get_list_api_chat_list_get**
> ApiChatModelsListResponse get_list_api_chat_list_get(body)

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
body = hipai_client.ApiChatModelsListRequest() # ApiChatModelsListRequest | 

try:
    # Get List
    api_response = api_instance.get_list_api_chat_list_get(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->get_list_api_chat_list_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiChatModelsListRequest**](ApiChatModelsListRequest.md)|  | 

### Return type

[**ApiChatModelsListResponse**](ApiChatModelsListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_api_chat_load_post**
> LoadResponse load_api_chat_load_post(body)

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
    api_response = api_instance.load_api_chat_load_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->load_api_chat_load_post: %s\n" % e)
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

# **streaming_completions_api_chat_completions_stream_post**
> streaming_completions_api_chat_completions_stream_post(body)

Streaming Completions

This endpoint was form copied from the OpenAI /v1/chat interface. Because the streaming behavior is becoming bespoke to our use case, we have separated the v1/chat and this interface so as not to confuse v1/chat streaming with our dashboard streaming support.

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
body = hipai_client.ChatCompletionRequest() # ChatCompletionRequest | 

try:
    # Streaming Completions
    api_instance.streaming_completions_api_chat_completions_stream_post(body)
except ApiException as e:
    print("Exception when calling ChatApi->streaming_completions_api_chat_completions_stream_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChatCompletionRequest**](ChatCompletionRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

