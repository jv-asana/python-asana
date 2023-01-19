# asana.model.audit_log_event_actor.AuditLogEventActor

The entity that triggered the event. Will typically be a user.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The entity that triggered the event. Will typically be a user. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**actor_type** | str,  | str,  | The type of actor. Can be one of &#x60;user&#x60;, &#x60;asana&#x60;, &#x60;asana_support&#x60;, &#x60;anonymous&#x60;, or &#x60;external_administrator&#x60;. | [optional] must be one of ["user", "asana", "asana_support", "anonymous", "external_administrator", ] 
**gid** | str,  | str,  | Globally unique identifier of the actor, if it is a user. | [optional] 
**name** | str,  | str,  | The name of the actor, if it is a user. | [optional] 
**email** | str,  | str,  | The email of the actor, if it is a user. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

