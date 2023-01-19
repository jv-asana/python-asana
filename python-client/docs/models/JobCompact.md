# asana.model.job_compact.JobCompact

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[AsanaResource](AsanaResource.md) | [**AsanaResource**](AsanaResource.md) | [**AsanaResource**](AsanaResource.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  | A *job* is an object representing a process that handles asynchronous work. | 

# all_of_1

A *job* is an object representing a process that handles asynchronous work.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A *job* is an object representing a process that handles asynchronous work. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**resource_subtype** | str,  | str,  | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] 
**status** | str,  | str,  | The current status of this job. The value is one of: &#x60;not_started&#x60;, &#x60;in_progress&#x60;, &#x60;succeeded&#x60;, or &#x60;failed&#x60;. | [optional] must be one of ["not_started", "in_progress", "succeeded", "failed", ] 
**new_project** | [**ProjectCompact**](ProjectCompact.md) | [**ProjectCompact**](ProjectCompact.md) |  | [optional] 
**new_task** | [**TaskCompact**](TaskCompact.md) | [**TaskCompact**](TaskCompact.md) |  | [optional] 
**new_project_template** | [**ProjectTemplateCompact**](ProjectTemplateCompact.md) | [**ProjectTemplateCompact**](ProjectTemplateCompact.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

