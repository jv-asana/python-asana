# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/developer-docs/master/defs/asana_oas.yaml).  # noqa: E501

    The version of the OpenAPI document: 1.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from asana import schemas  # noqa: F401


class BatchRequestAction(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    An action object for use in a batch request.
    """


    class MetaOapg:
        required = {
            "method",
            "relative_path",
        }
        
        class properties:
            relative_path = schemas.StrSchema
            
            
            class method(
                schemas.EnumBase,
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    enum_value_to_name = {
                        "get": "GET",
                        "post": "POST",
                        "put": "PUT",
                        "delete": "DELETE",
                        "patch": "PATCH",
                        "head": "HEAD",
                    }
                
                @schemas.classproperty
                def GET(cls):
                    return cls("get")
                
                @schemas.classproperty
                def POST(cls):
                    return cls("post")
                
                @schemas.classproperty
                def PUT(cls):
                    return cls("put")
                
                @schemas.classproperty
                def DELETE(cls):
                    return cls("delete")
                
                @schemas.classproperty
                def PATCH(cls):
                    return cls("patch")
                
                @schemas.classproperty
                def HEAD(cls):
                    return cls("head")
            data = schemas.DictSchema
            
            
            class options(
                schemas.DictSchema
            ):
            
            
                class MetaOapg:
                    
                    class properties:
                        limit = schemas.IntSchema
                        offset = schemas.IntSchema
                        
                        
                        class fields(
                            schemas.ListSchema
                        ):
                        
                        
                            class MetaOapg:
                                items = schemas.StrSchema
                        
                            def __new__(
                                cls,
                                arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
                                _configuration: typing.Optional[schemas.Configuration] = None,
                            ) -> 'fields':
                                return super().__new__(
                                    cls,
                                    arg,
                                    _configuration=_configuration,
                                )
                        
                            def __getitem__(self, i: int) -> MetaOapg.items:
                                return super().__getitem__(i)
                        __annotations__ = {
                            "limit": limit,
                            "offset": offset,
                            "fields": fields,
                        }
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["limit"]) -> MetaOapg.properties.limit: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["offset"]) -> MetaOapg.properties.offset: ...
                
                @typing.overload
                def __getitem__(self, name: typing_extensions.Literal["fields"]) -> MetaOapg.properties.fields: ...
                
                @typing.overload
                def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
                
                def __getitem__(self, name: typing.Union[typing_extensions.Literal["limit", "offset", "fields", ], str]):
                    # dict_instance[name] accessor
                    return super().__getitem__(name)
                
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["limit"]) -> typing.Union[MetaOapg.properties.limit, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["offset"]) -> typing.Union[MetaOapg.properties.offset, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: typing_extensions.Literal["fields"]) -> typing.Union[MetaOapg.properties.fields, schemas.Unset]: ...
                
                @typing.overload
                def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
                
                def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["limit", "offset", "fields", ], str]):
                    return super().get_item_oapg(name)
                
            
                def __new__(
                    cls,
                    *args: typing.Union[dict, frozendict.frozendict, ],
                    limit: typing.Union[MetaOapg.properties.limit, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    offset: typing.Union[MetaOapg.properties.offset, decimal.Decimal, int, schemas.Unset] = schemas.unset,
                    fields: typing.Union[MetaOapg.properties.fields, list, tuple, schemas.Unset] = schemas.unset,
                    _configuration: typing.Optional[schemas.Configuration] = None,
                    **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
                ) -> 'options':
                    return super().__new__(
                        cls,
                        *args,
                        limit=limit,
                        offset=offset,
                        fields=fields,
                        _configuration=_configuration,
                        **kwargs,
                    )
            __annotations__ = {
                "relative_path": relative_path,
                "method": method,
                "data": data,
                "options": options,
            }
    
    method: MetaOapg.properties.method
    relative_path: MetaOapg.properties.relative_path
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["relative_path"]) -> MetaOapg.properties.relative_path: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["options"]) -> MetaOapg.properties.options: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["relative_path", "method", "data", "options", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["relative_path"]) -> MetaOapg.properties.relative_path: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["method"]) -> MetaOapg.properties.method: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["options"]) -> typing.Union[MetaOapg.properties.options, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["relative_path", "method", "data", "options", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        method: typing.Union[MetaOapg.properties.method, str, ],
        relative_path: typing.Union[MetaOapg.properties.relative_path, str, ],
        data: typing.Union[MetaOapg.properties.data, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        options: typing.Union[MetaOapg.properties.options, dict, frozendict.frozendict, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'BatchRequestAction':
        return super().__new__(
            cls,
            *args,
            method=method,
            relative_path=relative_path,
            data=data,
            options=options,
            _configuration=_configuration,
            **kwargs,
        )
