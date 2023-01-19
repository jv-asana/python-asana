# asana.model.enum_option.EnumOption

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[AsanaResource](AsanaResource.md) | [**AsanaResource**](AsanaResource.md) | [**AsanaResource**](AsanaResource.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  | Enum options are the possible values which an enum custom field can adopt. An enum custom field must contain at least 1 enum option but no more than 500.  You can add enum options to a custom field by using the &#x60;POST /custom_fields/custom_field_gid/enum_options&#x60; endpoint.  **It is not possible to remove or delete an enum option**. Instead, enum options can be disabled by updating the &#x60;enabled&#x60; field to false with the &#x60;PUT /enum_options/enum_option_gid&#x60; endpoint. Other attributes can be updated similarly.  On creation of an enum option, &#x60;enabled&#x60; is always set to &#x60;true&#x60;, meaning the enum option is a selectable value for the custom field. Setting &#x60;enabled&#x3D;false&#x60; is equivalent to “trashing” the enum option in the Asana web app within the “Edit Fields” dialog. The enum option will no longer be selectable but, if the enum option value was previously set within a task, the task will retain the value.  Enum options are an ordered list and by default new enum options are inserted at the end. Ordering in relation to existing enum options can be specified on creation by using &#x60;insert_before&#x60; or &#x60;insert_after&#x60; to reference an existing enum option. Only one of &#x60;insert_before&#x60; and &#x60;insert_after&#x60; can be provided when creating a new enum option.  An enum options list can be reordered with the &#x60;POST /custom_fields/custom_field_gid/enum_options/insert&#x60; endpoint. | 

# all_of_1

Enum options are the possible values which an enum custom field can adopt. An enum custom field must contain at least 1 enum option but no more than 500.  You can add enum options to a custom field by using the `POST /custom_fields/custom_field_gid/enum_options` endpoint.  **It is not possible to remove or delete an enum option**. Instead, enum options can be disabled by updating the `enabled` field to false with the `PUT /enum_options/enum_option_gid` endpoint. Other attributes can be updated similarly.  On creation of an enum option, `enabled` is always set to `true`, meaning the enum option is a selectable value for the custom field. Setting `enabled=false` is equivalent to “trashing” the enum option in the Asana web app within the “Edit Fields” dialog. The enum option will no longer be selectable but, if the enum option value was previously set within a task, the task will retain the value.  Enum options are an ordered list and by default new enum options are inserted at the end. Ordering in relation to existing enum options can be specified on creation by using `insert_before` or `insert_after` to reference an existing enum option. Only one of `insert_before` and `insert_after` can be provided when creating a new enum option.  An enum options list can be reordered with the `POST /custom_fields/custom_field_gid/enum_options/insert` endpoint.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Enum options are the possible values which an enum custom field can adopt. An enum custom field must contain at least 1 enum option but no more than 500.  You can add enum options to a custom field by using the &#x60;POST /custom_fields/custom_field_gid/enum_options&#x60; endpoint.  **It is not possible to remove or delete an enum option**. Instead, enum options can be disabled by updating the &#x60;enabled&#x60; field to false with the &#x60;PUT /enum_options/enum_option_gid&#x60; endpoint. Other attributes can be updated similarly.  On creation of an enum option, &#x60;enabled&#x60; is always set to &#x60;true&#x60;, meaning the enum option is a selectable value for the custom field. Setting &#x60;enabled&#x3D;false&#x60; is equivalent to “trashing” the enum option in the Asana web app within the “Edit Fields” dialog. The enum option will no longer be selectable but, if the enum option value was previously set within a task, the task will retain the value.  Enum options are an ordered list and by default new enum options are inserted at the end. Ordering in relation to existing enum options can be specified on creation by using &#x60;insert_before&#x60; or &#x60;insert_after&#x60; to reference an existing enum option. Only one of &#x60;insert_before&#x60; and &#x60;insert_after&#x60; can be provided when creating a new enum option.  An enum options list can be reordered with the &#x60;POST /custom_fields/custom_field_gid/enum_options/insert&#x60; endpoint. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | The name of the enum option. | [optional] 
**enabled** | bool,  | BoolClass,  | Whether or not the enum option is a selectable value for the custom field. | [optional] 
**color** | str,  | str,  | The color of the enum option. Defaults to ‘none’. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

