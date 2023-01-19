# asana.model.audit_log_event_context.AuditLogEventContext

The context from which this event originated.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The context from which this event originated. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**context_type** | str,  | str,  | The type of context. Can be one of &#x60;web&#x60;, &#x60;desktop&#x60;, &#x60;mobile&#x60;, &#x60;asana_support&#x60;, &#x60;asana&#x60;, &#x60;email&#x60;, or &#x60;api&#x60;. | [optional] must be one of ["web", "desktop", "mobile", "asana_support", "asana", "email", "api", ] 
**api_authentication_method** | str,  | str,  | The authentication method used in the context of an API request. Only present if the &#x60;context_type&#x60; is &#x60;api&#x60;. Can be one of &#x60;cookie&#x60;, &#x60;oauth&#x60;, &#x60;personal_access_token&#x60;, or &#x60;service_account&#x60;. | [optional] must be one of ["cookie", "oauth", "personal_access_token", "service_account", ] 
**client_ip_address** | str,  | str,  | The IP address of the client that initiated the event, if applicable. | [optional] 
**user_agent** | str,  | str,  | The user agent of the client that initiated the event, if applicable. | [optional] 
**oauth_app_name** | str,  | str,  | The name of the OAuth App that initiated the event. Only present if the &#x60;api_authentication_method&#x60; is &#x60;oauth&#x60;. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

