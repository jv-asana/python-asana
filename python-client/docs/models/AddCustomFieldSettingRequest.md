# asana.model.add_custom_field_setting_request.AddCustomFieldSettingRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**custom_field** | str,  | str,  | The custom field to associate with this container. | 
**is_important** | bool,  | BoolClass,  | Whether this field should be considered important to this container (for instance, to display in the list view of items in the container). | [optional] 
**insert_before** | str,  | str,  | A gid of a Custom Field Setting on this container, before which the new Custom Field Setting will be added.  &#x60;insert_before&#x60; and &#x60;insert_after&#x60; parameters cannot both be specified. | [optional] 
**insert_after** | str,  | str,  | A gid of a Custom Field Setting on this container, after which the new Custom Field Setting will be added.  &#x60;insert_before&#x60; and &#x60;insert_after&#x60; parameters cannot both be specified. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

