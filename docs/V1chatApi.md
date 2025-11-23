# hipai_client.V1chatApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**completions_v1_chat_completions_post**](V1chatApi.md#completions_v1_chat_completions_post) | **POST** /v1/chat/completions | Completions

# **completions_v1_chat_completions_post**
> ChatCompletion completions_v1_chat_completions_post(body)

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
api_instance = hipai_client.V1chatApi(hipai_client.ApiClient(configuration))
body = hipai_client.ChatCompletionRequest() # ChatCompletionRequest | 

try:
    # Completions
    api_response = api_instance.completions_v1_chat_completions_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling V1chatApi->completions_v1_chat_completions_post: %s\n" % e)
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

