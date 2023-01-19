# asana.model.audit_log_event_resource.AuditLogEventResource

The primary object that was affected by this event.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The primary object that was affected by this event. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**resource_type** | str,  | str,  | The type of resource. | [optional] 
**resource_subtype** | str,  | str,  | The subtype of resource. Most resources will not have a subtype. | [optional] 
**gid** | str,  | str,  | Globally unique identifier of the resource. | [optional] 
**name** | str,  | str,  | The name of the resource. | [optional] 
**email** | str,  | str,  | The email of the resource, if applicable. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

