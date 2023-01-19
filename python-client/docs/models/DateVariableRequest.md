# asana.model.date_variable_request.DateVariableRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**gid** | str,  | str,  | Globally unique identifier of the date field in the project template. A value of &#x60;1&#x60; refers to the project start date, while &#x60;2&#x60; refers to the project due date. | [optional] 
**value** | None, str, datetime,  | NoneClass, str,  | The date with which the date variable should be replaced when instantiating a project. This takes a date with &#x60;YYYY-MM-DD&#x60; format. | [optional] value must conform to RFC-3339 date-time
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

