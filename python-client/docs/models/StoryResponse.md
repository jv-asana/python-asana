# asana.model.story_response.StoryResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[StoryBase](StoryBase.md) | [**StoryBase**](StoryBase.md) | [**StoryBase**](StoryBase.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_by** | [**UserCompact**](UserCompact.md) | [**UserCompact**](UserCompact.md) |  | [optional] 
**type** | str,  | str,  |  | [optional] must be one of ["comment", "system", ] 
**is_editable** | bool,  | BoolClass,  | *Conditional*. Whether the text of the story can be edited after creation. | [optional] 
**is_edited** | bool,  | BoolClass,  | *Conditional*. Whether the text of the story has been edited after creation. | [optional] 
**hearted** | bool,  | BoolClass,  | *Deprecated - please use likes instead* *Conditional*. True if the story is hearted by the authorized user, false if not. | [optional] 
**[hearts](#hearts)** | list, tuple,  | tuple,  | *Deprecated - please use likes instead*  *Conditional*. Array of likes for users who have hearted this story. | [optional] 
**num_hearts** | decimal.Decimal, int,  | decimal.Decimal,  | *Deprecated - please use likes instead*  *Conditional*. The number of users who have hearted this story. | [optional] 
**liked** | bool,  | BoolClass,  | *Conditional*. True if the story is liked by the authorized user, false if not. | [optional] 
**[likes](#likes)** | list, tuple,  | tuple,  | *Conditional*. Array of likes for users who have liked this story. | [optional] 
**num_likes** | decimal.Decimal, int,  | decimal.Decimal,  | *Conditional*. The number of users who have liked this story. | [optional] 
**[previews](#previews)** | list, tuple,  | tuple,  | *Conditional*. A collection of previews to be displayed in the story.  *Note: This property only exists for comment stories.* | [optional] 
**old_name** | str,  | str,  | *Conditional*&#x27; | [optional] 
**new_name** | str,  | str,  | *Conditional* | [optional] 
**old_dates** | [**StoryResponseDates**](StoryResponseDates.md) | [**StoryResponseDates**](StoryResponseDates.md) |  | [optional] 
**new_dates** | [**StoryResponseDates**](StoryResponseDates.md) | [**StoryResponseDates**](StoryResponseDates.md) |  | [optional] 
**old_resource_subtype** | str,  | str,  | *Conditional* | [optional] 
**new_resource_subtype** | str,  | str,  | *Conditional* | [optional] 
**story** | [**StoryCompact**](StoryCompact.md) | [**StoryCompact**](StoryCompact.md) |  | [optional] 
**assignee** | [**UserCompact**](UserCompact.md) | [**UserCompact**](UserCompact.md) |  | [optional] 
**follower** | [**UserCompact**](UserCompact.md) | [**UserCompact**](UserCompact.md) |  | [optional] 
**old_section** | [**SectionCompact**](SectionCompact.md) | [**SectionCompact**](SectionCompact.md) |  | [optional] 
**new_section** | [**SectionCompact**](SectionCompact.md) | [**SectionCompact**](SectionCompact.md) |  | [optional] 
**task** | [**TaskCompact**](TaskCompact.md) | [**TaskCompact**](TaskCompact.md) |  | [optional] 
**project** | [**ProjectCompact**](ProjectCompact.md) | [**ProjectCompact**](ProjectCompact.md) |  | [optional] 
**tag** | [**TagCompact**](TagCompact.md) | [**TagCompact**](TagCompact.md) |  | [optional] 
**custom_field** | [**CustomFieldCompact**](CustomFieldCompact.md) | [**CustomFieldCompact**](CustomFieldCompact.md) |  | [optional] 
**old_text_value** | str,  | str,  | *Conditional* | [optional] 
**new_text_value** | str,  | str,  | *Conditional* | [optional] 
**old_number_value** | decimal.Decimal, int,  | decimal.Decimal,  | *Conditional* | [optional] 
**new_number_value** | decimal.Decimal, int,  | decimal.Decimal,  | *Conditional* | [optional] 
**old_enum_value** | [**EnumOption**](EnumOption.md) | [**EnumOption**](EnumOption.md) |  | [optional] 
**new_enum_value** | [**EnumOption**](EnumOption.md) | [**EnumOption**](EnumOption.md) |  | [optional] 
**[old_date_value](#old_date_value)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**[new_date_value](#new_date_value)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**[old_people_value](#old_people_value)** | list, tuple,  | tuple,  | *Conditional*. The old value of a people custom field story. | [optional] 
**[new_people_value](#new_people_value)** | list, tuple,  | tuple,  | *Conditional*. The new value of a people custom field story. | [optional] 
**[old_multi_enum_values](#old_multi_enum_values)** | list, tuple,  | tuple,  | *Conditional*. The old value of a multi-enum custom field story. | [optional] 
**[new_multi_enum_values](#new_multi_enum_values)** | list, tuple,  | tuple,  | *Conditional*. The new value of a multi-enum custom field story. | [optional] 
**new_approval_status** | str,  | str,  | *Conditional*. The new value of approval status. | [optional] 
**old_approval_status** | str,  | str,  | *Conditional*. The old value of approval status. | [optional] 
**duplicate_of** | [**TaskCompact**](TaskCompact.md) | [**TaskCompact**](TaskCompact.md) |  | [optional] 
**duplicated_from** | [**TaskCompact**](TaskCompact.md) | [**TaskCompact**](TaskCompact.md) |  | [optional] 
**dependency** | [**TaskCompact**](TaskCompact.md) | [**TaskCompact**](TaskCompact.md) |  | [optional] 
**source** | str,  | str,  | The component of the Asana product the user used to trigger the story. | [optional] must be one of ["web", "email", "mobile", "api", "unknown", ] 
**[target](#target)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# hearts

*Deprecated - please use likes instead*  *Conditional*. Array of likes for users who have hearted this story.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | *Deprecated - please use likes instead*  *Conditional*. Array of likes for users who have hearted this story. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Like**](Like.md) | [**Like**](Like.md) | [**Like**](Like.md) |  | 

# likes

*Conditional*. Array of likes for users who have liked this story.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | *Conditional*. Array of likes for users who have liked this story. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Like**](Like.md) | [**Like**](Like.md) | [**Like**](Like.md) |  | 

# previews

*Conditional*. A collection of previews to be displayed in the story.  *Note: This property only exists for comment stories.*

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | *Conditional*. A collection of previews to be displayed in the story.  *Note: This property only exists for comment stories.* | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Preview**](Preview.md) | [**Preview**](Preview.md) | [**Preview**](Preview.md) |  | 

# old_date_value

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[StoryResponseDates](StoryResponseDates.md) | [**StoryResponseDates**](StoryResponseDates.md) | [**StoryResponseDates**](StoryResponseDates.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | *Conditional*. The old value of a date custom field story. | 

# all_of_1

*Conditional*. The old value of a date custom field story.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | *Conditional*. The old value of a date custom field story. | 

# new_date_value

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[StoryResponseDates](StoryResponseDates.md) | [**StoryResponseDates**](StoryResponseDates.md) | [**StoryResponseDates**](StoryResponseDates.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | *Conditional* The new value of a date custom field story. | 

# all_of_1

*Conditional* The new value of a date custom field story.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | *Conditional* The new value of a date custom field story. | 

# old_people_value

*Conditional*. The old value of a people custom field story.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | *Conditional*. The old value of a people custom field story. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UserCompact**](UserCompact.md) | [**UserCompact**](UserCompact.md) | [**UserCompact**](UserCompact.md) |  | 

# new_people_value

*Conditional*. The new value of a people custom field story.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | *Conditional*. The new value of a people custom field story. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**UserCompact**](UserCompact.md) | [**UserCompact**](UserCompact.md) | [**UserCompact**](UserCompact.md) |  | 

# old_multi_enum_values

*Conditional*. The old value of a multi-enum custom field story.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | *Conditional*. The old value of a multi-enum custom field story. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EnumOption**](EnumOption.md) | [**EnumOption**](EnumOption.md) | [**EnumOption**](EnumOption.md) |  | 

# new_multi_enum_values

*Conditional*. The new value of a multi-enum custom field story.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | *Conditional*. The new value of a multi-enum custom field story. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**EnumOption**](EnumOption.md) | [**EnumOption**](EnumOption.md) | [**EnumOption**](EnumOption.md) |  | 

# target

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[TaskCompact](TaskCompact.md) | [**TaskCompact**](TaskCompact.md) | [**TaskCompact**](TaskCompact.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The object this story is associated with. Currently may only be a task. | 

# all_of_1

The object this story is associated with. Currently may only be a task.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The object this story is associated with. Currently may only be a task. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

