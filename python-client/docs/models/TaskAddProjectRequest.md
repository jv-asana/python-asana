# asana.model.task_add_project_request.TaskAddProjectRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**project** | str,  | str,  | The project to add the task to. | 
**insert_after** | None, str,  | NoneClass, str,  | A task in the project to insert the task after, or &#x60;null&#x60; to insert at the beginning of the list. | [optional] 
**insert_before** | None, str,  | NoneClass, str,  | A task in the project to insert the task before, or &#x60;null&#x60; to insert at the end of the list. | [optional] 
**section** | None, str,  | NoneClass, str,  | A section in the project to insert the task into. The task will be inserted at the bottom of the section. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

