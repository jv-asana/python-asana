from asana.paths.tags_tag_gid.get import ApiForget
from asana.paths.tags_tag_gid.put import ApiForput
from asana.paths.tags_tag_gid.delete import ApiFordelete


class TagsTagGid(
    ApiForget,
    ApiForput,
    ApiFordelete,
):
    pass
