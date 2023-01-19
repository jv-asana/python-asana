# asana.model.goal_metric_base.GoalMetricBase

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[AsanaResource](AsanaResource.md) | [**AsanaResource**](AsanaResource.md) | [**AsanaResource**](AsanaResource.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**resource_subtype** | str,  | str,  | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] must be one of ["number", ] 
**precision** | decimal.Decimal, int,  | decimal.Decimal,  | *Conditional*. Only relevant for goal metrics of type ‘Number’. This field dictates the number of places after the decimal to round to, i.e. 0 is integer values, 1 rounds to the nearest tenth, and so on. Must be between 0 and 6, inclusive. For percentage format, this may be unintuitive, as a value of 0.25 has a precision of 0, while a value of 0.251 has a precision of 1. This is due to 0.25 being displayed as 25%. | [optional] 
**unit** | str,  | str,  | A supported unit of measure for the goal metric, or none. | [optional] must be one of ["none", "currency", "percentage", ] 
**currency_code** | None, str,  | NoneClass, str,  | ISO 4217 currency code to format this custom field. This will be null if the &#x60;unit&#x60; is not &#x60;currency&#x60;. | [optional] 
**initial_number_value** | decimal.Decimal, int, float,  | decimal.Decimal,  | This number is the start value of a goal metric of type number. | [optional] 
**target_number_value** | decimal.Decimal, int, float,  | decimal.Decimal,  | This number is the end value of a goal metric of type number. This number cannot equal &#x60;initial_number_value&#x60;. | [optional] 
**current_number_value** | decimal.Decimal, int, float,  | decimal.Decimal,  | This number is the current value of a goal metric of type number. | [optional] 
**current_display_value** | str,  | str,  | This string is the current value of a goal metric of type string. | [optional] 
**progress_source** | str,  | str,  | This field defines how the progress value of a goal metric is being calculated. A goal&#x27;s progress can be provided manually by the user, calculated automatically from contributing subgoals or projects, or managed by an integration with an external data source, such as Salesforce. | [optional] must be one of ["manual", "subgoal_progress", "project_task_completion", "project_milestone_completion", "external", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

