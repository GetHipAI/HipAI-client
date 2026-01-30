# hipai_client.UsersApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_replacement_api_key_api_users_api_keys_generate_replacement_post**](UsersApi.md#generate_replacement_api_key_api_users_api_keys_generate_replacement_post) | **POST** /api/users/api-keys/generate-replacement | Generate Replacement Api Key
[**get_api_key_api_users_api_keys_get**](UsersApi.md#get_api_key_api_users_api_keys_get) | **GET** /api/users/api-keys | Get Api Key
[**get_current_user_api_users_get**](UsersApi.md#get_current_user_api_users_get) | **GET** /api/users/ | Get Current User
[**replace_api_key_api_users_api_keys_replace_post**](UsersApi.md#replace_api_key_api_users_api_keys_replace_post) | **POST** /api/users/api-keys/replace | Replace Api Key
[**update_current_user_api_users_post**](UsersApi.md#update_current_user_api_users_post) | **POST** /api/users/ | Update Current User

# **generate_replacement_api_key_api_users_api_keys_generate_replacement_post**
> UserAPIKeys generate_replacement_api_key_api_users_api_keys_generate_replacement_post()

Generate Replacement Api Key

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
api_instance = hipai_client.UsersApi(hipai_client.ApiClient(configuration))

try:
    # Generate Replacement Api Key
    api_response = api_instance.generate_replacement_api_key_api_users_api_keys_generate_replacement_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->generate_replacement_api_key_api_users_api_keys_generate_replacement_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserAPIKeys**](UserAPIKeys.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_key_api_users_api_keys_get**
> UserAPIKeys get_api_key_api_users_api_keys_get()

Get Api Key

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
api_instance = hipai_client.UsersApi(hipai_client.ApiClient(configuration))

try:
    # Get Api Key
    api_response = api_instance.get_api_key_api_users_api_keys_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_api_key_api_users_api_keys_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserAPIKeys**](UserAPIKeys.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_current_user_api_users_get**
> UserPublic get_current_user_api_users_get()

Get Current User

Get current user with role and company information.

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
api_instance = hipai_client.UsersApi(hipai_client.ApiClient(configuration))

try:
    # Get Current User
    api_response = api_instance.get_current_user_api_users_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_current_user_api_users_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserPublic**](UserPublic.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **replace_api_key_api_users_api_keys_replace_post**
> UserAPIKeys replace_api_key_api_users_api_keys_replace_post()

Replace Api Key

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
api_instance = hipai_client.UsersApi(hipai_client.ApiClient(configuration))

try:
    # Replace Api Key
    api_response = api_instance.replace_api_key_api_users_api_keys_replace_post()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->replace_api_key_api_users_api_keys_replace_post: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserAPIKeys**](UserAPIKeys.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_current_user_api_users_post**
> UserPublic update_current_user_api_users_post(body)

Update Current User

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
api_instance = hipai_client.UsersApi(hipai_client.ApiClient(configuration))
body = hipai_client.UserPublic() # UserPublic | 

try:
    # Update Current User
    api_response = api_instance.update_current_user_api_users_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_current_user_api_users_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserPublic**](UserPublic.md)|  | 

### Return type

[**UserPublic**](UserPublic.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

