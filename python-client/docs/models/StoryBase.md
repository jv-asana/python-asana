# asana.model.story_base.StoryBase

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[AsanaResource](AsanaResource.md) | [**AsanaResource**](AsanaResource.md) | [**AsanaResource**](AsanaResource.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  | A story represents an activity associated with an object in the Asana system. | 

# all_of_1

A story represents an activity associated with an object in the Asana system.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A story represents an activity associated with an object in the Asana system. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | str, datetime,  | str,  | The time at which this resource was created. | [optional] value must conform to RFC-3339 date-time
**resource_subtype** | str,  | str,  | The subtype of this resource. Different subtypes retain many of the same fields and behavior, but may render differently in Asana or represent resources with different semantic meaning. | [optional] 
**text** | str,  | str,  | The plain text of the comment to add. Cannot be used with html_text. | [optional] 
**html_text** | str,  | str,  | [Opt In](/docs/input-output-options). HTML formatted text for a comment. This will not include the name of the creator. | [optional] 
**is_pinned** | bool,  | BoolClass,  | *Conditional*. Whether the story should be pinned on the resource. | [optional] 
**sticker_name** | str,  | str,  | The name of the sticker in this story. &#x60;null&#x60; if there is no sticker. | [optional] must be one of ["green_checkmark", "people_dancing", "dancing_unicorn", "heart", "party_popper", "people_waving_flags", "splashing_narwhal", "trophy", "yeti_riding_unicorn", "celebrating_people", "determined_climbers", "phoenix_spreading_love", ] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

