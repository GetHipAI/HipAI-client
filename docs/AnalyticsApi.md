# hipai_client.AnalyticsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**analytics_query_api_analytics_post**](AnalyticsApi.md#analytics_query_api_analytics_post) | **POST** /api/analytics/ | Analytics Query

# **analytics_query_api_analytics_post**
> AnalyticsResponse analytics_query_api_analytics_post(body)

Analytics Query

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
api_instance = hipai_client.AnalyticsApi(hipai_client.ApiClient(configuration))
body = hipai_client.AnalyticsQuery() # AnalyticsQuery | 

try:
    # Analytics Query
    api_response = api_instance.analytics_query_api_analytics_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AnalyticsApi->analytics_query_api_analytics_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AnalyticsQuery**](AnalyticsQuery.md)|  | 

### Return type

[**AnalyticsResponse**](AnalyticsResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

