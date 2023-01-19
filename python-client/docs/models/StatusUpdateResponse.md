# asana.model.status_update_response.StatusUpdateResponse

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[StatusUpdateBase](StatusUpdateBase.md) | [**StatusUpdateBase**](StatusUpdateBase.md) | [**StatusUpdateBase**](StatusUpdateBase.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

# all_of_1

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**author** | [**UserCompact**](UserCompact.md) | [**UserCompact**](UserCompact.md) |  | [optional] 
**created_at** | str, datetime,  | str,  | The time at which this resource was created. | [optional] value must conform to RFC-3339 date-time
**created_by** | [**UserCompact**](UserCompact.md) | [**UserCompact**](UserCompact.md) |  | [optional] 
**hearted** | bool,  | BoolClass,  | *Deprecated - please use liked instead* True if the status is hearted by the authorized user, false if not. | [optional] 
**[hearts](#hearts)** | list, tuple,  | tuple,  | *Deprecated - please use likes instead* Array of likes for users who have hearted this status. | [optional] 
**liked** | bool,  | BoolClass,  | True if the status is liked by the authorized user, false if not. | [optional] 
**[likes](#likes)** | list, tuple,  | tuple,  | Array of likes for users who have liked this status. | [optional] 
**modified_at** | str, datetime,  | str,  | The time at which this project status was last modified. *Note: This does not currently reflect any changes in associations such as comments that may have been added or removed from the status.* | [optional] value must conform to RFC-3339 date-time
**num_hearts** | decimal.Decimal, int,  | decimal.Decimal,  | *Deprecated - please use likes instead* The number of users who have hearted this status. | [optional] 
**num_likes** | decimal.Decimal, int,  | decimal.Decimal,  | The number of users who have liked this status. | [optional] 
**[parent](#parent)** | dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# hearts

*Deprecated - please use likes instead* Array of likes for users who have hearted this status.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | *Deprecated - please use likes instead* Array of likes for users who have hearted this status. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Like**](Like.md) | [**Like**](Like.md) | [**Like**](Like.md) |  | 

# likes

Array of likes for users who have liked this status.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Array of likes for users who have liked this status. | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Like**](Like.md) | [**Like**](Like.md) | [**Like**](Like.md) |  | 

# parent

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader,  | frozendict.frozendict, str, decimal.Decimal, BoolClass, NoneClass, tuple, bytes, FileIO |  | 

### Composed Schemas (allOf/anyOf/oneOf/not)
#### allOf
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[ProjectCompact](ProjectCompact.md) | [**ProjectCompact**](ProjectCompact.md) | [**ProjectCompact**](ProjectCompact.md) |  | 
[all_of_1](#all_of_1) | dict, frozendict.frozendict,  | frozendict.frozendict,  | The parent of the status update. This can be a project, goal or portfolio, and indicates that this status was sent on that object. | 

# all_of_1

The parent of the status update. This can be a project, goal or portfolio, and indicates that this status was sent on that object.

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | The parent of the status update. This can be a project, goal or portfolio, and indicates that this status was sent on that object. | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

