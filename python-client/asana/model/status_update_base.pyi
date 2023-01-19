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


class StatusUpdateBase(
    schemas.ComposedSchema,
):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """


    class MetaOapg:
        
        
        class all_of_1(
            schemas.DictSchema
        ):
        
        
            class MetaOapg:
                required = {
                    "status_type",
                    "text",
                }
                
                class properties:
                    text = schemas.StrSchema
                    html_text = schemas.StrSchema
                    
                    
                    class status_type(
                        schemas.EnumBase,
                        schemas.StrSchema
                    ):
                        
                        @schemas.classproperty
                        def ON_TRACK(cls):
                            return cls("on_track")
                        
                        @schemas.classproperty
                        def AT_RISK(cls):
                            return cls("at_risk")
                        
                        @schemas.classproperty
                        def OFF_TRACK(cls):
                            return cls("off_track")
                        
                        @schemas.classproperty
                        def ON_HOLD(cls):
                            return cls("on_hold")
                        
                        @schemas.classproperty
                        def COMPLETE(cls):
                            return cls("complete")
                        
                        @schemas.classproperty
                        def ACHIEVED(cls):
                            return cls("achieved")
                        
                        @schemas.classproperty
                        def PARTIAL(cls):
                            return cls("partial")
                        
                        @schemas.classproperty
                        def MISSED(cls):
                            return cls("missed")
                        
                        @schemas.classproperty
                        def DROPPED(cls):
                            return cls("dropped")
                    __annotations__ = {
                        "text": text,
                        "html_text": html_text,
                        "status_type": status_type,
                    }
            
            status_type: MetaOapg.properties.status_type
            text: MetaOapg.properties.text
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["html_text"]) -> MetaOapg.properties.html_text: ...
            
            @typing.overload
            def __getitem__(self, name: typing_extensions.Literal["status_type"]) -> MetaOapg.properties.status_type: ...
            
            @typing.overload
            def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
            
            def __getitem__(self, name: typing.Union[typing_extensions.Literal["text", "html_text", "status_type", ], str]):
                # dict_instance[name] accessor
                return super().__getitem__(name)
            
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["text"]) -> MetaOapg.properties.text: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["html_text"]) -> typing.Union[MetaOapg.properties.html_text, schemas.Unset]: ...
            
            @typing.overload
            def get_item_oapg(self, name: typing_extensions.Literal["status_type"]) -> MetaOapg.properties.status_type: ...
            
            @typing.overload
            def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
            
            def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["text", "html_text", "status_type", ], str]):
                return super().get_item_oapg(name)
            
        
            def __new__(
                cls,
                *args: typing.Union[dict, frozendict.frozendict, ],
                status_type: typing.Union[MetaOapg.properties.status_type, str, ],
                text: typing.Union[MetaOapg.properties.text, str, ],
                html_text: typing.Union[MetaOapg.properties.html_text, str, schemas.Unset] = schemas.unset,
                _configuration: typing.Optional[schemas.Configuration] = None,
                **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
            ) -> 'all_of_1':
                return super().__new__(
                    cls,
                    *args,
                    status_type=status_type,
                    text=text,
                    html_text=html_text,
                    _configuration=_configuration,
                    **kwargs,
                )
        
        @classmethod
        @functools.lru_cache()
        def all_of(cls):
            # we need this here to make our import statements work
            # we must store _composed_schemas in here so the code is only run
            # when we invoke this method. If we kept this at the class
            # level we would get an error because the class level
            # code would be run when this module is imported, and these composed
            # classes don't exist yet because their module has not finished
            # loading
            return [
                StatusUpdateCompact,
                cls.all_of_1,
            ]


    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, bool, None, list, tuple, bytes, io.FileIO, io.BufferedReader, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'StatusUpdateBase':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
            **kwargs,
        )

from asana.model.status_update_compact import StatusUpdateCompact
