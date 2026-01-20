# hipai_client.ConnectionConfigsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_connection_config_api_connection_configs_id_delete**](ConnectionConfigsApi.md#delete_connection_config_api_connection_configs_id_delete) | **DELETE** /api/connection-configs/{id} | Delete Connection Config
[**delete_document_api_connection_configs_documents_id_delete**](ConnectionConfigsApi.md#delete_document_api_connection_configs_documents_id_delete) | **DELETE** /api/connection-configs/documents/{id} | Delete Document
[**delete_many_connection_configs_api_connection_configs_delete_many_post**](ConnectionConfigsApi.md#delete_many_connection_configs_api_connection_configs_delete_many_post) | **POST** /api/connection-configs/delete_many | Delete Many Connection Configs
[**document_upload_api_connection_configs_document_upload_post**](ConnectionConfigsApi.md#document_upload_api_connection_configs_document_upload_post) | **POST** /api/connection-configs/document-upload | Document Upload
[**list_connection_configs_api_connection_configs_list_post**](ConnectionConfigsApi.md#list_connection_configs_api_connection_configs_list_post) | **POST** /api/connection-configs/list | List Connection Configs
[**list_documents_api_connection_configs_documents_id_get**](ConnectionConfigsApi.md#list_documents_api_connection_configs_documents_id_get) | **GET** /api/connection-configs/documents/{id} | List Documents
[**load_connection_config_api_connection_configs_id_get**](ConnectionConfigsApi.md#load_connection_config_api_connection_configs_id_get) | **GET** /api/connection-configs/{id} | Load Connection Config
[**upsert_connection_config_api_connection_configs_post**](ConnectionConfigsApi.md#upsert_connection_config_api_connection_configs_post) | **POST** /api/connection-configs/ | Upsert Connection Config

# **delete_connection_config_api_connection_configs_id_delete**
> Message delete_connection_config_api_connection_configs_id_delete(id)

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

try:
    # Delete Connection Config
    api_response = api_instance.delete_connection_config_api_connection_configs_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->delete_connection_config_api_connection_configs_id_delete: %s\n" % e)
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

# **delete_document_api_connection_configs_documents_id_delete**
> Message delete_document_api_connection_configs_documents_id_delete(id)

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

try:
    # Delete Document
    api_response = api_instance.delete_document_api_connection_configs_documents_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->delete_document_api_connection_configs_documents_id_delete: %s\n" % e)
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
> DocumentListResponse list_documents_api_connection_configs_documents_id_get(id)

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

try:
    # List Documents
    api_response = api_instance.list_documents_api_connection_configs_documents_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->list_documents_api_connection_configs_documents_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**DocumentListResponse**](DocumentListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **load_connection_config_api_connection_configs_id_get**
> ConnectionConfigObject load_connection_config_api_connection_configs_id_get(id)

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

try:
    # Load Connection Config
    api_response = api_instance.load_connection_config_api_connection_configs_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectionConfigsApi->load_connection_config_api_connection_configs_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**ConnectionConfigObject**](ConnectionConfigObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
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

