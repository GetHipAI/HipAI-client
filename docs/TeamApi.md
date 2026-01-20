# hipai_client.TeamApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_team_members_api_team_members_get**](TeamApi.md#list_team_members_api_team_members_get) | **GET** /api/team/members | List Team Members
[**remove_team_member_api_team_members_user_id_delete**](TeamApi.md#remove_team_member_api_team_members_user_id_delete) | **DELETE** /api/team/members/{user_id} | Remove Team Member
[**reset_user_password_api_team_reset_password_user_id_post**](TeamApi.md#reset_user_password_api_team_reset_password_user_id_post) | **POST** /api/team/reset-password/{user_id} | Reset User Password
[**upsert_team_member_api_team_members_upsert_post**](TeamApi.md#upsert_team_member_api_team_members_upsert_post) | **POST** /api/team/members/upsert | Upsert Team Member

# **list_team_members_api_team_members_get**
> ApiAuthModelsListResponse list_team_members_api_team_members_get()

List Team Members

List all members in the current user's organization.

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
api_instance = hipai_client.TeamApi(hipai_client.ApiClient(configuration))

try:
    # List Team Members
    api_response = api_instance.list_team_members_api_team_members_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->list_team_members_api_team_members_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiAuthModelsListResponse**](ApiAuthModelsListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_team_member_api_team_members_user_id_delete**
> Message remove_team_member_api_team_members_user_id_delete(user_id)

Remove Team Member

Remove a team member from the organization.

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
api_instance = hipai_client.TeamApi(hipai_client.ApiClient(configuration))
user_id = NULL # object | 

try:
    # Remove Team Member
    api_response = api_instance.remove_team_member_api_team_members_user_id_delete(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->remove_team_member_api_team_members_user_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | 

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reset_user_password_api_team_reset_password_user_id_post**
> Message reset_user_password_api_team_reset_password_user_id_post(user_id)

Reset User Password

Reset a team member's password.

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
api_instance = hipai_client.TeamApi(hipai_client.ApiClient(configuration))
user_id = NULL # object | 

try:
    # Reset User Password
    api_response = api_instance.reset_user_password_api_team_reset_password_user_id_post(user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->reset_user_password_api_team_reset_password_user_id_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | [**object**](.md)|  | 

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_team_member_api_team_members_upsert_post**
> UserPublic upsert_team_member_api_team_members_upsert_post(body)

Upsert Team Member

Creates a new user or update an existing user

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
api_instance = hipai_client.TeamApi(hipai_client.ApiClient(configuration))
body = hipai_client.UserPublic() # UserPublic | 

try:
    # Upsert Team Member
    api_response = api_instance.upsert_team_member_api_team_members_upsert_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamApi->upsert_team_member_api_team_members_upsert_post: %s\n" % e)
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

