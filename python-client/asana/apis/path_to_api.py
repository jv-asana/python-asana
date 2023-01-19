import typing_extensions

from asana.paths import PathValues
from asana.apis.paths.attachments_attachment_gid import AttachmentsAttachmentGid
from asana.apis.paths.attachments import Attachments
from asana.apis.paths.workspaces_workspace_gid_audit_log_events import WorkspacesWorkspaceGidAuditLogEvents
from asana.apis.paths.batch import Batch
from asana.apis.paths.projects_project_gid_custom_field_settings import ProjectsProjectGidCustomFieldSettings
from asana.apis.paths.portfolios_portfolio_gid_custom_field_settings import PortfoliosPortfolioGidCustomFieldSettings
from asana.apis.paths.custom_fields import CustomFields
from asana.apis.paths.custom_fields_custom_field_gid import CustomFieldsCustomFieldGid
from asana.apis.paths.workspaces_workspace_gid_custom_fields import WorkspacesWorkspaceGidCustomFields
from asana.apis.paths.custom_fields_custom_field_gid_enum_options import CustomFieldsCustomFieldGidEnumOptions
from asana.apis.paths.custom_fields_custom_field_gid_enum_options_insert import CustomFieldsCustomFieldGidEnumOptionsInsert
from asana.apis.paths.enum_options_enum_option_gid import EnumOptionsEnumOptionGid
from asana.apis.paths.events import Events
from asana.apis.paths.goal_relationships_goal_relationship_gid import GoalRelationshipsGoalRelationshipGid
from asana.apis.paths.goal_relationships import GoalRelationships
from asana.apis.paths.goals_goal_gid_add_supporting_relationship import GoalsGoalGidAddSupportingRelationship
from asana.apis.paths.goals_goal_gid_remove_supporting_relationship import GoalsGoalGidRemoveSupportingRelationship
from asana.apis.paths.goals_goal_gid import GoalsGoalGid
from asana.apis.paths.goals import Goals
from asana.apis.paths.goals_goal_gid_set_metric import GoalsGoalGidSetMetric
from asana.apis.paths.goals_goal_gid_set_metric_current_value import GoalsGoalGidSetMetricCurrentValue
from asana.apis.paths.goals_goal_gid_add_followers import GoalsGoalGidAddFollowers
from asana.apis.paths.goals_goal_gid_remove_followers import GoalsGoalGidRemoveFollowers
from asana.apis.paths.goals_goal_gid_parent_goals import GoalsGoalGidParentGoals
from asana.apis.paths.jobs_job_gid import JobsJobGid
from asana.apis.paths.organization_exports import OrganizationExports
from asana.apis.paths.organization_exports_organization_export_gid import OrganizationExportsOrganizationExportGid
from asana.apis.paths.portfolio_memberships import PortfolioMemberships
from asana.apis.paths.portfolio_memberships_portfolio_membership_gid import PortfolioMembershipsPortfolioMembershipGid
from asana.apis.paths.portfolios_portfolio_gid_portfolio_memberships import PortfoliosPortfolioGidPortfolioMemberships
from asana.apis.paths.portfolios import Portfolios
from asana.apis.paths.portfolios_portfolio_gid import PortfoliosPortfolioGid
from asana.apis.paths.portfolios_portfolio_gid_items import PortfoliosPortfolioGidItems
from asana.apis.paths.portfolios_portfolio_gid_add_item import PortfoliosPortfolioGidAddItem
from asana.apis.paths.portfolios_portfolio_gid_remove_item import PortfoliosPortfolioGidRemoveItem
from asana.apis.paths.portfolios_portfolio_gid_add_custom_field_setting import PortfoliosPortfolioGidAddCustomFieldSetting
from asana.apis.paths.portfolios_portfolio_gid_remove_custom_field_setting import PortfoliosPortfolioGidRemoveCustomFieldSetting
from asana.apis.paths.portfolios_portfolio_gid_add_members import PortfoliosPortfolioGidAddMembers
from asana.apis.paths.portfolios_portfolio_gid_remove_members import PortfoliosPortfolioGidRemoveMembers
from asana.apis.paths.project_briefs_project_brief_gid import ProjectBriefsProjectBriefGid
from asana.apis.paths.projects_project_gid_project_briefs import ProjectsProjectGidProjectBriefs
from asana.apis.paths.project_memberships_project_membership_gid import ProjectMembershipsProjectMembershipGid
from asana.apis.paths.projects_project_gid_project_memberships import ProjectsProjectGidProjectMemberships
from asana.apis.paths.project_statuses_project_status_gid import ProjectStatusesProjectStatusGid
from asana.apis.paths.projects_project_gid_project_statuses import ProjectsProjectGidProjectStatuses
from asana.apis.paths.project_templates_project_template_gid import ProjectTemplatesProjectTemplateGid
from asana.apis.paths.project_templates import ProjectTemplates
from asana.apis.paths.teams_team_gid_project_templates import TeamsTeamGidProjectTemplates
from asana.apis.paths.project_templates_project_template_gid_instantiate_project import ProjectTemplatesProjectTemplateGidInstantiateProject
from asana.apis.paths.projects import Projects
from asana.apis.paths.projects_project_gid import ProjectsProjectGid
from asana.apis.paths.projects_project_gid_duplicate import ProjectsProjectGidDuplicate
from asana.apis.paths.tasks_task_gid_projects import TasksTaskGidProjects
from asana.apis.paths.teams_team_gid_projects import TeamsTeamGidProjects
from asana.apis.paths.workspaces_workspace_gid_projects import WorkspacesWorkspaceGidProjects
from asana.apis.paths.projects_project_gid_add_custom_field_setting import ProjectsProjectGidAddCustomFieldSetting
from asana.apis.paths.projects_project_gid_remove_custom_field_setting import ProjectsProjectGidRemoveCustomFieldSetting
from asana.apis.paths.projects_project_gid_task_counts import ProjectsProjectGidTaskCounts
from asana.apis.paths.projects_project_gid_add_members import ProjectsProjectGidAddMembers
from asana.apis.paths.projects_project_gid_remove_members import ProjectsProjectGidRemoveMembers
from asana.apis.paths.projects_project_gid_add_followers import ProjectsProjectGidAddFollowers
from asana.apis.paths.projects_project_gid_remove_followers import ProjectsProjectGidRemoveFollowers
from asana.apis.paths.projects_project_gid_save_as_template import ProjectsProjectGidSaveAsTemplate
from asana.apis.paths.sections_section_gid import SectionsSectionGid
from asana.apis.paths.projects_project_gid_sections import ProjectsProjectGidSections
from asana.apis.paths.sections_section_gid_add_task import SectionsSectionGidAddTask
from asana.apis.paths.projects_project_gid_sections_insert import ProjectsProjectGidSectionsInsert
from asana.apis.paths.status_updates_status_gid import StatusUpdatesStatusGid
from asana.apis.paths.status_updates import StatusUpdates
from asana.apis.paths.stories_story_gid import StoriesStoryGid
from asana.apis.paths.tasks_task_gid_stories import TasksTaskGidStories
from asana.apis.paths.tags import Tags
from asana.apis.paths.tags_tag_gid import TagsTagGid
from asana.apis.paths.tasks_task_gid_tags import TasksTaskGidTags
from asana.apis.paths.workspaces_workspace_gid_tags import WorkspacesWorkspaceGidTags
from asana.apis.paths.tasks import Tasks
from asana.apis.paths.tasks_task_gid import TasksTaskGid
from asana.apis.paths.tasks_task_gid_duplicate import TasksTaskGidDuplicate
from asana.apis.paths.projects_project_gid_tasks import ProjectsProjectGidTasks
from asana.apis.paths.sections_section_gid_tasks import SectionsSectionGidTasks
from asana.apis.paths.tags_tag_gid_tasks import TagsTagGidTasks
from asana.apis.paths.user_task_lists_user_task_list_gid_tasks import UserTaskListsUserTaskListGidTasks
from asana.apis.paths.tasks_task_gid_subtasks import TasksTaskGidSubtasks
from asana.apis.paths.tasks_task_gid_set_parent import TasksTaskGidSetParent
from asana.apis.paths.tasks_task_gid_dependencies import TasksTaskGidDependencies
from asana.apis.paths.tasks_task_gid_add_dependencies import TasksTaskGidAddDependencies
from asana.apis.paths.tasks_task_gid_remove_dependencies import TasksTaskGidRemoveDependencies
from asana.apis.paths.tasks_task_gid_dependents import TasksTaskGidDependents
from asana.apis.paths.tasks_task_gid_add_dependents import TasksTaskGidAddDependents
from asana.apis.paths.tasks_task_gid_remove_dependents import TasksTaskGidRemoveDependents
from asana.apis.paths.tasks_task_gid_add_project import TasksTaskGidAddProject
from asana.apis.paths.tasks_task_gid_remove_project import TasksTaskGidRemoveProject
from asana.apis.paths.tasks_task_gid_add_tag import TasksTaskGidAddTag
from asana.apis.paths.tasks_task_gid_remove_tag import TasksTaskGidRemoveTag
from asana.apis.paths.tasks_task_gid_add_followers import TasksTaskGidAddFollowers
from asana.apis.paths.tasks_task_gid_remove_followers import TasksTaskGidRemoveFollowers
from asana.apis.paths.workspaces_workspace_gid_tasks_search import WorkspacesWorkspaceGidTasksSearch
from asana.apis.paths.team_memberships_team_membership_gid import TeamMembershipsTeamMembershipGid
from asana.apis.paths.team_memberships import TeamMemberships
from asana.apis.paths.teams_team_gid_team_memberships import TeamsTeamGidTeamMemberships
from asana.apis.paths.users_user_gid_team_memberships import UsersUserGidTeamMemberships
from asana.apis.paths.teams import Teams
from asana.apis.paths.teams_team_gid import TeamsTeamGid
from asana.apis.paths.workspaces_workspace_gid_teams import WorkspacesWorkspaceGidTeams
from asana.apis.paths.users_user_gid_teams import UsersUserGidTeams
from asana.apis.paths.teams_team_gid_add_user import TeamsTeamGidAddUser
from asana.apis.paths.teams_team_gid_remove_user import TeamsTeamGidRemoveUser
from asana.apis.paths.time_periods_time_period_gid import TimePeriodsTimePeriodGid
from asana.apis.paths.time_periods import TimePeriods
from asana.apis.paths.workspaces_workspace_gid_typeahead import WorkspacesWorkspaceGidTypeahead
from asana.apis.paths.user_task_lists_user_task_list_gid import UserTaskListsUserTaskListGid
from asana.apis.paths.users_user_gid_user_task_list import UsersUserGidUserTaskList
from asana.apis.paths.users import Users
from asana.apis.paths.users_user_gid import UsersUserGid
from asana.apis.paths.users_user_gid_favorites import UsersUserGidFavorites
from asana.apis.paths.teams_team_gid_users import TeamsTeamGidUsers
from asana.apis.paths.workspaces_workspace_gid_users import WorkspacesWorkspaceGidUsers
from asana.apis.paths.webhooks import Webhooks
from asana.apis.paths.webhooks_webhook_gid import WebhooksWebhookGid
from asana.apis.paths.workspace_memberships_workspace_membership_gid import WorkspaceMembershipsWorkspaceMembershipGid
from asana.apis.paths.users_user_gid_workspace_memberships import UsersUserGidWorkspaceMemberships
from asana.apis.paths.workspaces_workspace_gid_workspace_memberships import WorkspacesWorkspaceGidWorkspaceMemberships
from asana.apis.paths.workspaces import Workspaces
from asana.apis.paths.workspaces_workspace_gid import WorkspacesWorkspaceGid
from asana.apis.paths.workspaces_workspace_gid_add_user import WorkspacesWorkspaceGidAddUser
from asana.apis.paths.workspaces_workspace_gid_remove_user import WorkspacesWorkspaceGidRemoveUser

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.ATTACHMENTS_ATTACHMENT_GID: AttachmentsAttachmentGid,
        PathValues.ATTACHMENTS: Attachments,
        PathValues.WORKSPACES_WORKSPACE_GID_AUDIT_LOG_EVENTS: WorkspacesWorkspaceGidAuditLogEvents,
        PathValues.BATCH: Batch,
        PathValues.PROJECTS_PROJECT_GID_CUSTOM_FIELD_SETTINGS: ProjectsProjectGidCustomFieldSettings,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_CUSTOM_FIELD_SETTINGS: PortfoliosPortfolioGidCustomFieldSettings,
        PathValues.CUSTOM_FIELDS: CustomFields,
        PathValues.CUSTOM_FIELDS_CUSTOM_FIELD_GID: CustomFieldsCustomFieldGid,
        PathValues.WORKSPACES_WORKSPACE_GID_CUSTOM_FIELDS: WorkspacesWorkspaceGidCustomFields,
        PathValues.CUSTOM_FIELDS_CUSTOM_FIELD_GID_ENUM_OPTIONS: CustomFieldsCustomFieldGidEnumOptions,
        PathValues.CUSTOM_FIELDS_CUSTOM_FIELD_GID_ENUM_OPTIONS_INSERT: CustomFieldsCustomFieldGidEnumOptionsInsert,
        PathValues.ENUM_OPTIONS_ENUM_OPTION_GID: EnumOptionsEnumOptionGid,
        PathValues.EVENTS: Events,
        PathValues.GOAL_RELATIONSHIPS_GOAL_RELATIONSHIP_GID: GoalRelationshipsGoalRelationshipGid,
        PathValues.GOAL_RELATIONSHIPS: GoalRelationships,
        PathValues.GOALS_GOAL_GID_ADD_SUPPORTING_RELATIONSHIP: GoalsGoalGidAddSupportingRelationship,
        PathValues.GOALS_GOAL_GID_REMOVE_SUPPORTING_RELATIONSHIP: GoalsGoalGidRemoveSupportingRelationship,
        PathValues.GOALS_GOAL_GID: GoalsGoalGid,
        PathValues.GOALS: Goals,
        PathValues.GOALS_GOAL_GID_SET_METRIC: GoalsGoalGidSetMetric,
        PathValues.GOALS_GOAL_GID_SET_METRIC_CURRENT_VALUE: GoalsGoalGidSetMetricCurrentValue,
        PathValues.GOALS_GOAL_GID_ADD_FOLLOWERS: GoalsGoalGidAddFollowers,
        PathValues.GOALS_GOAL_GID_REMOVE_FOLLOWERS: GoalsGoalGidRemoveFollowers,
        PathValues.GOALS_GOAL_GID_PARENT_GOALS: GoalsGoalGidParentGoals,
        PathValues.JOBS_JOB_GID: JobsJobGid,
        PathValues.ORGANIZATION_EXPORTS: OrganizationExports,
        PathValues.ORGANIZATION_EXPORTS_ORGANIZATION_EXPORT_GID: OrganizationExportsOrganizationExportGid,
        PathValues.PORTFOLIO_MEMBERSHIPS: PortfolioMemberships,
        PathValues.PORTFOLIO_MEMBERSHIPS_PORTFOLIO_MEMBERSHIP_GID: PortfolioMembershipsPortfolioMembershipGid,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_PORTFOLIO_MEMBERSHIPS: PortfoliosPortfolioGidPortfolioMemberships,
        PathValues.PORTFOLIOS: Portfolios,
        PathValues.PORTFOLIOS_PORTFOLIO_GID: PortfoliosPortfolioGid,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_ITEMS: PortfoliosPortfolioGidItems,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_ADD_ITEM: PortfoliosPortfolioGidAddItem,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_REMOVE_ITEM: PortfoliosPortfolioGidRemoveItem,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_ADD_CUSTOM_FIELD_SETTING: PortfoliosPortfolioGidAddCustomFieldSetting,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_REMOVE_CUSTOM_FIELD_SETTING: PortfoliosPortfolioGidRemoveCustomFieldSetting,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_ADD_MEMBERS: PortfoliosPortfolioGidAddMembers,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_REMOVE_MEMBERS: PortfoliosPortfolioGidRemoveMembers,
        PathValues.PROJECT_BRIEFS_PROJECT_BRIEF_GID: ProjectBriefsProjectBriefGid,
        PathValues.PROJECTS_PROJECT_GID_PROJECT_BRIEFS: ProjectsProjectGidProjectBriefs,
        PathValues.PROJECT_MEMBERSHIPS_PROJECT_MEMBERSHIP_GID: ProjectMembershipsProjectMembershipGid,
        PathValues.PROJECTS_PROJECT_GID_PROJECT_MEMBERSHIPS: ProjectsProjectGidProjectMemberships,
        PathValues.PROJECT_STATUSES_PROJECT_STATUS_GID: ProjectStatusesProjectStatusGid,
        PathValues.PROJECTS_PROJECT_GID_PROJECT_STATUSES: ProjectsProjectGidProjectStatuses,
        PathValues.PROJECT_TEMPLATES_PROJECT_TEMPLATE_GID: ProjectTemplatesProjectTemplateGid,
        PathValues.PROJECT_TEMPLATES: ProjectTemplates,
        PathValues.TEAMS_TEAM_GID_PROJECT_TEMPLATES: TeamsTeamGidProjectTemplates,
        PathValues.PROJECT_TEMPLATES_PROJECT_TEMPLATE_GID_INSTANTIATE_PROJECT: ProjectTemplatesProjectTemplateGidInstantiateProject,
        PathValues.PROJECTS: Projects,
        PathValues.PROJECTS_PROJECT_GID: ProjectsProjectGid,
        PathValues.PROJECTS_PROJECT_GID_DUPLICATE: ProjectsProjectGidDuplicate,
        PathValues.TASKS_TASK_GID_PROJECTS: TasksTaskGidProjects,
        PathValues.TEAMS_TEAM_GID_PROJECTS: TeamsTeamGidProjects,
        PathValues.WORKSPACES_WORKSPACE_GID_PROJECTS: WorkspacesWorkspaceGidProjects,
        PathValues.PROJECTS_PROJECT_GID_ADD_CUSTOM_FIELD_SETTING: ProjectsProjectGidAddCustomFieldSetting,
        PathValues.PROJECTS_PROJECT_GID_REMOVE_CUSTOM_FIELD_SETTING: ProjectsProjectGidRemoveCustomFieldSetting,
        PathValues.PROJECTS_PROJECT_GID_TASK_COUNTS: ProjectsProjectGidTaskCounts,
        PathValues.PROJECTS_PROJECT_GID_ADD_MEMBERS: ProjectsProjectGidAddMembers,
        PathValues.PROJECTS_PROJECT_GID_REMOVE_MEMBERS: ProjectsProjectGidRemoveMembers,
        PathValues.PROJECTS_PROJECT_GID_ADD_FOLLOWERS: ProjectsProjectGidAddFollowers,
        PathValues.PROJECTS_PROJECT_GID_REMOVE_FOLLOWERS: ProjectsProjectGidRemoveFollowers,
        PathValues.PROJECTS_PROJECT_GID_SAVE_AS_TEMPLATE: ProjectsProjectGidSaveAsTemplate,
        PathValues.SECTIONS_SECTION_GID: SectionsSectionGid,
        PathValues.PROJECTS_PROJECT_GID_SECTIONS: ProjectsProjectGidSections,
        PathValues.SECTIONS_SECTION_GID_ADD_TASK: SectionsSectionGidAddTask,
        PathValues.PROJECTS_PROJECT_GID_SECTIONS_INSERT: ProjectsProjectGidSectionsInsert,
        PathValues.STATUS_UPDATES_STATUS_GID: StatusUpdatesStatusGid,
        PathValues.STATUS_UPDATES: StatusUpdates,
        PathValues.STORIES_STORY_GID: StoriesStoryGid,
        PathValues.TASKS_TASK_GID_STORIES: TasksTaskGidStories,
        PathValues.TAGS: Tags,
        PathValues.TAGS_TAG_GID: TagsTagGid,
        PathValues.TASKS_TASK_GID_TAGS: TasksTaskGidTags,
        PathValues.WORKSPACES_WORKSPACE_GID_TAGS: WorkspacesWorkspaceGidTags,
        PathValues.TASKS: Tasks,
        PathValues.TASKS_TASK_GID: TasksTaskGid,
        PathValues.TASKS_TASK_GID_DUPLICATE: TasksTaskGidDuplicate,
        PathValues.PROJECTS_PROJECT_GID_TASKS: ProjectsProjectGidTasks,
        PathValues.SECTIONS_SECTION_GID_TASKS: SectionsSectionGidTasks,
        PathValues.TAGS_TAG_GID_TASKS: TagsTagGidTasks,
        PathValues.USER_TASK_LISTS_USER_TASK_LIST_GID_TASKS: UserTaskListsUserTaskListGidTasks,
        PathValues.TASKS_TASK_GID_SUBTASKS: TasksTaskGidSubtasks,
        PathValues.TASKS_TASK_GID_SET_PARENT: TasksTaskGidSetParent,
        PathValues.TASKS_TASK_GID_DEPENDENCIES: TasksTaskGidDependencies,
        PathValues.TASKS_TASK_GID_ADD_DEPENDENCIES: TasksTaskGidAddDependencies,
        PathValues.TASKS_TASK_GID_REMOVE_DEPENDENCIES: TasksTaskGidRemoveDependencies,
        PathValues.TASKS_TASK_GID_DEPENDENTS: TasksTaskGidDependents,
        PathValues.TASKS_TASK_GID_ADD_DEPENDENTS: TasksTaskGidAddDependents,
        PathValues.TASKS_TASK_GID_REMOVE_DEPENDENTS: TasksTaskGidRemoveDependents,
        PathValues.TASKS_TASK_GID_ADD_PROJECT: TasksTaskGidAddProject,
        PathValues.TASKS_TASK_GID_REMOVE_PROJECT: TasksTaskGidRemoveProject,
        PathValues.TASKS_TASK_GID_ADD_TAG: TasksTaskGidAddTag,
        PathValues.TASKS_TASK_GID_REMOVE_TAG: TasksTaskGidRemoveTag,
        PathValues.TASKS_TASK_GID_ADD_FOLLOWERS: TasksTaskGidAddFollowers,
        PathValues.TASKS_TASK_GID_REMOVE_FOLLOWERS: TasksTaskGidRemoveFollowers,
        PathValues.WORKSPACES_WORKSPACE_GID_TASKS_SEARCH: WorkspacesWorkspaceGidTasksSearch,
        PathValues.TEAM_MEMBERSHIPS_TEAM_MEMBERSHIP_GID: TeamMembershipsTeamMembershipGid,
        PathValues.TEAM_MEMBERSHIPS: TeamMemberships,
        PathValues.TEAMS_TEAM_GID_TEAM_MEMBERSHIPS: TeamsTeamGidTeamMemberships,
        PathValues.USERS_USER_GID_TEAM_MEMBERSHIPS: UsersUserGidTeamMemberships,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_TEAM_GID: TeamsTeamGid,
        PathValues.WORKSPACES_WORKSPACE_GID_TEAMS: WorkspacesWorkspaceGidTeams,
        PathValues.USERS_USER_GID_TEAMS: UsersUserGidTeams,
        PathValues.TEAMS_TEAM_GID_ADD_USER: TeamsTeamGidAddUser,
        PathValues.TEAMS_TEAM_GID_REMOVE_USER: TeamsTeamGidRemoveUser,
        PathValues.TIME_PERIODS_TIME_PERIOD_GID: TimePeriodsTimePeriodGid,
        PathValues.TIME_PERIODS: TimePeriods,
        PathValues.WORKSPACES_WORKSPACE_GID_TYPEAHEAD: WorkspacesWorkspaceGidTypeahead,
        PathValues.USER_TASK_LISTS_USER_TASK_LIST_GID: UserTaskListsUserTaskListGid,
        PathValues.USERS_USER_GID_USER_TASK_LIST: UsersUserGidUserTaskList,
        PathValues.USERS: Users,
        PathValues.USERS_USER_GID: UsersUserGid,
        PathValues.USERS_USER_GID_FAVORITES: UsersUserGidFavorites,
        PathValues.TEAMS_TEAM_GID_USERS: TeamsTeamGidUsers,
        PathValues.WORKSPACES_WORKSPACE_GID_USERS: WorkspacesWorkspaceGidUsers,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_WEBHOOK_GID: WebhooksWebhookGid,
        PathValues.WORKSPACE_MEMBERSHIPS_WORKSPACE_MEMBERSHIP_GID: WorkspaceMembershipsWorkspaceMembershipGid,
        PathValues.USERS_USER_GID_WORKSPACE_MEMBERSHIPS: UsersUserGidWorkspaceMemberships,
        PathValues.WORKSPACES_WORKSPACE_GID_WORKSPACE_MEMBERSHIPS: WorkspacesWorkspaceGidWorkspaceMemberships,
        PathValues.WORKSPACES: Workspaces,
        PathValues.WORKSPACES_WORKSPACE_GID: WorkspacesWorkspaceGid,
        PathValues.WORKSPACES_WORKSPACE_GID_ADD_USER: WorkspacesWorkspaceGidAddUser,
        PathValues.WORKSPACES_WORKSPACE_GID_REMOVE_USER: WorkspacesWorkspaceGidRemoveUser,
    }
)

path_to_api = PathToApi(
    {
        PathValues.ATTACHMENTS_ATTACHMENT_GID: AttachmentsAttachmentGid,
        PathValues.ATTACHMENTS: Attachments,
        PathValues.WORKSPACES_WORKSPACE_GID_AUDIT_LOG_EVENTS: WorkspacesWorkspaceGidAuditLogEvents,
        PathValues.BATCH: Batch,
        PathValues.PROJECTS_PROJECT_GID_CUSTOM_FIELD_SETTINGS: ProjectsProjectGidCustomFieldSettings,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_CUSTOM_FIELD_SETTINGS: PortfoliosPortfolioGidCustomFieldSettings,
        PathValues.CUSTOM_FIELDS: CustomFields,
        PathValues.CUSTOM_FIELDS_CUSTOM_FIELD_GID: CustomFieldsCustomFieldGid,
        PathValues.WORKSPACES_WORKSPACE_GID_CUSTOM_FIELDS: WorkspacesWorkspaceGidCustomFields,
        PathValues.CUSTOM_FIELDS_CUSTOM_FIELD_GID_ENUM_OPTIONS: CustomFieldsCustomFieldGidEnumOptions,
        PathValues.CUSTOM_FIELDS_CUSTOM_FIELD_GID_ENUM_OPTIONS_INSERT: CustomFieldsCustomFieldGidEnumOptionsInsert,
        PathValues.ENUM_OPTIONS_ENUM_OPTION_GID: EnumOptionsEnumOptionGid,
        PathValues.EVENTS: Events,
        PathValues.GOAL_RELATIONSHIPS_GOAL_RELATIONSHIP_GID: GoalRelationshipsGoalRelationshipGid,
        PathValues.GOAL_RELATIONSHIPS: GoalRelationships,
        PathValues.GOALS_GOAL_GID_ADD_SUPPORTING_RELATIONSHIP: GoalsGoalGidAddSupportingRelationship,
        PathValues.GOALS_GOAL_GID_REMOVE_SUPPORTING_RELATIONSHIP: GoalsGoalGidRemoveSupportingRelationship,
        PathValues.GOALS_GOAL_GID: GoalsGoalGid,
        PathValues.GOALS: Goals,
        PathValues.GOALS_GOAL_GID_SET_METRIC: GoalsGoalGidSetMetric,
        PathValues.GOALS_GOAL_GID_SET_METRIC_CURRENT_VALUE: GoalsGoalGidSetMetricCurrentValue,
        PathValues.GOALS_GOAL_GID_ADD_FOLLOWERS: GoalsGoalGidAddFollowers,
        PathValues.GOALS_GOAL_GID_REMOVE_FOLLOWERS: GoalsGoalGidRemoveFollowers,
        PathValues.GOALS_GOAL_GID_PARENT_GOALS: GoalsGoalGidParentGoals,
        PathValues.JOBS_JOB_GID: JobsJobGid,
        PathValues.ORGANIZATION_EXPORTS: OrganizationExports,
        PathValues.ORGANIZATION_EXPORTS_ORGANIZATION_EXPORT_GID: OrganizationExportsOrganizationExportGid,
        PathValues.PORTFOLIO_MEMBERSHIPS: PortfolioMemberships,
        PathValues.PORTFOLIO_MEMBERSHIPS_PORTFOLIO_MEMBERSHIP_GID: PortfolioMembershipsPortfolioMembershipGid,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_PORTFOLIO_MEMBERSHIPS: PortfoliosPortfolioGidPortfolioMemberships,
        PathValues.PORTFOLIOS: Portfolios,
        PathValues.PORTFOLIOS_PORTFOLIO_GID: PortfoliosPortfolioGid,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_ITEMS: PortfoliosPortfolioGidItems,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_ADD_ITEM: PortfoliosPortfolioGidAddItem,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_REMOVE_ITEM: PortfoliosPortfolioGidRemoveItem,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_ADD_CUSTOM_FIELD_SETTING: PortfoliosPortfolioGidAddCustomFieldSetting,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_REMOVE_CUSTOM_FIELD_SETTING: PortfoliosPortfolioGidRemoveCustomFieldSetting,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_ADD_MEMBERS: PortfoliosPortfolioGidAddMembers,
        PathValues.PORTFOLIOS_PORTFOLIO_GID_REMOVE_MEMBERS: PortfoliosPortfolioGidRemoveMembers,
        PathValues.PROJECT_BRIEFS_PROJECT_BRIEF_GID: ProjectBriefsProjectBriefGid,
        PathValues.PROJECTS_PROJECT_GID_PROJECT_BRIEFS: ProjectsProjectGidProjectBriefs,
        PathValues.PROJECT_MEMBERSHIPS_PROJECT_MEMBERSHIP_GID: ProjectMembershipsProjectMembershipGid,
        PathValues.PROJECTS_PROJECT_GID_PROJECT_MEMBERSHIPS: ProjectsProjectGidProjectMemberships,
        PathValues.PROJECT_STATUSES_PROJECT_STATUS_GID: ProjectStatusesProjectStatusGid,
        PathValues.PROJECTS_PROJECT_GID_PROJECT_STATUSES: ProjectsProjectGidProjectStatuses,
        PathValues.PROJECT_TEMPLATES_PROJECT_TEMPLATE_GID: ProjectTemplatesProjectTemplateGid,
        PathValues.PROJECT_TEMPLATES: ProjectTemplates,
        PathValues.TEAMS_TEAM_GID_PROJECT_TEMPLATES: TeamsTeamGidProjectTemplates,
        PathValues.PROJECT_TEMPLATES_PROJECT_TEMPLATE_GID_INSTANTIATE_PROJECT: ProjectTemplatesProjectTemplateGidInstantiateProject,
        PathValues.PROJECTS: Projects,
        PathValues.PROJECTS_PROJECT_GID: ProjectsProjectGid,
        PathValues.PROJECTS_PROJECT_GID_DUPLICATE: ProjectsProjectGidDuplicate,
        PathValues.TASKS_TASK_GID_PROJECTS: TasksTaskGidProjects,
        PathValues.TEAMS_TEAM_GID_PROJECTS: TeamsTeamGidProjects,
        PathValues.WORKSPACES_WORKSPACE_GID_PROJECTS: WorkspacesWorkspaceGidProjects,
        PathValues.PROJECTS_PROJECT_GID_ADD_CUSTOM_FIELD_SETTING: ProjectsProjectGidAddCustomFieldSetting,
        PathValues.PROJECTS_PROJECT_GID_REMOVE_CUSTOM_FIELD_SETTING: ProjectsProjectGidRemoveCustomFieldSetting,
        PathValues.PROJECTS_PROJECT_GID_TASK_COUNTS: ProjectsProjectGidTaskCounts,
        PathValues.PROJECTS_PROJECT_GID_ADD_MEMBERS: ProjectsProjectGidAddMembers,
        PathValues.PROJECTS_PROJECT_GID_REMOVE_MEMBERS: ProjectsProjectGidRemoveMembers,
        PathValues.PROJECTS_PROJECT_GID_ADD_FOLLOWERS: ProjectsProjectGidAddFollowers,
        PathValues.PROJECTS_PROJECT_GID_REMOVE_FOLLOWERS: ProjectsProjectGidRemoveFollowers,
        PathValues.PROJECTS_PROJECT_GID_SAVE_AS_TEMPLATE: ProjectsProjectGidSaveAsTemplate,
        PathValues.SECTIONS_SECTION_GID: SectionsSectionGid,
        PathValues.PROJECTS_PROJECT_GID_SECTIONS: ProjectsProjectGidSections,
        PathValues.SECTIONS_SECTION_GID_ADD_TASK: SectionsSectionGidAddTask,
        PathValues.PROJECTS_PROJECT_GID_SECTIONS_INSERT: ProjectsProjectGidSectionsInsert,
        PathValues.STATUS_UPDATES_STATUS_GID: StatusUpdatesStatusGid,
        PathValues.STATUS_UPDATES: StatusUpdates,
        PathValues.STORIES_STORY_GID: StoriesStoryGid,
        PathValues.TASKS_TASK_GID_STORIES: TasksTaskGidStories,
        PathValues.TAGS: Tags,
        PathValues.TAGS_TAG_GID: TagsTagGid,
        PathValues.TASKS_TASK_GID_TAGS: TasksTaskGidTags,
        PathValues.WORKSPACES_WORKSPACE_GID_TAGS: WorkspacesWorkspaceGidTags,
        PathValues.TASKS: Tasks,
        PathValues.TASKS_TASK_GID: TasksTaskGid,
        PathValues.TASKS_TASK_GID_DUPLICATE: TasksTaskGidDuplicate,
        PathValues.PROJECTS_PROJECT_GID_TASKS: ProjectsProjectGidTasks,
        PathValues.SECTIONS_SECTION_GID_TASKS: SectionsSectionGidTasks,
        PathValues.TAGS_TAG_GID_TASKS: TagsTagGidTasks,
        PathValues.USER_TASK_LISTS_USER_TASK_LIST_GID_TASKS: UserTaskListsUserTaskListGidTasks,
        PathValues.TASKS_TASK_GID_SUBTASKS: TasksTaskGidSubtasks,
        PathValues.TASKS_TASK_GID_SET_PARENT: TasksTaskGidSetParent,
        PathValues.TASKS_TASK_GID_DEPENDENCIES: TasksTaskGidDependencies,
        PathValues.TASKS_TASK_GID_ADD_DEPENDENCIES: TasksTaskGidAddDependencies,
        PathValues.TASKS_TASK_GID_REMOVE_DEPENDENCIES: TasksTaskGidRemoveDependencies,
        PathValues.TASKS_TASK_GID_DEPENDENTS: TasksTaskGidDependents,
        PathValues.TASKS_TASK_GID_ADD_DEPENDENTS: TasksTaskGidAddDependents,
        PathValues.TASKS_TASK_GID_REMOVE_DEPENDENTS: TasksTaskGidRemoveDependents,
        PathValues.TASKS_TASK_GID_ADD_PROJECT: TasksTaskGidAddProject,
        PathValues.TASKS_TASK_GID_REMOVE_PROJECT: TasksTaskGidRemoveProject,
        PathValues.TASKS_TASK_GID_ADD_TAG: TasksTaskGidAddTag,
        PathValues.TASKS_TASK_GID_REMOVE_TAG: TasksTaskGidRemoveTag,
        PathValues.TASKS_TASK_GID_ADD_FOLLOWERS: TasksTaskGidAddFollowers,
        PathValues.TASKS_TASK_GID_REMOVE_FOLLOWERS: TasksTaskGidRemoveFollowers,
        PathValues.WORKSPACES_WORKSPACE_GID_TASKS_SEARCH: WorkspacesWorkspaceGidTasksSearch,
        PathValues.TEAM_MEMBERSHIPS_TEAM_MEMBERSHIP_GID: TeamMembershipsTeamMembershipGid,
        PathValues.TEAM_MEMBERSHIPS: TeamMemberships,
        PathValues.TEAMS_TEAM_GID_TEAM_MEMBERSHIPS: TeamsTeamGidTeamMemberships,
        PathValues.USERS_USER_GID_TEAM_MEMBERSHIPS: UsersUserGidTeamMemberships,
        PathValues.TEAMS: Teams,
        PathValues.TEAMS_TEAM_GID: TeamsTeamGid,
        PathValues.WORKSPACES_WORKSPACE_GID_TEAMS: WorkspacesWorkspaceGidTeams,
        PathValues.USERS_USER_GID_TEAMS: UsersUserGidTeams,
        PathValues.TEAMS_TEAM_GID_ADD_USER: TeamsTeamGidAddUser,
        PathValues.TEAMS_TEAM_GID_REMOVE_USER: TeamsTeamGidRemoveUser,
        PathValues.TIME_PERIODS_TIME_PERIOD_GID: TimePeriodsTimePeriodGid,
        PathValues.TIME_PERIODS: TimePeriods,
        PathValues.WORKSPACES_WORKSPACE_GID_TYPEAHEAD: WorkspacesWorkspaceGidTypeahead,
        PathValues.USER_TASK_LISTS_USER_TASK_LIST_GID: UserTaskListsUserTaskListGid,
        PathValues.USERS_USER_GID_USER_TASK_LIST: UsersUserGidUserTaskList,
        PathValues.USERS: Users,
        PathValues.USERS_USER_GID: UsersUserGid,
        PathValues.USERS_USER_GID_FAVORITES: UsersUserGidFavorites,
        PathValues.TEAMS_TEAM_GID_USERS: TeamsTeamGidUsers,
        PathValues.WORKSPACES_WORKSPACE_GID_USERS: WorkspacesWorkspaceGidUsers,
        PathValues.WEBHOOKS: Webhooks,
        PathValues.WEBHOOKS_WEBHOOK_GID: WebhooksWebhookGid,
        PathValues.WORKSPACE_MEMBERSHIPS_WORKSPACE_MEMBERSHIP_GID: WorkspaceMembershipsWorkspaceMembershipGid,
        PathValues.USERS_USER_GID_WORKSPACE_MEMBERSHIPS: UsersUserGidWorkspaceMemberships,
        PathValues.WORKSPACES_WORKSPACE_GID_WORKSPACE_MEMBERSHIPS: WorkspacesWorkspaceGidWorkspaceMemberships,
        PathValues.WORKSPACES: Workspaces,
        PathValues.WORKSPACES_WORKSPACE_GID: WorkspacesWorkspaceGid,
        PathValues.WORKSPACES_WORKSPACE_GID_ADD_USER: WorkspacesWorkspaceGidAddUser,
        PathValues.WORKSPACES_WORKSPACE_GID_REMOVE_USER: WorkspacesWorkspaceGidRemoveUser,
    }
)
