# asana.model.portfolio_response.PortfolioResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[PortfolioBase](PortfolioBase.md) | [**PortfolioBase**](PortfolioBase.md) | [**PortfolioBase**](PortfolioBase.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created_at** | str, datetime,  | str,  | The time at which this resource was created. | [optional] value must conform to RFC-3339 date-time
**created_by** | [**UserCompact**](UserCompact.md) | [**UserCompact**](UserCompact.md) |  | [optional] 
**[custom_field_settings](#custom_field_settings)** | list, tuple,  | tuple,  | Array of custom field settings applied to the portfolio. | [optional] 
**[current_status_update](#current_status_update)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The latest &#x60;status_update&#x60; posted to this portfolio. | [optional] 
**due_on** | None, str, datetime,  | NoneClass, str,  | The localized day on which this portfolio is due. This takes a date with format YYYY-MM-DD. | [optional] value must conform to RFC-3339 date-time
**[custom_fields](#custom_fields)** | list, tuple,  | tuple,  | Array of Custom Fields. | [optional] 
**[members](#members)** | list, tuple,  | tuple,  |  | [optional] 
**owner** | [**UserCompact**](UserCompact.md) | [**UserCompact**](UserCompact.md) |  | [optional] 
**start_on** | None, str, date,  | NoneClass, str,  | The day on which work for this portfolio begins, or null if the portfolio has no start date. This takes a date with &#x60;YYYY-MM-DD&#x60; format. *Note: &#x60;due_on&#x60; must be present in the request when setting or unsetting the &#x60;start_on&#x60; parameter. Additionally, &#x60;start_on&#x60; and &#x60;due_on&#x60; cannot be the same date.* | [optional] value must conform to RFC-3339 full-date YYYY-MM-DD
**[workspace](#workspace)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**permalink_url** | str,  | str,  | A url that points directly to the object within Asana. | [optional] 
**public** | bool,  | BoolClass,  | True if the portfolio is public to its workspace members. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# custom_field_settings

Array of custom field settings applied to the portfolio.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of custom field settings applied to the portfolio. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CustomFieldSettingResponse**](CustomFieldSettingResponse.md) | [**CustomFieldSettingResponse**](CustomFieldSettingResponse.md) | [**CustomFieldSettingResponse**](CustomFieldSettingResponse.md) |  | 

# current_status_update

The latest `status_update` posted to this portfolio.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO | The latest &#x60;status_update&#x60; posted to this portfolio. | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[StatusUpdateCompact](StatusUpdateCompact.md) | [**StatusUpdateCompact**](StatusUpdateCompact.md) | [**StatusUpdateCompact**](StatusUpdateCompact.md) |  | 

# custom_fields

Array of Custom Fields.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of Custom Fields. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CustomFieldCompact**](CustomFieldCompact.md) | [**CustomFieldCompact**](CustomFieldCompact.md) | [**CustomFieldCompact**](CustomFieldCompact.md) |  | 

# members

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  |  | 

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
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  | *Create-only*. The workspace or organization that the portfolio belongs to. | 

# all_of_1

*Create-only*. The workspace or organization that the portfolio belongs to.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | *Create-only*. The workspace or organization that the portfolio belongs to. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

