# hipai_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**ping_ping_get**](DefaultApi.md#ping_ping_get) | **GET** /ping | Ping

# **ping_ping_get**
> object ping_ping_get()

Ping

### Example
```python
from __future__ import print_function
import time
import hipai_client
from hipai_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hipai_client.DefaultApi()

try:
    # Ping
    api_response = api_instance.ping_ping_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->ping_ping_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

