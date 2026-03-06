# hipai_client.ProjectsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_project_api_projects_id_delete**](ProjectsApi.md#delete_project_api_projects_id_delete) | **DELETE** /api/projects/{id} | Delete Project
[**get_user_permissions_api_projects_user_permissions_get**](ProjectsApi.md#get_user_permissions_api_projects_user_permissions_get) | **GET** /api/projects/user-permissions | Get User Permissions
[**list_project_permissions_api_projects_permissions_id_get**](ProjectsApi.md#list_project_permissions_api_projects_permissions_id_get) | **GET** /api/projects/permissions/{id} | List Project Permissions
[**list_projects_api_projects_get**](ProjectsApi.md#list_projects_api_projects_get) | **GET** /api/projects/ | List Projects
[**upsert_project_api_projects_post**](ProjectsApi.md#upsert_project_api_projects_post) | **POST** /api/projects/ | Upsert Project
[**upsert_project_permission_api_projects_permissions_post**](ProjectsApi.md#upsert_project_permission_api_projects_permissions_post) | **POST** /api/projects/permissions | Upsert Project Permission

# **delete_project_api_projects_id_delete**
> Message delete_project_api_projects_id_delete(id)

Delete Project

Deletes a Project. Admin only.

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
api_instance = hipai_client.ProjectsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Delete Project
    api_response = api_instance.delete_project_api_projects_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->delete_project_api_projects_id_delete: %s\n" % e)
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

# **get_user_permissions_api_projects_user_permissions_get**
> object get_user_permissions_api_projects_user_permissions_get()

Get User Permissions

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
api_instance = hipai_client.ProjectsApi(hipai_client.ApiClient(configuration))

try:
    # Get User Permissions
    api_response = api_instance.get_user_permissions_api_projects_user_permissions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->get_user_permissions_api_projects_user_permissions_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_project_permissions_api_projects_permissions_id_get**
> UserPermissionsListResponse list_project_permissions_api_projects_permissions_id_get(id)

List Project Permissions

Lists all company users with their resolved access level per project. Admin only.  Users with admin/superadmin permission_group always have full access (is_admin=True) and their discrete project permissions are not editable.  Access levels: - \"edit\"  → user has read + write + delete permissions (or is admin) - \"read\"  → user has only read permission

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
api_instance = hipai_client.ProjectsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 

try:
    # List Project Permissions
    api_response = api_instance.list_project_permissions_api_projects_permissions_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->list_project_permissions_api_projects_permissions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**UserPermissionsListResponse**](UserPermissionsListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_projects_api_projects_get**
> ApiProjectsModelsListResponse list_projects_api_projects_get()

List Projects

Lists all Projects under the current company. Admin only.

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
api_instance = hipai_client.ProjectsApi(hipai_client.ApiClient(configuration))

try:
    # List Projects
    api_response = api_instance.list_projects_api_projects_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->list_projects_api_projects_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiProjectsModelsListResponse**](ApiProjectsModelsListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_project_api_projects_post**
> ProjectObject upsert_project_api_projects_post(body)

Upsert Project

Creates or updates a Project. Admin only.

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
api_instance = hipai_client.ProjectsApi(hipai_client.ApiClient(configuration))
body = hipai_client.ProjectObject() # ProjectObject | 

try:
    # Upsert Project
    api_response = api_instance.upsert_project_api_projects_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->upsert_project_api_projects_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectObject**](ProjectObject.md)|  | 

### Return type

[**ProjectObject**](ProjectObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_project_permission_api_projects_permissions_post**
> UserPermissionsEntry upsert_project_permission_api_projects_permissions_post(body)

Upsert Project Permission

Sets a user's access level for a project. Admin only.  - \"edit\"  → creates read, write, and delete permissions (idempotent) - \"read\"  → creates read permission, removes write and delete - null    → removes all permissions for this user/project  Raises 403 if the target user is an admin (their access is implicit and not editable).

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
api_instance = hipai_client.ProjectsApi(hipai_client.ApiClient(configuration))
body = hipai_client.ProjectPermissionUpsert() # ProjectPermissionUpsert | 

try:
    # Upsert Project Permission
    api_response = api_instance.upsert_project_permission_api_projects_permissions_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProjectsApi->upsert_project_permission_api_projects_permissions_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ProjectPermissionUpsert**](ProjectPermissionUpsert.md)|  | 

### Return type

[**UserPermissionsEntry**](UserPermissionsEntry.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

