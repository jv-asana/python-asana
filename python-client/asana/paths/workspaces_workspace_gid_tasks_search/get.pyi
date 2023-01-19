# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from urllib3._collections import HTTPHeaderDict

from asana import api_client, exceptions
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

from asana.model.error_response import ErrorResponse
from asana.model.task_compact import TaskCompact

# Query params
OptPrettySchema = schemas.BoolSchema


class OptFieldsSchema(
    schemas.ListSchema
):


    class MetaOapg:
        items = schemas.StrSchema

    def __new__(
        cls,
        arg: typing.Union[typing.Tuple[typing.Union[MetaOapg.items, str, ]], typing.List[typing.Union[MetaOapg.items, str, ]]],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'OptFieldsSchema':
        return super().__new__(
            cls,
            arg,
            _configuration=_configuration,
        )

    def __getitem__(self, i: int) -> MetaOapg.items:
        return super().__getitem__(i)
TextSchema = schemas.StrSchema


class ResourceSubtypeSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def DEFAULT_TASK(cls):
        return cls("default_task")
    
    @schemas.classproperty
    def MILESTONE(cls):
        return cls("milestone")
AssigneeAnySchema = schemas.StrSchema
AssigneeNotSchema = schemas.StrSchema
PortfoliosAnySchema = schemas.StrSchema
ProjectsAnySchema = schemas.StrSchema
ProjectsNotSchema = schemas.StrSchema
ProjectsAllSchema = schemas.StrSchema
SectionsAnySchema = schemas.StrSchema
SectionsNotSchema = schemas.StrSchema
SectionsAllSchema = schemas.StrSchema
TagsAnySchema = schemas.StrSchema
TagsNotSchema = schemas.StrSchema
TagsAllSchema = schemas.StrSchema
TeamsAnySchema = schemas.StrSchema
FollowersNotSchema = schemas.StrSchema
CreatedByAnySchema = schemas.StrSchema
CreatedByNotSchema = schemas.StrSchema
AssignedByAnySchema = schemas.StrSchema
AssignedByNotSchema = schemas.StrSchema
LikedByNotSchema = schemas.StrSchema
CommentedOnByNotSchema = schemas.StrSchema
DueOnBeforeSchema = schemas.DateSchema
DueOnAfterSchema = schemas.DateSchema


class DueOnSchema(
    schemas.DateBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        format = 'date'


    def __new__(
        cls,
        *args: typing.Union[None, str, date, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'DueOnSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
DueAtBeforeSchema = schemas.DateTimeSchema
DueAtAfterSchema = schemas.DateTimeSchema
StartOnBeforeSchema = schemas.DateSchema
StartOnAfterSchema = schemas.DateSchema


class StartOnSchema(
    schemas.DateBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        format = 'date'


    def __new__(
        cls,
        *args: typing.Union[None, str, date, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'StartOnSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
CreatedOnBeforeSchema = schemas.DateSchema
CreatedOnAfterSchema = schemas.DateSchema


class CreatedOnSchema(
    schemas.DateBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        format = 'date'


    def __new__(
        cls,
        *args: typing.Union[None, str, date, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CreatedOnSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
CreatedAtBeforeSchema = schemas.DateTimeSchema
CreatedAtAfterSchema = schemas.DateTimeSchema
CompletedOnBeforeSchema = schemas.DateSchema
CompletedOnAfterSchema = schemas.DateSchema


class CompletedOnSchema(
    schemas.DateBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        format = 'date'


    def __new__(
        cls,
        *args: typing.Union[None, str, date, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'CompletedOnSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
CompletedAtBeforeSchema = schemas.DateTimeSchema
CompletedAtAfterSchema = schemas.DateTimeSchema
ModifiedOnBeforeSchema = schemas.DateSchema
ModifiedOnAfterSchema = schemas.DateSchema


class ModifiedOnSchema(
    schemas.DateBase,
    schemas.StrBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneStrMixin
):


    class MetaOapg:
        format = 'date'


    def __new__(
        cls,
        *args: typing.Union[None, str, date, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
    ) -> 'ModifiedOnSchema':
        return super().__new__(
            cls,
            *args,
            _configuration=_configuration,
        )
ModifiedAtBeforeSchema = schemas.DateTimeSchema
ModifiedAtAfterSchema = schemas.DateTimeSchema
IsBlockingSchema = schemas.BoolSchema
IsBlockedSchema = schemas.BoolSchema
HasAttachmentSchema = schemas.BoolSchema
CompletedSchema = schemas.BoolSchema
IsSubtaskSchema = schemas.BoolSchema


class SortBySchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def DUE_DATE(cls):
        return cls("due_date")
    
    @schemas.classproperty
    def CREATED_AT(cls):
        return cls("created_at")
    
    @schemas.classproperty
    def COMPLETED_AT(cls):
        return cls("completed_at")
    
    @schemas.classproperty
    def LIKES(cls):
        return cls("likes")
    
    @schemas.classproperty
    def MODIFIED_AT(cls):
        return cls("modified_at")
SortAscendingSchema = schemas.BoolSchema
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'opt_pretty': typing.Union[OptPrettySchema, bool, ],
        'opt_fields': typing.Union[OptFieldsSchema, list, tuple, ],
        'text': typing.Union[TextSchema, str, ],
        'resource_subtype': typing.Union[ResourceSubtypeSchema, str, ],
        'assignee.any': typing.Union[AssigneeAnySchema, str, ],
        'assignee.not': typing.Union[AssigneeNotSchema, str, ],
        'portfolios.any': typing.Union[PortfoliosAnySchema, str, ],
        'projects.any': typing.Union[ProjectsAnySchema, str, ],
        'projects.not': typing.Union[ProjectsNotSchema, str, ],
        'projects.all': typing.Union[ProjectsAllSchema, str, ],
        'sections.any': typing.Union[SectionsAnySchema, str, ],
        'sections.not': typing.Union[SectionsNotSchema, str, ],
        'sections.all': typing.Union[SectionsAllSchema, str, ],
        'tags.any': typing.Union[TagsAnySchema, str, ],
        'tags.not': typing.Union[TagsNotSchema, str, ],
        'tags.all': typing.Union[TagsAllSchema, str, ],
        'teams.any': typing.Union[TeamsAnySchema, str, ],
        'followers.not': typing.Union[FollowersNotSchema, str, ],
        'created_by.any': typing.Union[CreatedByAnySchema, str, ],
        'created_by.not': typing.Union[CreatedByNotSchema, str, ],
        'assigned_by.any': typing.Union[AssignedByAnySchema, str, ],
        'assigned_by.not': typing.Union[AssignedByNotSchema, str, ],
        'liked_by.not': typing.Union[LikedByNotSchema, str, ],
        'commented_on_by.not': typing.Union[CommentedOnByNotSchema, str, ],
        'due_on.before': typing.Union[DueOnBeforeSchema, str, date, ],
        'due_on.after': typing.Union[DueOnAfterSchema, str, date, ],
        'due_on': typing.Union[DueOnSchema, None, str, date, ],
        'due_at.before': typing.Union[DueAtBeforeSchema, str, datetime, ],
        'due_at.after': typing.Union[DueAtAfterSchema, str, datetime, ],
        'start_on.before': typing.Union[StartOnBeforeSchema, str, date, ],
        'start_on.after': typing.Union[StartOnAfterSchema, str, date, ],
        'start_on': typing.Union[StartOnSchema, None, str, date, ],
        'created_on.before': typing.Union[CreatedOnBeforeSchema, str, date, ],
        'created_on.after': typing.Union[CreatedOnAfterSchema, str, date, ],
        'created_on': typing.Union[CreatedOnSchema, None, str, date, ],
        'created_at.before': typing.Union[CreatedAtBeforeSchema, str, datetime, ],
        'created_at.after': typing.Union[CreatedAtAfterSchema, str, datetime, ],
        'completed_on.before': typing.Union[CompletedOnBeforeSchema, str, date, ],
        'completed_on.after': typing.Union[CompletedOnAfterSchema, str, date, ],
        'completed_on': typing.Union[CompletedOnSchema, None, str, date, ],
        'completed_at.before': typing.Union[CompletedAtBeforeSchema, str, datetime, ],
        'completed_at.after': typing.Union[CompletedAtAfterSchema, str, datetime, ],
        'modified_on.before': typing.Union[ModifiedOnBeforeSchema, str, date, ],
        'modified_on.after': typing.Union[ModifiedOnAfterSchema, str, date, ],
        'modified_on': typing.Union[ModifiedOnSchema, None, str, date, ],
        'modified_at.before': typing.Union[ModifiedAtBeforeSchema, str, datetime, ],
        'modified_at.after': typing.Union[ModifiedAtAfterSchema, str, datetime, ],
        'is_blocking': typing.Union[IsBlockingSchema, bool, ],
        'is_blocked': typing.Union[IsBlockedSchema, bool, ],
        'has_attachment': typing.Union[HasAttachmentSchema, bool, ],
        'completed': typing.Union[CompletedSchema, bool, ],
        'is_subtask': typing.Union[IsSubtaskSchema, bool, ],
        'sort_by': typing.Union[SortBySchema, str, ],
        'sort_ascending': typing.Union[SortAscendingSchema, bool, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_opt_pretty = api_client.QueryParameter(
    name="opt_pretty",
    style=api_client.ParameterStyle.FORM,
    schema=OptPrettySchema,
    explode=True,
)
request_query_opt_fields = api_client.QueryParameter(
    name="opt_fields",
    style=api_client.ParameterStyle.FORM,
    schema=OptFieldsSchema,
)
request_query_text = api_client.QueryParameter(
    name="text",
    style=api_client.ParameterStyle.FORM,
    schema=TextSchema,
    explode=True,
)
request_query_resource_subtype = api_client.QueryParameter(
    name="resource_subtype",
    style=api_client.ParameterStyle.FORM,
    schema=ResourceSubtypeSchema,
    explode=True,
)
request_query_assignee_any = api_client.QueryParameter(
    name="assignee.any",
    style=api_client.ParameterStyle.FORM,
    schema=AssigneeAnySchema,
    explode=True,
)
request_query_assignee_not = api_client.QueryParameter(
    name="assignee.not",
    style=api_client.ParameterStyle.FORM,
    schema=AssigneeNotSchema,
    explode=True,
)
request_query_portfolios_any = api_client.QueryParameter(
    name="portfolios.any",
    style=api_client.ParameterStyle.FORM,
    schema=PortfoliosAnySchema,
    explode=True,
)
request_query_projects_any = api_client.QueryParameter(
    name="projects.any",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectsAnySchema,
    explode=True,
)
request_query_projects_not = api_client.QueryParameter(
    name="projects.not",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectsNotSchema,
    explode=True,
)
request_query_projects_all = api_client.QueryParameter(
    name="projects.all",
    style=api_client.ParameterStyle.FORM,
    schema=ProjectsAllSchema,
    explode=True,
)
request_query_sections_any = api_client.QueryParameter(
    name="sections.any",
    style=api_client.ParameterStyle.FORM,
    schema=SectionsAnySchema,
    explode=True,
)
request_query_sections_not = api_client.QueryParameter(
    name="sections.not",
    style=api_client.ParameterStyle.FORM,
    schema=SectionsNotSchema,
    explode=True,
)
request_query_sections_all = api_client.QueryParameter(
    name="sections.all",
    style=api_client.ParameterStyle.FORM,
    schema=SectionsAllSchema,
    explode=True,
)
request_query_tags_any = api_client.QueryParameter(
    name="tags.any",
    style=api_client.ParameterStyle.FORM,
    schema=TagsAnySchema,
    explode=True,
)
request_query_tags_not = api_client.QueryParameter(
    name="tags.not",
    style=api_client.ParameterStyle.FORM,
    schema=TagsNotSchema,
    explode=True,
)
request_query_tags_all = api_client.QueryParameter(
    name="tags.all",
    style=api_client.ParameterStyle.FORM,
    schema=TagsAllSchema,
    explode=True,
)
request_query_teams_any = api_client.QueryParameter(
    name="teams.any",
    style=api_client.ParameterStyle.FORM,
    schema=TeamsAnySchema,
    explode=True,
)
request_query_followers_not = api_client.QueryParameter(
    name="followers.not",
    style=api_client.ParameterStyle.FORM,
    schema=FollowersNotSchema,
    explode=True,
)
request_query_created_by_any = api_client.QueryParameter(
    name="created_by.any",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedByAnySchema,
    explode=True,
)
request_query_created_by_not = api_client.QueryParameter(
    name="created_by.not",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedByNotSchema,
    explode=True,
)
request_query_assigned_by_any = api_client.QueryParameter(
    name="assigned_by.any",
    style=api_client.ParameterStyle.FORM,
    schema=AssignedByAnySchema,
    explode=True,
)
request_query_assigned_by_not = api_client.QueryParameter(
    name="assigned_by.not",
    style=api_client.ParameterStyle.FORM,
    schema=AssignedByNotSchema,
    explode=True,
)
request_query_liked_by_not = api_client.QueryParameter(
    name="liked_by.not",
    style=api_client.ParameterStyle.FORM,
    schema=LikedByNotSchema,
    explode=True,
)
request_query_commented_on_by_not = api_client.QueryParameter(
    name="commented_on_by.not",
    style=api_client.ParameterStyle.FORM,
    schema=CommentedOnByNotSchema,
    explode=True,
)
request_query_due_on_before = api_client.QueryParameter(
    name="due_on.before",
    style=api_client.ParameterStyle.FORM,
    schema=DueOnBeforeSchema,
    explode=True,
)
request_query_due_on_after = api_client.QueryParameter(
    name="due_on.after",
    style=api_client.ParameterStyle.FORM,
    schema=DueOnAfterSchema,
    explode=True,
)
request_query_due_on = api_client.QueryParameter(
    name="due_on",
    style=api_client.ParameterStyle.FORM,
    schema=DueOnSchema,
    explode=True,
)
request_query_due_at_before = api_client.QueryParameter(
    name="due_at.before",
    style=api_client.ParameterStyle.FORM,
    schema=DueAtBeforeSchema,
    explode=True,
)
request_query_due_at_after = api_client.QueryParameter(
    name="due_at.after",
    style=api_client.ParameterStyle.FORM,
    schema=DueAtAfterSchema,
    explode=True,
)
request_query_start_on_before = api_client.QueryParameter(
    name="start_on.before",
    style=api_client.ParameterStyle.FORM,
    schema=StartOnBeforeSchema,
    explode=True,
)
request_query_start_on_after = api_client.QueryParameter(
    name="start_on.after",
    style=api_client.ParameterStyle.FORM,
    schema=StartOnAfterSchema,
    explode=True,
)
request_query_start_on = api_client.QueryParameter(
    name="start_on",
    style=api_client.ParameterStyle.FORM,
    schema=StartOnSchema,
    explode=True,
)
request_query_created_on_before = api_client.QueryParameter(
    name="created_on.before",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedOnBeforeSchema,
    explode=True,
)
request_query_created_on_after = api_client.QueryParameter(
    name="created_on.after",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedOnAfterSchema,
    explode=True,
)
request_query_created_on = api_client.QueryParameter(
    name="created_on",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedOnSchema,
    explode=True,
)
request_query_created_at_before = api_client.QueryParameter(
    name="created_at.before",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedAtBeforeSchema,
    explode=True,
)
request_query_created_at_after = api_client.QueryParameter(
    name="created_at.after",
    style=api_client.ParameterStyle.FORM,
    schema=CreatedAtAfterSchema,
    explode=True,
)
request_query_completed_on_before = api_client.QueryParameter(
    name="completed_on.before",
    style=api_client.ParameterStyle.FORM,
    schema=CompletedOnBeforeSchema,
    explode=True,
)
request_query_completed_on_after = api_client.QueryParameter(
    name="completed_on.after",
    style=api_client.ParameterStyle.FORM,
    schema=CompletedOnAfterSchema,
    explode=True,
)
request_query_completed_on = api_client.QueryParameter(
    name="completed_on",
    style=api_client.ParameterStyle.FORM,
    schema=CompletedOnSchema,
    explode=True,
)
request_query_completed_at_before = api_client.QueryParameter(
    name="completed_at.before",
    style=api_client.ParameterStyle.FORM,
    schema=CompletedAtBeforeSchema,
    explode=True,
)
request_query_completed_at_after = api_client.QueryParameter(
    name="completed_at.after",
    style=api_client.ParameterStyle.FORM,
    schema=CompletedAtAfterSchema,
    explode=True,
)
request_query_modified_on_before = api_client.QueryParameter(
    name="modified_on.before",
    style=api_client.ParameterStyle.FORM,
    schema=ModifiedOnBeforeSchema,
    explode=True,
)
request_query_modified_on_after = api_client.QueryParameter(
    name="modified_on.after",
    style=api_client.ParameterStyle.FORM,
    schema=ModifiedOnAfterSchema,
    explode=True,
)
request_query_modified_on = api_client.QueryParameter(
    name="modified_on",
    style=api_client.ParameterStyle.FORM,
    schema=ModifiedOnSchema,
    explode=True,
)
request_query_modified_at_before = api_client.QueryParameter(
    name="modified_at.before",
    style=api_client.ParameterStyle.FORM,
    schema=ModifiedAtBeforeSchema,
    explode=True,
)
request_query_modified_at_after = api_client.QueryParameter(
    name="modified_at.after",
    style=api_client.ParameterStyle.FORM,
    schema=ModifiedAtAfterSchema,
    explode=True,
)
request_query_is_blocking = api_client.QueryParameter(
    name="is_blocking",
    style=api_client.ParameterStyle.FORM,
    schema=IsBlockingSchema,
    explode=True,
)
request_query_is_blocked = api_client.QueryParameter(
    name="is_blocked",
    style=api_client.ParameterStyle.FORM,
    schema=IsBlockedSchema,
    explode=True,
)
request_query_has_attachment = api_client.QueryParameter(
    name="has_attachment",
    style=api_client.ParameterStyle.FORM,
    schema=HasAttachmentSchema,
    explode=True,
)
request_query_completed = api_client.QueryParameter(
    name="completed",
    style=api_client.ParameterStyle.FORM,
    schema=CompletedSchema,
    explode=True,
)
request_query_is_subtask = api_client.QueryParameter(
    name="is_subtask",
    style=api_client.ParameterStyle.FORM,
    schema=IsSubtaskSchema,
    explode=True,
)
request_query_sort_by = api_client.QueryParameter(
    name="sort_by",
    style=api_client.ParameterStyle.FORM,
    schema=SortBySchema,
    explode=True,
)
request_query_sort_ascending = api_client.QueryParameter(
    name="sort_ascending",
    style=api_client.ParameterStyle.FORM,
    schema=SortAscendingSchema,
    explode=True,
)
# Path params
WorkspaceGidSchema = schemas.StrSchema
RequestRequiredPathParams = typing_extensions.TypedDict(
    'RequestRequiredPathParams',
    {
        'workspace_gid': typing.Union[WorkspaceGidSchema, str, ],
    }
)
RequestOptionalPathParams = typing_extensions.TypedDict(
    'RequestOptionalPathParams',
    {
    },
    total=False
)


class RequestPathParams(RequestRequiredPathParams, RequestOptionalPathParams):
    pass


request_path_workspace_gid = api_client.PathParameter(
    name="workspace_gid",
    style=api_client.ParameterStyle.SIMPLE,
    schema=WorkspaceGidSchema,
    required=True,
)


class SchemaFor200ResponseBodyApplicationJson(
    schemas.DictSchema
):


    class MetaOapg:
        
        class properties:
            
            
            class data(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['TaskCompact']:
                        return TaskCompact
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['TaskCompact'], typing.List['TaskCompact']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'data':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'TaskCompact':
                    return super().__getitem__(i)
            __annotations__ = {
                "data": data,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["data"]) -> MetaOapg.properties.data: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["data"]) -> typing.Union[MetaOapg.properties.data, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["data", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        data: typing.Union[MetaOapg.properties.data, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SchemaFor200ResponseBodyApplicationJson':
        return super().__new__(
            cls,
            *args,
            data=data,
            _configuration=_configuration,
            **kwargs,
        )


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor200ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
SchemaFor400ResponseBodyApplicationJson = ErrorResponse


@dataclass
class ApiResponseFor400(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor400ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_400 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor400,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor400ResponseBodyApplicationJson),
    },
)
SchemaFor401ResponseBodyApplicationJson = ErrorResponse


@dataclass
class ApiResponseFor401(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor401ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_401 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor401,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor401ResponseBodyApplicationJson),
    },
)
SchemaFor403ResponseBodyApplicationJson = ErrorResponse


@dataclass
class ApiResponseFor403(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor403ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_403 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor403,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor403ResponseBodyApplicationJson),
    },
)
SchemaFor404ResponseBodyApplicationJson = ErrorResponse


@dataclass
class ApiResponseFor404(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor404ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_404 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor404,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor404ResponseBodyApplicationJson),
    },
)
SchemaFor500ResponseBodyApplicationJson = ErrorResponse


@dataclass
class ApiResponseFor500(api_client.ApiResponse):
    response: urllib3.HTTPResponse
    body: typing.Union[
        SchemaFor500ResponseBodyApplicationJson,
    ]
    headers: schemas.Unset = schemas.unset


_response_for_500 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor500,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor500ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):
    @typing.overload
    def _search_tasks_for_workspace_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def _search_tasks_for_workspace_oapg(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def _search_tasks_for_workspace_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def _search_tasks_for_workspace_oapg(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        """
        Search tasks in a workspace
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        self._verify_typed_dict_inputs_oapg(RequestPathParams, path_params)
        used_path = path.value

        _path_params = {}
        for parameter in (
            request_path_workspace_gid,
        ):
            parameter_data = path_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            serialized_data = parameter.serialize(parameter_data)
            _path_params.update(serialized_data)

        for k, v in _path_params.items():
            used_path = used_path.replace('{%s}' % k, v)

        prefix_separator_iterator = None
        for parameter in (
            request_query_opt_pretty,
            request_query_opt_fields,
            request_query_text,
            request_query_resource_subtype,
            request_query_assignee_any,
            request_query_assignee_not,
            request_query_portfolios_any,
            request_query_projects_any,
            request_query_projects_not,
            request_query_projects_all,
            request_query_sections_any,
            request_query_sections_not,
            request_query_sections_all,
            request_query_tags_any,
            request_query_tags_not,
            request_query_tags_all,
            request_query_teams_any,
            request_query_followers_not,
            request_query_created_by_any,
            request_query_created_by_not,
            request_query_assigned_by_any,
            request_query_assigned_by_not,
            request_query_liked_by_not,
            request_query_commented_on_by_not,
            request_query_due_on_before,
            request_query_due_on_after,
            request_query_due_on,
            request_query_due_at_before,
            request_query_due_at_after,
            request_query_start_on_before,
            request_query_start_on_after,
            request_query_start_on,
            request_query_created_on_before,
            request_query_created_on_after,
            request_query_created_on,
            request_query_created_at_before,
            request_query_created_at_after,
            request_query_completed_on_before,
            request_query_completed_on_after,
            request_query_completed_on,
            request_query_completed_at_before,
            request_query_completed_at_after,
            request_query_modified_on_before,
            request_query_modified_on_after,
            request_query_modified_on,
            request_query_modified_at_before,
            request_query_modified_at_after,
            request_query_is_blocking,
            request_query_is_blocked,
            request_query_has_attachment,
            request_query_completed,
            request_query_is_subtask,
            request_query_sort_by,
            request_query_sort_ascending,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value

        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)

        response = self.api_client.call_api(
            resource_path=used_path,
            method='get'.upper(),
            headers=_headers,
            auth_settings=_auth,
            stream=stream,
            timeout=timeout,
        )

        if skip_deserialization:
            api_response = api_client.ApiResponseWithoutDeserialization(response=response)
        else:
            response_for_status = _status_code_to_response.get(str(response.status))
            if response_for_status:
                api_response = response_for_status.deserialize(response, self.api_client.configuration)
            else:
                api_response = api_client.ApiResponseWithoutDeserialization(response=response)

        if not 200 <= response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)

        return api_response


class SearchTasksForWorkspace(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    @typing.overload
    def search_tasks_for_workspace(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def search_tasks_for_workspace(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def search_tasks_for_workspace(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def search_tasks_for_workspace(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._search_tasks_for_workspace_oapg(
            query_params=query_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: typing_extensions.Literal[False] = ...,
    ) -> typing.Union[
        ApiResponseFor200,
    ]: ...

    @typing.overload
    def get(
        self,
        skip_deserialization: typing_extensions.Literal[True],
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
    ) -> api_client.ApiResponseWithoutDeserialization: ...

    @typing.overload
    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = ...,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]: ...

    def get(
        self,
        query_params: RequestQueryParams = frozendict.frozendict(),
        path_params: RequestPathParams = frozendict.frozendict(),
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        timeout: typing.Optional[typing.Union[int, typing.Tuple]] = None,
        skip_deserialization: bool = False,
    ):
        return self._search_tasks_for_workspace_oapg(
            query_params=query_params,
            path_params=path_params,
            accept_content_types=accept_content_types,
            stream=stream,
            timeout=timeout,
            skip_deserialization=skip_deserialization
        )


