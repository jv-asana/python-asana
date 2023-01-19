import typing_extensions

from asana.apis.tags import TagValues
from asana.apis.tags.attachments_api import AttachmentsApi
from asana.apis.tags.audit_log_api_api import AuditLogAPIApi
from asana.apis.tags.batch_api_api import BatchAPIApi
from asana.apis.tags.custom_fields_api import CustomFieldsApi
from asana.apis.tags.custom_field_settings_api import CustomFieldSettingsApi
from asana.apis.tags.events_api import EventsApi
from asana.apis.tags.goals_api import GoalsApi
from asana.apis.tags.goal_relationships_api import GoalRelationshipsApi
from asana.apis.tags.jobs_api import JobsApi
from asana.apis.tags.organization_exports_api import OrganizationExportsApi
from asana.apis.tags.portfolios_api import PortfoliosApi
from asana.apis.tags.portfolio_memberships_api import PortfolioMembershipsApi
from asana.apis.tags.projects_api import ProjectsApi
from asana.apis.tags.project_briefs_api import ProjectBriefsApi
from asana.apis.tags.project_memberships_api import ProjectMembershipsApi
from asana.apis.tags.project_statuses_api import ProjectStatusesApi
from asana.apis.tags.project_templates_api import ProjectTemplatesApi
from asana.apis.tags.sections_api import SectionsApi
from asana.apis.tags.status_updates_api import StatusUpdatesApi
from asana.apis.tags.stories_api import StoriesApi
from asana.apis.tags.tags_api import TagsApi
from asana.apis.tags.tasks_api import TasksApi
from asana.apis.tags.teams_api import TeamsApi
from asana.apis.tags.team_memberships_api import TeamMembershipsApi
from asana.apis.tags.time_periods_api import TimePeriodsApi
from asana.apis.tags.typeahead_api import TypeaheadApi
from asana.apis.tags.users_api import UsersApi
from asana.apis.tags.user_task_lists_api import UserTaskListsApi
from asana.apis.tags.webhooks_api import WebhooksApi
from asana.apis.tags.workspaces_api import WorkspacesApi
from asana.apis.tags.workspace_memberships_api import WorkspaceMembershipsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.AUDIT_LOG_API: AuditLogAPIApi,
        TagValues.BATCH_API: BatchAPIApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.CUSTOM_FIELD_SETTINGS: CustomFieldSettingsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.GOALS: GoalsApi,
        TagValues.GOAL_RELATIONSHIPS: GoalRelationshipsApi,
        TagValues.JOBS: JobsApi,
        TagValues.ORGANIZATION_EXPORTS: OrganizationExportsApi,
        TagValues.PORTFOLIOS: PortfoliosApi,
        TagValues.PORTFOLIO_MEMBERSHIPS: PortfolioMembershipsApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.PROJECT_BRIEFS: ProjectBriefsApi,
        TagValues.PROJECT_MEMBERSHIPS: ProjectMembershipsApi,
        TagValues.PROJECT_STATUSES: ProjectStatusesApi,
        TagValues.PROJECT_TEMPLATES: ProjectTemplatesApi,
        TagValues.SECTIONS: SectionsApi,
        TagValues.STATUS_UPDATES: StatusUpdatesApi,
        TagValues.STORIES: StoriesApi,
        TagValues.TAGS: TagsApi,
        TagValues.TASKS: TasksApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.TEAM_MEMBERSHIPS: TeamMembershipsApi,
        TagValues.TIME_PERIODS: TimePeriodsApi,
        TagValues.TYPEAHEAD: TypeaheadApi,
        TagValues.USERS: UsersApi,
        TagValues.USER_TASK_LISTS: UserTaskListsApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.WORKSPACES: WorkspacesApi,
        TagValues.WORKSPACE_MEMBERSHIPS: WorkspaceMembershipsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.ATTACHMENTS: AttachmentsApi,
        TagValues.AUDIT_LOG_API: AuditLogAPIApi,
        TagValues.BATCH_API: BatchAPIApi,
        TagValues.CUSTOM_FIELDS: CustomFieldsApi,
        TagValues.CUSTOM_FIELD_SETTINGS: CustomFieldSettingsApi,
        TagValues.EVENTS: EventsApi,
        TagValues.GOALS: GoalsApi,
        TagValues.GOAL_RELATIONSHIPS: GoalRelationshipsApi,
        TagValues.JOBS: JobsApi,
        TagValues.ORGANIZATION_EXPORTS: OrganizationExportsApi,
        TagValues.PORTFOLIOS: PortfoliosApi,
        TagValues.PORTFOLIO_MEMBERSHIPS: PortfolioMembershipsApi,
        TagValues.PROJECTS: ProjectsApi,
        TagValues.PROJECT_BRIEFS: ProjectBriefsApi,
        TagValues.PROJECT_MEMBERSHIPS: ProjectMembershipsApi,
        TagValues.PROJECT_STATUSES: ProjectStatusesApi,
        TagValues.PROJECT_TEMPLATES: ProjectTemplatesApi,
        TagValues.SECTIONS: SectionsApi,
        TagValues.STATUS_UPDATES: StatusUpdatesApi,
        TagValues.STORIES: StoriesApi,
        TagValues.TAGS: TagsApi,
        TagValues.TASKS: TasksApi,
        TagValues.TEAMS: TeamsApi,
        TagValues.TEAM_MEMBERSHIPS: TeamMembershipsApi,
        TagValues.TIME_PERIODS: TimePeriodsApi,
        TagValues.TYPEAHEAD: TypeaheadApi,
        TagValues.USERS: UsersApi,
        TagValues.USER_TASK_LISTS: UserTaskListsApi,
        TagValues.WEBHOOKS: WebhooksApi,
        TagValues.WORKSPACES: WorkspacesApi,
        TagValues.WORKSPACE_MEMBERSHIPS: WorkspaceMembershipsApi,
    }
)
