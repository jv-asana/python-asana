# asana.model.project_save_as_template_request.ProjectSaveAsTemplateRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**public** | bool,  | BoolClass,  | Sets the project template to public to its team. | 
**name** | str,  | str,  | The name of the new project template. | 
**team** | str,  | str,  | Sets the team of the new project template. If the project exists in an organization, specify team and not workspace. | [optional] 
**workspace** | str,  | str,  | Sets the workspace of the new project template. Only specify workspace if the project exists in a workspace. | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

