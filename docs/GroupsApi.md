# hipai_client.GroupsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_group_api_groups_id_delete**](GroupsApi.md#delete_group_api_groups_id_delete) | **DELETE** /api/groups/{id} | Delete Group
[**list_groups_api_groups_list_get**](GroupsApi.md#list_groups_api_groups_list_get) | **GET** /api/groups/list | List Groups
[**upsert_group_api_groups_post**](GroupsApi.md#upsert_group_api_groups_post) | **POST** /api/groups/ | Upsert Group

# **delete_group_api_groups_id_delete**
> Message delete_group_api_groups_id_delete(id)

Delete Group

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
api_instance = hipai_client.GroupsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Delete Group
    api_response = api_instance.delete_group_api_groups_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->delete_group_api_groups_id_delete: %s\n" % e)
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

# **list_groups_api_groups_list_get**
> ApiGroupsModelsListResponse list_groups_api_groups_list_get()

List Groups

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
api_instance = hipai_client.GroupsApi(hipai_client.ApiClient(configuration))

try:
    # List Groups
    api_response = api_instance.list_groups_api_groups_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->list_groups_api_groups_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiGroupsModelsListResponse**](ApiGroupsModelsListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_group_api_groups_post**
> GroupIsolationObject upsert_group_api_groups_post(body)

Upsert Group

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
api_instance = hipai_client.GroupsApi(hipai_client.ApiClient(configuration))
body = hipai_client.GroupIsolationObject() # GroupIsolationObject | 

try:
    # Upsert Group
    api_response = api_instance.upsert_group_api_groups_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GroupsApi->upsert_group_api_groups_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GroupIsolationObject**](GroupIsolationObject.md)|  | 

### Return type

[**GroupIsolationObject**](GroupIsolationObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

