from asana.paths.stories_story_gid.get import ApiForget
from asana.paths.stories_story_gid.put import ApiForput
from asana.paths.stories_story_gid.delete import ApiFordelete


class StoriesStoryGid(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
