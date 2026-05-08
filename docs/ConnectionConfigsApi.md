# hipai_client.ConnectionConfigsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_connection_config_api_connection_configs_id_delete**](ConnectionConfigsApi.md#delete_connection_config_api_connection_configs_id_delete) | **DELETE** /api/connection-configs/{id} | Delete Connection Config
[**delete_document_api_connection_configs_documents_id_delete**](ConnectionConfigsApi.md#delete_document_api_connection_configs_documents_id_delete) | **DELETE** /api/connection-configs/documents/{id} | Delete Document
[**delete_many_connection_configs_api_connection_configs_delete_many_post**](ConnectionConfigsApi.md#delete_many_connection_configs_api_connection_configs_delete_many_post) | **POST** /api/connection-configs/delete_many | Delete Many Connection Configs
[**document_upload_api_connection_configs_document_upload_post**](ConnectionConfigsApi.md#document_upload_api_connection_configs_document_upload_post) | **POST** /api/connection-configs/document-upload | Document Upload
[**gdrive_auth_url_api_connection_configs_gdrive_auth_url_get**](ConnectionConfigsApi.md#gdrive_auth_url_api_connection_configs_gdrive_auth_url_get) | **GET** /api/connection-configs/gdrive/auth-url | Gdrive Auth Url
[**gdrive_exchange_api_connection_configs_gdrive_exchange_post**](ConnectionConfigsApi.md#gdrive_exchange_api_connection_configs_gdrive_exchange_post) | **POST** /api/connection-configs/gdrive/exchange | Gdrive Exchange
[**gdrive_picker_token_api_connection_configs_gdrive_picker_token_get**](ConnectionConfigsApi.md#gdrive_picker_token_api_connection_configs_gdrive_picker_token_get) | **GET** /api/connection-configs/gdrive/picker-token | Gdrive Picker Token
[**list_connection_configs_api_connection_configs_list_post**](ConnectionConfigsApi.md#list_connection_configs_api_connection_configs_list_post) | **POST** /api/connection-configs/list | List Connection Configs
[**list_documents_api_connection_configs_documents_id_get**](ConnectionConfigsApi.md#list_documents_api_connection_configs_documents_id_get) | **GET** /api/connection-configs/documents/{id} | List Documents
[**list_remote_files_api_connection_configs_remote_files_post**](ConnectionConfigsApi.md#list_remote_files_api_connection_configs_remote_files_post) | **POST** /api/connection-configs/remote-files | List Remote Files
[**load_connection_config_api_connection_configs_id_get**](ConnectionConfigsApi.md#load_connection_config_api_connection_configs_id_get) | **GET** /api/connection-configs/{id} | Load Connection Config
[**test_connection_api_connection_configs_test_connection_post**](ConnectionConfigsApi.md#test_connection_api_connection_configs_test_connection_post) | **POST** /api/connection-configs/test-connection | Test Connection
[**upsert_connection_config_api_connection_configs_post**](ConnectionConfigsApi.md#upsert_connection_config_api_connection_configs_post) | **POST** /api/connection-configs/ | Upsert Connection Config

# **delete_connection_config_api_connection_configs_id_delete**
> Message delete_connection_config_api_connection_configs_id_delete(id, project_id=project_id)

Delete Connection Config

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
api_instance = hipai_client.ConnectionConfigsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 
project_id = NULL # object |  (optional)

try:
    # Delete Connection Config
    api_response = api_instance.delete_connection_config_api_connection_configs_id_delete(id, project_id=project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->delete_connection_config_api_connection_configs_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **project_id** | [**object**](.md)|  | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_document_api_connection_configs_documents_id_delete**
> Message delete_document_api_connection_configs_documents_id_delete(id, project_id=project_id)

Delete Document

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
api_instance = hipai_client.ConnectionConfigsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 
project_id = NULL # object |  (optional)

try:
    # Delete Document
    api_response = api_instance.delete_document_api_connection_configs_documents_id_delete(id, project_id=project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->delete_document_api_connection_configs_documents_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **project_id** | [**object**](.md)|  | [optional] 

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_many_connection_configs_api_connection_configs_delete_many_post**
> Message delete_many_connection_configs_api_connection_configs_delete_many_post(body)

Delete Many Connection Configs

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
api_instance = hipai_client.ConnectionConfigsApi(hipai_client.ApiClient(configuration))
body = hipai_client.ApiConnectionConfigsModelsListRequest() # ApiConnectionConfigsModelsListRequest | 

try:
    # Delete Many Connection Configs
    api_response = api_instance.delete_many_connection_configs_api_connection_configs_delete_many_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->delete_many_connection_configs_api_connection_configs_delete_many_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiConnectionConfigsModelsListRequest**](ApiConnectionConfigsModelsListRequest.md)|  | 

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_upload_api_connection_configs_document_upload_post**
> ConnectionConfigObject document_upload_api_connection_configs_document_upload_post(request, file)

Document Upload

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
api_instance = hipai_client.ConnectionConfigsApi(hipai_client.ApiClient(configuration))
request = hipai_client.ConnectionConfigObject() # ConnectionConfigObject | 
file = NULL # object | 

try:
    # Document Upload
    api_response = api_instance.document_upload_api_connection_configs_document_upload_post(request, file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->document_upload_api_connection_configs_document_upload_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request** | [**ConnectionConfigObject**](.md)|  | 
 **file** | [**object**](.md)|  | 

### Return type

[**ConnectionConfigObject**](ConnectionConfigObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gdrive_auth_url_api_connection_configs_gdrive_auth_url_get**
> GDriveAuthUrlResponse gdrive_auth_url_api_connection_configs_gdrive_auth_url_get(redirect_uri, state=state)

Gdrive Auth Url

Returns the Google OAuth2 authorization URL. The frontend should redirect the user to this URL. After the user authenticates, Google will redirect back to ``redirect_uri`` with a ``code`` parameter. Pass ``state`` to have it returned unchanged in the callback (e.g. the connection_config_id).

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
api_instance = hipai_client.ConnectionConfigsApi(hipai_client.ApiClient(configuration))
redirect_uri = NULL # object | 
state = NULL # object |  (optional)

try:
    # Gdrive Auth Url
    api_response = api_instance.gdrive_auth_url_api_connection_configs_gdrive_auth_url_get(redirect_uri, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->gdrive_auth_url_api_connection_configs_gdrive_auth_url_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **redirect_uri** | [**object**](.md)|  | 
 **state** | [**object**](.md)|  | [optional] 

### Return type

[**GDriveAuthUrlResponse**](GDriveAuthUrlResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gdrive_exchange_api_connection_configs_gdrive_exchange_post**
> GDriveExchangeResponse gdrive_exchange_api_connection_configs_gdrive_exchange_post(body)

Gdrive Exchange

Exchanges the OAuth2 authorization code for a refresh token and attaches credentials to the specified ConnectionConfig. Call this after the user is redirected back from Google. The connection config is located by company_id + connection_config_id only (no project_id required, since this endpoint is called from an OAuth popup that does not carry project context).

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
api_instance = hipai_client.ConnectionConfigsApi(hipai_client.ApiClient(configuration))
body = hipai_client.GDriveExchangeRequest() # GDriveExchangeRequest | 

try:
    # Gdrive Exchange
    api_response = api_instance.gdrive_exchange_api_connection_configs_gdrive_exchange_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->gdrive_exchange_api_connection_configs_gdrive_exchange_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GDriveExchangeRequest**](GDriveExchangeRequest.md)|  | 

### Return type

[**GDriveExchangeResponse**](GDriveExchangeResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **gdrive_picker_token_api_connection_configs_gdrive_picker_token_get**
> GDrivePickerTokenResponse gdrive_picker_token_api_connection_configs_gdrive_picker_token_get(connection_config_id)

Gdrive Picker Token

Returns a short-lived access token for the authenticated user's Google Drive connection. Used by the frontend to open the Google Drive Folder Picker.

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
api_instance = hipai_client.ConnectionConfigsApi(hipai_client.ApiClient(configuration))
connection_config_id = NULL # object | 

try:
    # Gdrive Picker Token
    api_response = api_instance.gdrive_picker_token_api_connection_configs_gdrive_picker_token_get(connection_config_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->gdrive_picker_token_api_connection_configs_gdrive_picker_token_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connection_config_id** | [**object**](.md)|  | 

### Return type

[**GDrivePickerTokenResponse**](GDrivePickerTokenResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_connection_configs_api_connection_configs_list_post**
> ApiConnectionConfigsModelsListResponse list_connection_configs_api_connection_configs_list_post(body)

List Connection Configs

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
api_instance = hipai_client.ConnectionConfigsApi(hipai_client.ApiClient(configuration))
body = hipai_client.ApiConnectionConfigsModelsListRequest() # ApiConnectionConfigsModelsListRequest | 

try:
    # List Connection Configs
    api_response = api_instance.list_connection_configs_api_connection_configs_list_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->list_connection_configs_api_connection_configs_list_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ApiConnectionConfigsModelsListRequest**](ApiConnectionConfigsModelsListRequest.md)|  | 

### Return type

[**ApiConnectionConfigsModelsListResponse**](ApiConnectionConfigsModelsListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_documents_api_connection_configs_documents_id_get**
> DocumentListResponse list_documents_api_connection_configs_documents_id_get(id, project_id=project_id)

List Documents

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
api_instance = hipai_client.ConnectionConfigsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 
project_id = NULL # object |  (optional)

try:
    # List Documents
    api_response = api_instance.list_documents_api_connection_configs_documents_id_get(id, project_id=project_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->list_documents_api_connection_configs_documents_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **project_id** | [**object**](.md)|  | [optional] 

### Return type

[**DocumentListResponse**](DocumentListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_remote_files_api_connection_configs_remote_files_post**
> RemoteFilesResponse list_remote_files_api_connection_configs_remote_files_post(body)

List Remote Files

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
api_instance = hipai_client.ConnectionConfigsApi(hipai_client.ApiClient(configuration))
body = hipai_client.ConnectionConfigObject() # ConnectionConfigObject | 

try:
    # List Remote Files
    api_response = api_instance.list_remote_files_api_connection_configs_remote_files_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->list_remote_files_api_connection_configs_remote_files_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionConfigObject**](ConnectionConfigObject.md)|  | 

### Return type

[**RemoteFilesResponse**](RemoteFilesResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_connection_config_api_connection_configs_id_get**
> ConnectionConfigObject load_connection_config_api_connection_configs_id_get(id, project_id=project_id, group_id=group_id)

Load Connection Config

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
api_instance = hipai_client.ConnectionConfigsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 
project_id = NULL # object |  (optional)
group_id = NULL # object |  (optional)

try:
    # Load Connection Config
    api_response = api_instance.load_connection_config_api_connection_configs_id_get(id, project_id=project_id, group_id=group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->load_connection_config_api_connection_configs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 
 **project_id** | [**object**](.md)|  | [optional] 
 **group_id** | [**object**](.md)|  | [optional] 

### Return type

[**ConnectionConfigObject**](ConnectionConfigObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_connection_api_connection_configs_test_connection_post**
> Message test_connection_api_connection_configs_test_connection_post(body)

Test Connection

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
api_instance = hipai_client.ConnectionConfigsApi(hipai_client.ApiClient(configuration))
body = hipai_client.ConnectionConfigObject() # ConnectionConfigObject | 

try:
    # Test Connection
    api_response = api_instance.test_connection_api_connection_configs_test_connection_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->test_connection_api_connection_configs_test_connection_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionConfigObject**](ConnectionConfigObject.md)|  | 

### Return type

[**Message**](Message.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_connection_config_api_connection_configs_post**
> ConnectionConfigObject upsert_connection_config_api_connection_configs_post(body)

Upsert Connection Config

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
api_instance = hipai_client.ConnectionConfigsApi(hipai_client.ApiClient(configuration))
body = hipai_client.ConnectionConfigObject() # ConnectionConfigObject | 

try:
    # Upsert Connection Config
    api_response = api_instance.upsert_connection_config_api_connection_configs_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->upsert_connection_config_api_connection_configs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ConnectionConfigObject**](ConnectionConfigObject.md)|  | 

### Return type

[**ConnectionConfigObject**](ConnectionConfigObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

