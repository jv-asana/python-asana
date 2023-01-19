# asana.model.workspace_membership_response.WorkspaceMembershipResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[WorkspaceMembershipCompact](WorkspaceMembershipCompact.md) | [**WorkspaceMembershipCompact**](WorkspaceMembershipCompact.md) | [**WorkspaceMembershipCompact**](WorkspaceMembershipCompact.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**user_task_list** | [**UserTaskListCompact**](UserTaskListCompact.md) | [**UserTaskListCompact**](UserTaskListCompact.md) |  | [optional] 
**is_active** | bool,  | BoolClass,  | Reflects if this user still a member of the workspace. | [optional] 
**is_admin** | bool,  | BoolClass,  | Reflects if this user is an admin of the workspace. | [optional] 
**is_guest** | bool,  | BoolClass,  | Reflects if this user is a guest of the workspace. | [optional] 
**[vacation_dates](#vacation_dates)** | dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Contains keys &#x60;start_on&#x60; and &#x60;end_on&#x60; for the vacation dates for the user in this workspace. If &#x60;start_on&#x60; is null, the entire &#x60;vacation_dates&#x60; object will be null. If &#x60;end_on&#x60; is before today, the entire &#x60;vacation_dates&#x60; object will be null. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# vacation_dates

Contains keys `start_on` and `end_on` for the vacation dates for the user in this workspace. If `start_on` is null, the entire `vacation_dates` object will be null. If `end_on` is before today, the entire `vacation_dates` object will be null.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Contains keys &#x60;start_on&#x60; and &#x60;end_on&#x60; for the vacation dates for the user in this workspace. If &#x60;start_on&#x60; is null, the entire &#x60;vacation_dates&#x60; object will be null. If &#x60;end_on&#x60; is before today, the entire &#x60;vacation_dates&#x60; object will be null. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**start_on** | str,  | str,  | The day on which the user&#x27;s vacation in this workspace starts. This is a date with &#x60;YYYY-MM-DD&#x60; format. | [optional] 
**end_on** | None, str,  | NoneClass, str,  | The day on which the user&#x27;s vacation in this workspace ends, or null if there is no end date. This is a date with &#x60;YYYY-MM-DD&#x60; format. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

