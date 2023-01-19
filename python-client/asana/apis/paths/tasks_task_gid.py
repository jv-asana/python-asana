from asana.paths.tasks_task_gid.get import ApiForget
from asana.paths.tasks_task_gid.put import ApiForput
from asana.paths.tasks_task_gid.delete import ApiFordelete


class TasksTaskGid(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
