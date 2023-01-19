from asana.paths.projects_project_gid.get import ApiForget
from asana.paths.projects_project_gid.put import ApiForput
from asana.paths.projects_project_gid.delete import ApiFordelete


class ProjectsProjectGid(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
