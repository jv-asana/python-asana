# asana.model.task_count_response.TaskCountResponse

A response object returned from the task count endpoint.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A response object returned from the task count endpoint. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**num_tasks** | decimal.Decimal, int,  | decimal.Decimal,  | The number of tasks in a project. | [optional] 
**num_incomplete_tasks** | decimal.Decimal, int,  | decimal.Decimal,  | The number of incomplete tasks in a project. | [optional] 
**num_completed_tasks** | decimal.Decimal, int,  | decimal.Decimal,  | The number of completed tasks in a project. | [optional] 
**num_milestones** | decimal.Decimal, int,  | decimal.Decimal,  | The number of milestones in a project. | [optional] 
**num_incomplete_milestones** | decimal.Decimal, int,  | decimal.Decimal,  | The number of incomplete milestones in a project. | [optional] 
**num_completed_milestones** | decimal.Decimal, int,  | decimal.Decimal,  | The number of completed milestones in a project. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

