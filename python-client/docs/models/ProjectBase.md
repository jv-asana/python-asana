# asana.model.project_base.ProjectBase

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ProjectCompact](ProjectCompact.md) | [**ProjectCompact**](ProjectCompact.md) | [**ProjectCompact**](ProjectCompact.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**archived** | bool,  | BoolClass,  | True if the project is archived, false if not. Archived projects do not show in the UI by default and may be treated differently for queries. | [optional] 
**color** | None, str,  | NoneClass, str,  | Color of the project. | [optional] must be one of ["dark-pink", "dark-green", "dark-blue", "dark-red", "dark-teal", "dark-brown", "dark-orange", "dark-purple", "dark-warm-gray", "light-pink", "light-green", "light-blue", "light-red", "light-teal", "light-brown", "light-orange", "light-purple", "light-warm-gray", ] 
**created_at** | str, datetime,  | str,  | The time at which this resource was created. | [optional] value must conform to RFC-3339 date-time
**[current_status](#current_status)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | *Deprecated: new integrations should prefer the &#x60;current_status_update&#x60; resource.* | [optional] 
**[current_status_update](#current_status_update)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The latest &#x60;status_update&#x60; posted to this project. | [optional] 
**[custom_field_settings](#custom_field_settings)** | list, tuple,  | tuple,  | Array of Custom Field Settings (in compact form). | [optional] 
**default_view** | str,  | str,  | The default view (list, board, calendar, or timeline) of a project. | [optional] must be one of ["list", "board", "calendar", "timeline", ] 
**due_date** | None, str, datetime,  | NoneClass, str,  | *Deprecated: new integrations should prefer the &#x60;due_on&#x60; field.* | [optional] value must conform to RFC-3339 date-time
**due_on** | None, str, datetime,  | NoneClass, str,  | The day on which this project is due. This takes a date with format YYYY-MM-DD. | [optional] value must conform to RFC-3339 date-time
**html_notes** | str,  | str,  | [Opt In](/docs/input-output-options). The notes of the project with formatting as HTML. | [optional] 
**is_template** | bool,  | BoolClass,  | [Opt In](/docs/input-output-options). *Deprecated - please use a project template endpoint instead (more in [this forum post](https://forum.asana.com/t/a-new-api-for-project-templates/156432)).* Determines if the project is a template. | [optional] 
**[members](#members)** | list, tuple,  | tuple,  | Array of users who are members of this project. | [optional] 
**modified_at** | str, datetime,  | str,  | The time at which this project was last modified. *Note: This does not currently reflect any changes in associations such as tasks or comments that may have been added or removed from the project.* | [optional] value must conform to RFC-3339 date-time
**notes** | str,  | str,  | Free-form textual information associated with the project (ie., its description). | [optional] 
**public** | bool,  | BoolClass,  | True if the project is public to its team. | [optional] 
**start_on** | None, str, date,  | NoneClass, str,  | The day on which work for this project begins, or null if the project has no start date. This takes a date with &#x60;YYYY-MM-DD&#x60; format. *Note: &#x60;due_on&#x60; or &#x60;due_at&#x60; must be present in the request when setting or unsetting the &#x60;start_on&#x60; parameter. Additionally, &#x60;start_on&#x60; and &#x60;due_on&#x60; cannot be the same date.* | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**[workspace](#workspace)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# current_status

*Deprecated: new integrations should prefer the `current_status_update` resource.*

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | *Deprecated: new integrations should prefer the &#x60;current_status_update&#x60; resource.* | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ProjectStatusResponse](ProjectStatusResponse.md) | [**ProjectStatusResponse**](ProjectStatusResponse.md) | [**ProjectStatusResponse**](ProjectStatusResponse.md) |  | 

# current_status_update

The latest `status_update` posted to this project.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The latest &#x60;status_update&#x60; posted to this project. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[StatusUpdateCompact](StatusUpdateCompact.md) | [**StatusUpdateCompact**](StatusUpdateCompact.md) | [**StatusUpdateCompact**](StatusUpdateCompact.md) |  | 

# custom_field_settings

Array of Custom Field Settings (in compact form).

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of Custom Field Settings (in compact form). | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CustomFieldSettingResponse**](CustomFieldSettingResponse.md) | [**CustomFieldSettingResponse**](CustomFieldSettingResponse.md) | [**CustomFieldSettingResponse**](CustomFieldSettingResponse.md) |  | 

# members

Array of users who are members of this project.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of users who are members of this project. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UserCompact**](UserCompact.md) | [**UserCompact**](UserCompact.md) | [**UserCompact**](UserCompact.md) |  | 

# workspace

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[WorkspaceCompact](WorkspaceCompact.md) | [**WorkspaceCompact**](WorkspaceCompact.md) | [**WorkspaceCompact**](WorkspaceCompact.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  | *Create-only*. The workspace or organization this project is associated with. Once created, projects cannot be moved to a different workspace. This attribute can only be specified at creation time. | 

# all_of_1

*Create-only*. The workspace or organization this project is associated with. Once created, projects cannot be moved to a different workspace. This attribute can only be specified at creation time.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | *Create-only*. The workspace or organization this project is associated with. Once created, projects cannot be moved to a different workspace. This attribute can only be specified at creation time. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

