# hipai_client.ModelConfigApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**model_config_list_model_config_list_get**](ModelConfigApi.md#model_config_list_model_config_list_get) | **GET** /model-config/list | Model Config List
[**model_config_upsert_model_config_post**](ModelConfigApi.md#model_config_upsert_model_config_post) | **POST** /model-config/ | Model Config Upsert

# **model_config_list_model_config_list_get**
> ApiModelConfigModelsListResponse model_config_list_model_config_list_get()

Model Config List

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
api_instance = hipai_client.ModelConfigApi(hipai_client.ApiClient(configuration))

try:
    # Model Config List
    api_response = api_instance.model_config_list_model_config_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigApi->model_config_list_model_config_list_get: %s\n" % e)
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

# **model_config_upsert_model_config_post**
> ModelConfigObject model_config_upsert_model_config_post(body)

Model Config Upsert

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
api_instance = hipai_client.ModelConfigApi(hipai_client.ApiClient(configuration))
body = hipai_client.ModelConfigObject() # ModelConfigObject | 

try:
    # Model Config Upsert
    api_response = api_instance.model_config_upsert_model_config_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ModelConfigApi->model_config_upsert_model_config_post: %s\n" % e)
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

