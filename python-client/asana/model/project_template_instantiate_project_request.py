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


class ProjectTemplateInstantiateProjectRequest(
    schemas.DictSchema
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        required = {
            "public",
            "name",
        }
        
        class properties:
            name = schemas.StrSchema
            public = schemas.BoolSchema
            team = schemas.StrSchema
            workspace = schemas.StrSchema
            is_strict = schemas.BoolSchema
            
            
            class requested_dates(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['DateVariableRequest']:
                        return DateVariableRequest
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['DateVariableRequest'], typing.List['DateVariableRequest']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'requested_dates':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'DateVariableRequest':
                    return super().__getitem__(i)
            __annotations__ = {
                "name": name,
                "public": public,
                "team": team,
                "workspace": workspace,
                "is_strict": is_strict,
                "requested_dates": requested_dates,
            }
    
    public: MetaOapg.properties.public
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["public"]) -> MetaOapg.properties.public: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["team"]) -> MetaOapg.properties.team: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["workspace"]) -> MetaOapg.properties.workspace: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_strict"]) -> MetaOapg.properties.is_strict: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requested_dates"]) -> MetaOapg.properties.requested_dates: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "public", "team", "workspace", "is_strict", "requested_dates", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["public"]) -> MetaOapg.properties.public: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["team"]) -> typing.Union[MetaOapg.properties.team, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["workspace"]) -> typing.Union[MetaOapg.properties.workspace, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_strict"]) -> typing.Union[MetaOapg.properties.is_strict, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requested_dates"]) -> typing.Union[MetaOapg.properties.requested_dates, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "public", "team", "workspace", "is_strict", "requested_dates", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        public: typing.Union[MetaOapg.properties.public, bool, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        team: typing.Union[MetaOapg.properties.team, str, schemas.Unset] = schemas.unset,
        workspace: typing.Union[MetaOapg.properties.workspace, str, schemas.Unset] = schemas.unset,
        is_strict: typing.Union[MetaOapg.properties.is_strict, bool, schemas.Unset] = schemas.unset,
        requested_dates: typing.Union[MetaOapg.properties.requested_dates, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'ProjectTemplateInstantiateProjectRequest':
        return super().__new__(
            cls,
            *args,
            public=public,
            name=name,
            team=team,
            workspace=workspace,
            is_strict=is_strict,
            requested_dates=requested_dates,
            _configuration=_configuration,
            **kwargs,
        )

from asana.model.date_variable_request import DateVariableRequest
