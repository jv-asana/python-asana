# asana.model.project_duplicate_request.ProjectDuplicateRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the new project. | 
**team** | str,  | str,  | Sets the team of the new project. If team is not defined, the new project will be in the same team as the the original project. | [optional] 
**include** | str,  | str,  | The elements that will be duplicated to the new project. Tasks are always included. | [optional] must be one of ["members", "notes", "forms", "task_notes", "task_assignee", "task_subtasks", "task_attachments", "task_dates", "task_dependencies", "task_followers", "task_tags", "task_projects", ] 
**[schedule_dates](#schedule_dates)** | dict, frozendict.frozendict,  | frozendict.frozendict,  | A dictionary of options to auto-shift dates. &#x60;task_dates&#x60; must be included to use this option. Requires either &#x60;start_on&#x60; or &#x60;due_on&#x60;, but not both. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# schedule_dates

A dictionary of options to auto-shift dates. `task_dates` must be included to use this option. Requires either `start_on` or `due_on`, but not both.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A dictionary of options to auto-shift dates. &#x60;task_dates&#x60; must be included to use this option. Requires either &#x60;start_on&#x60; or &#x60;due_on&#x60;, but not both. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**should_skip_weekends** | bool,  | BoolClass,  | Determines if the auto-shifted dates should skip weekends. | 
**due_on** | str,  | str,  | Sets the last due date in the duplicated project to the given date. The rest of the due dates will be offset by the same amount as the due dates in the original project. | [optional] 
**start_on** | str,  | str,  | Sets the first start date in the duplicated project to the given date. The rest of the start dates will be offset by the same amount as the start dates in the original project. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

