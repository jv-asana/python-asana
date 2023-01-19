# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from asana.paths.status_updates import Api

from asana.paths import PathValues

path = PathValues.STATUS_UPDATES