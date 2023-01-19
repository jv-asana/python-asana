# asana.model.preview.Preview

A collection of rich text that will be displayed as a preview to another app.  This is read-only except for a small group of whitelisted apps.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | A collection of rich text that will be displayed as a preview to another app.  This is read-only except for a small group of whitelisted apps. | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**fallback** | str,  | str,  | Some fallback text to display if unable to display the full preview. | [optional] 
**footer** | str,  | str,  | Text to display in the footer. | [optional] 
**header** | str,  | str,  | Text to display in the header. | [optional] 
**header_link** | str,  | str,  | Where the header will link to. | [optional] 
**html_text** | str,  | str,  | HTML formatted text for the body of the preview. | [optional] 
**text** | str,  | str,  | Text for the body of the preview. | [optional] 
**title** | str,  | str,  | Text to display as the title. | [optional] 
**title_link** | str,  | str,  | Where to title will link to. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

