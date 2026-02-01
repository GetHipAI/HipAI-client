# hipai_client.ChatApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**completions_api_chat_completions_post**](ChatApi.md#completions_api_chat_completions_post) | **POST** /api/chat/completions | Completions
[**streaming_completions_api_chat_completions_stream_post**](ChatApi.md#streaming_completions_api_chat_completions_stream_post) | **POST** /api/chat/completions/stream | Streaming Completions

# **completions_api_chat_completions_post**
> ChatCompletion completions_api_chat_completions_post(body)

Completions

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
    # Completions
    api_response = api_instance.completions_api_chat_completions_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChatApi->completions_api_chat_completions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChatCompletionRequest**](ChatCompletionRequest.md)|  | 

### Return type

[**ChatCompletion**](ChatCompletion.md)

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

