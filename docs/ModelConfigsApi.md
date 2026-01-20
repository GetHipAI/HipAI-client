# hipai_client.ModelConfigsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_model_config_api_model_configs_id_delete**](ModelConfigsApi.md#delete_model_config_api_model_configs_id_delete) | **DELETE** /api/model-configs/{id} | Delete Model Config
[**list_model_configs_api_model_configs_list_get**](ModelConfigsApi.md#list_model_configs_api_model_configs_list_get) | **GET** /api/model-configs/list | List Model Configs
[**upsert_model_config_api_model_configs_post**](ModelConfigsApi.md#upsert_model_config_api_model_configs_post) | **POST** /api/model-configs/ | Upsert Model Config

# **delete_model_config_api_model_configs_id_delete**
> Message delete_model_config_api_model_configs_id_delete(id)

Delete Model Config

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
api_instance = hipai_client.ModelConfigsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Delete Model Config
    api_response = api_instance.delete_model_config_api_model_configs_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigsApi->delete_model_config_api_model_configs_id_delete: %s\n" % e)
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

# **list_model_configs_api_model_configs_list_get**
> ApiModelConfigModelsListResponse list_model_configs_api_model_configs_list_get()

List Model Configs

Endpoint for listing model configurations.

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
api_instance = hipai_client.ModelConfigsApi(hipai_client.ApiClient(configuration))

try:
    # List Model Configs
    api_response = api_instance.list_model_configs_api_model_configs_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigsApi->list_model_configs_api_model_configs_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiModelConfigModelsListResponse**](ApiModelConfigModelsListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_model_config_api_model_configs_post**
> ModelConfigObject upsert_model_config_api_model_configs_post(body)

Upsert Model Config

End point for adding and updating model configuration.

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
api_instance = hipai_client.ModelConfigsApi(hipai_client.ApiClient(configuration))
body = hipai_client.ModelConfigObject() # ModelConfigObject | 

try:
    # Upsert Model Config
    api_response = api_instance.upsert_model_config_api_model_configs_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigsApi->upsert_model_config_api_model_configs_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ModelConfigObject**](ModelConfigObject.md)|  | 

### Return type

[**ModelConfigObject**](ModelConfigObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

