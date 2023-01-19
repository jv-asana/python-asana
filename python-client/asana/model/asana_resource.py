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


class AsanaResource(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    A generic Asana Resource, containing a globally unique identifier.
    """


    class MetaOapg:
        
        class properties:
            gid = schemas.StrSchema
            resource_type = schemas.StrSchema
            __annotations__ = {
                "gid": gid,
                "resource_type": resource_type,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gid"]) -> MetaOapg.properties.gid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["resource_type"]) -> MetaOapg.properties.resource_type: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["gid", "resource_type", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gid"]) -> typing.Union[MetaOapg.properties.gid, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["resource_type"]) -> typing.Union[MetaOapg.properties.resource_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["gid", "resource_type", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        gid: typing.Union[MetaOapg.properties.gid, str, schemas.Unset] = schemas.unset,
        resource_type: typing.Union[MetaOapg.properties.resource_type, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'AsanaResource':
        return super().__new__(
            cls,
            *args,
            gid=gid,
            resource_type=resource_type,
            _configuration=_configuration,
            **kwargs,
        )
