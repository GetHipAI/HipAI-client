# hipai_client.LoginApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**forgot_password_auth_forgot_password_post**](LoginApi.md#forgot_password_auth_forgot_password_post) | **POST** /auth/forgot-password | Forgot Password
[**login_access_token_login_access_token_post**](LoginApi.md#login_access_token_login_access_token_post) | **POST** /login/access-token | Login Access Token
[**login_google_login_google_post**](LoginApi.md#login_google_login_google_post) | **POST** /login/google | Login Google
[**request_access_auth_request_access_post**](LoginApi.md#request_access_auth_request_access_post) | **POST** /auth/request-access | Request Access
[**reset_password_auth_reset_password_post**](LoginApi.md#reset_password_auth_reset_password_post) | **POST** /auth/reset-password | Reset Password
[**verify_reset_token_auth_verify_reset_token_token_get**](LoginApi.md#verify_reset_token_auth_verify_reset_token_token_get) | **GET** /auth/verify-reset-token/{token} | Verify Reset Token

# **forgot_password_auth_forgot_password_post**
> Message forgot_password_auth_forgot_password_post(body)

Forgot Password

Initiate password reset flow by sending reset email.  Security considerations: - Always returns success to prevent email enumeration attacks - Only sends email if user exists and is not SSO-only - Rate limiting should be added at infrastructure level (API Gateway)

### Example
```python
from __future__ import print_function
import time
import hipai_client
from hipai_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hipai_client.LoginApi()
body = hipai_client.ForgotPasswordRequest() # ForgotPasswordRequest | 

try:
    # Forgot Password
    api_response = api_instance.forgot_password_auth_forgot_password_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->forgot_password_auth_forgot_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ForgotPasswordRequest**](ForgotPasswordRequest.md)|  | 

### Return type

[**Message**](Message.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

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

# **login_google_login_google_post**
> Token login_google_login_google_post(body)

Login Google

Google OAuth login - verify Google token and create/login user

### Example
```python
from __future__ import print_function
import time
import hipai_client
from hipai_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hipai_client.LoginApi()
body = hipai_client.GoogleLoginRequest() # GoogleLoginRequest | 

try:
    # Login Google
    api_response = api_instance.login_google_login_google_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->login_google_login_google_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GoogleLoginRequest**](GoogleLoginRequest.md)|  | 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_access_auth_request_access_post**
> Message request_access_auth_request_access_post(body)

Request Access

Submit a request access form.  Sends an email to request@gethip.ai with the form data. Always returns success to prevent information disclosure.

### Example
```python
from __future__ import print_function
import time
import hipai_client
from hipai_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hipai_client.LoginApi()
body = hipai_client.RequestAccessRequest() # RequestAccessRequest | 

try:
    # Request Access
    api_response = api_instance.request_access_auth_request_access_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->request_access_auth_request_access_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RequestAccessRequest**](RequestAccessRequest.md)|  | 

### Return type

[**Message**](Message.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_password_auth_reset_password_post**
> Message reset_password_auth_reset_password_post(body)

Reset Password

Reset user password using valid token.  Security considerations: - Token must be valid, not expired, and not previously used - Token is single-use only - Password is hashed via custom Password type

### Example
```python
from __future__ import print_function
import time
import hipai_client
from hipai_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hipai_client.LoginApi()
body = hipai_client.ResetPasswordRequest() # ResetPasswordRequest | 

try:
    # Reset Password
    api_response = api_instance.reset_password_auth_reset_password_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->reset_password_auth_reset_password_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetPasswordRequest**](ResetPasswordRequest.md)|  | 

### Return type

[**Message**](Message.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_reset_token_auth_verify_reset_token_token_get**
> Message verify_reset_token_auth_verify_reset_token_token_get(token)

Verify Reset Token

Verify if a password reset token is valid (frontend can check before showing form).

### Example
```python
from __future__ import print_function
import time
import hipai_client
from hipai_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hipai_client.LoginApi()
token = NULL # object | 

try:
    # Verify Reset Token
    api_response = api_instance.verify_reset_token_auth_verify_reset_token_token_get(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->verify_reset_token_auth_verify_reset_token_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | [**object**](.md)|  | 

### Return type

[**Message**](Message.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

