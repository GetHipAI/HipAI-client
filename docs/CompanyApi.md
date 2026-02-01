# hipai_client.CompanyApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_company_api_company_get**](CompanyApi.md#get_company_api_company_get) | **GET** /api/company/ | Get Company
[**get_limits_api_company_limits_get**](CompanyApi.md#get_limits_api_company_limits_get) | **GET** /api/company/limits | Get Limits

# **get_company_api_company_get**
> CompanyObject get_company_api_company_get()

Get Company

Gets the Current User's company

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
api_instance = hipai_client.CompanyApi(hipai_client.ApiClient(configuration))

try:
    # Get Company
    api_response = api_instance.get_company_api_company_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_company_api_company_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CompanyObject**](CompanyObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_limits_api_company_limits_get**
> LimitObject get_limits_api_company_limits_get()

Get Limits

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
api_instance = hipai_client.CompanyApi(hipai_client.ApiClient(configuration))

try:
    # Get Limits
    api_response = api_instance.get_limits_api_company_limits_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->get_limits_api_company_limits_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**LimitObject**](LimitObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

