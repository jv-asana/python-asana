from asana.paths.goals_goal_gid.get import ApiForget
from asana.paths.goals_goal_gid.put import ApiForput
from asana.paths.goals_goal_gid.delete import ApiFordelete


class GoalsGoalGid(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
