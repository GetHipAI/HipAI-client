# hipai_client.LoginApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_access_token_login_access_token_post**](LoginApi.md#login_access_token_login_access_token_post) | **POST** /login/access-token | Login Access Token

# **login_access_token_login_access_token_post**
> Token login_access_token_login_access_token_post(grant_type, username, password, scope, client_id, client_secret)

Login Access Token

OAuth2 compatible token login, get an access token for future requests

### Example
```python
from __future__ import print_function
import time
import hipai_client
from hipai_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hipai_client.LoginApi()
grant_type = NULL # object | 
username = NULL # object | 
password = NULL # object | 
scope = NULL # object | 
client_id = NULL # object | 
client_secret = NULL # object | 

try:
    # Login Access Token
    api_response = api_instance.login_access_token_login_access_token_post(grant_type, username, password, scope, client_id, client_secret)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login_access_token_login_access_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_type** | [**object**](.md)|  | 
 **username** | [**object**](.md)|  | 
 **password** | [**object**](.md)|  | 
 **scope** | [**object**](.md)|  | 
 **client_id** | [**object**](.md)|  | 
 **client_secret** | [**object**](.md)|  | 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

