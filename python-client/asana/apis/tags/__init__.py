# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from asana.apis.tag_to_api import tag_to_api

import enum


class TagValues(str, enum.Enum):
    ATTACHMENTS = "Attachments"
    AUDIT_LOG_API = "Audit log API"
    BATCH_API = "Batch API"
    CUSTOM_FIELDS = "Custom fields"
    CUSTOM_FIELD_SETTINGS = "Custom field settings"
    EVENTS = "Events"
    GOALS = "Goals"
    GOAL_RELATIONSHIPS = "Goal relationships"
    JOBS = "Jobs"
    ORGANIZATION_EXPORTS = "Organization exports"
    PORTFOLIOS = "Portfolios"
    PORTFOLIO_MEMBERSHIPS = "Portfolio memberships"
    PROJECTS = "Projects"
    PROJECT_BRIEFS = "Project briefs"
    PROJECT_MEMBERSHIPS = "Project memberships"
    PROJECT_STATUSES = "Project statuses"
    PROJECT_TEMPLATES = "Project templates"
    SECTIONS = "Sections"
    STATUS_UPDATES = "Status updates"
    STORIES = "Stories"
    TAGS = "Tags"
    TASKS = "Tasks"
    TEAMS = "Teams"
    TEAM_MEMBERSHIPS = "Team memberships"
    TIME_PERIODS = "Time periods"
    TYPEAHEAD = "Typeahead"
    USERS = "Users"
    USER_TASK_LISTS = "User task lists"
    WEBHOOKS = "Webhooks"
    WORKSPACES = "Workspaces"
    WORKSPACE_MEMBERSHIPS = "Workspace memberships"
