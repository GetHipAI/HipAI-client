# hipai_client.EvaluationsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_evaluation_api_evaluations_id_delete**](EvaluationsApi.md#delete_evaluation_api_evaluations_id_delete) | **DELETE** /api/evaluations/{id} | Delete Evaluation
[**delete_question_api_evaluations_questions_id_delete**](EvaluationsApi.md#delete_question_api_evaluations_questions_id_delete) | **DELETE** /api/evaluations/questions/{id} | Delete Question
[**list_evaluations_api_evaluations_list_get**](EvaluationsApi.md#list_evaluations_api_evaluations_list_get) | **GET** /api/evaluations/list | List Evaluations
[**list_questions_api_evaluations_questions_id_get**](EvaluationsApi.md#list_questions_api_evaluations_questions_id_get) | **GET** /api/evaluations/questions/{id} | List Questions
[**list_responses_api_evaluations_responses_id_get**](EvaluationsApi.md#list_responses_api_evaluations_responses_id_get) | **GET** /api/evaluations/responses/{id} | List Responses
[**list_runs_api_evaluations_runs_get**](EvaluationsApi.md#list_runs_api_evaluations_runs_get) | **GET** /api/evaluations/runs | List Runs
[**run_evaluation_api_evaluations_run_post**](EvaluationsApi.md#run_evaluation_api_evaluations_run_post) | **POST** /api/evaluations/run | Run Evaluation
[**upsert_evaluation_api_evaluations_post**](EvaluationsApi.md#upsert_evaluation_api_evaluations_post) | **POST** /api/evaluations/ | Upsert Evaluation
[**upsert_question_api_evaluations_question_post**](EvaluationsApi.md#upsert_question_api_evaluations_question_post) | **POST** /api/evaluations/question | Upsert Question

# **delete_evaluation_api_evaluations_id_delete**
> Message delete_evaluation_api_evaluations_id_delete(id)

Delete Evaluation

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
api_instance = hipai_client.EvaluationsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Delete Evaluation
    api_response = api_instance.delete_evaluation_api_evaluations_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationsApi->delete_evaluation_api_evaluations_id_delete: %s\n" % e)
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

# **delete_question_api_evaluations_questions_id_delete**
> Message delete_question_api_evaluations_questions_id_delete(id)

Delete Question

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
api_instance = hipai_client.EvaluationsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 

try:
    # Delete Question
    api_response = api_instance.delete_question_api_evaluations_questions_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationsApi->delete_question_api_evaluations_questions_id_delete: %s\n" % e)
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

# **list_evaluations_api_evaluations_list_get**
> ApiEvaluationsModelsListResponse list_evaluations_api_evaluations_list_get()

List Evaluations

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
api_instance = hipai_client.EvaluationsApi(hipai_client.ApiClient(configuration))

try:
    # List Evaluations
    api_response = api_instance.list_evaluations_api_evaluations_list_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationsApi->list_evaluations_api_evaluations_list_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiEvaluationsModelsListResponse**](ApiEvaluationsModelsListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_questions_api_evaluations_questions_id_get**
> ApiEvaluationsModelsListResponse list_questions_api_evaluations_questions_id_get(id)

List Questions

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
api_instance = hipai_client.EvaluationsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 

try:
    # List Questions
    api_response = api_instance.list_questions_api_evaluations_questions_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationsApi->list_questions_api_evaluations_questions_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**ApiEvaluationsModelsListResponse**](ApiEvaluationsModelsListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_responses_api_evaluations_responses_id_get**
> ApiEvaluationsModelsListResponse list_responses_api_evaluations_responses_id_get(id)

List Responses

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
api_instance = hipai_client.EvaluationsApi(hipai_client.ApiClient(configuration))
id = NULL # object | 

try:
    # List Responses
    api_response = api_instance.list_responses_api_evaluations_responses_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationsApi->list_responses_api_evaluations_responses_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**object**](.md)|  | 

### Return type

[**ApiEvaluationsModelsListResponse**](ApiEvaluationsModelsListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_runs_api_evaluations_runs_get**
> ApiEvaluationsModelsListResponse list_runs_api_evaluations_runs_get()

List Runs

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
api_instance = hipai_client.EvaluationsApi(hipai_client.ApiClient(configuration))

try:
    # List Runs
    api_response = api_instance.list_runs_api_evaluations_runs_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationsApi->list_runs_api_evaluations_runs_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ApiEvaluationsModelsListResponse**](ApiEvaluationsModelsListResponse.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **run_evaluation_api_evaluations_run_post**
> EvaluationRunObject run_evaluation_api_evaluations_run_post(body)

Run Evaluation

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
api_instance = hipai_client.EvaluationsApi(hipai_client.ApiClient(configuration))
body = hipai_client.EvaluationRunObject() # EvaluationRunObject | 

try:
    # Run Evaluation
    api_response = api_instance.run_evaluation_api_evaluations_run_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationsApi->run_evaluation_api_evaluations_run_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EvaluationRunObject**](EvaluationRunObject.md)|  | 

### Return type

[**EvaluationRunObject**](EvaluationRunObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_evaluation_api_evaluations_post**
> EvaluationObject upsert_evaluation_api_evaluations_post(body)

Upsert Evaluation

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
api_instance = hipai_client.EvaluationsApi(hipai_client.ApiClient(configuration))
body = hipai_client.EvaluationUpsert() # EvaluationUpsert | 

try:
    # Upsert Evaluation
    api_response = api_instance.upsert_evaluation_api_evaluations_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationsApi->upsert_evaluation_api_evaluations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EvaluationUpsert**](EvaluationUpsert.md)|  | 

### Return type

[**EvaluationObject**](EvaluationObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_question_api_evaluations_question_post**
> QuestionObject upsert_question_api_evaluations_question_post(body)

Upsert Question

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
api_instance = hipai_client.EvaluationsApi(hipai_client.ApiClient(configuration))
body = hipai_client.QuestionObject() # QuestionObject | 

try:
    # Upsert Question
    api_response = api_instance.upsert_question_api_evaluations_question_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EvaluationsApi->upsert_question_api_evaluations_question_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QuestionObject**](QuestionObject.md)|  | 

### Return type

[**QuestionObject**](QuestionObject.md)

### Authorization

[OAuth2PasswordBearer](../README.md#OAuth2PasswordBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

