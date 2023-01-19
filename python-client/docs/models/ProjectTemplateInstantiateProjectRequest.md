# asana.model.project_template_instantiate_project_request.ProjectTemplateInstantiateProjectRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**public** | bool,  | BoolClass,  | Sets the project to public to its team. | 
**name** | str,  | str,  | The name of the new project. | 
**team** | str,  | str,  | *Conditional*. Sets the team of the new project. If the project template exists in an _organization_, you must specify a value for &#x60;team&#x60; and not &#x60;workspace&#x60;. | [optional] 
**workspace** | str,  | str,  | *Conditional*. Sets the workspace of the new project. If the project template exists in a _workspace_, you must specify a value for &#x60;workspace&#x60; and not &#x60;team&#x60;. | [optional] 
**is_strict** | bool,  | BoolClass,  | *Optional*. If set to &#x60;true&#x60;, the endpoint returns an \&quot;Unprocessable Entity\&quot; error if you fail to provide a calendar date value for any date variable. If set to &#x60;false&#x60;, a default date is used for each unfulfilled date variable (e.g., the current date is used as the Start Date of a project). | [optional] 
**[requested_dates](#requested_dates)** | list, tuple,  | tuple,  | Array of mappings of date variables to calendar dates. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# requested_dates

Array of mappings of date variables to calendar dates.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of mappings of date variables to calendar dates. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**DateVariableRequest**](DateVariableRequest.md) | [**DateVariableRequest**](DateVariableRequest.md) | [**DateVariableRequest**](DateVariableRequest.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

