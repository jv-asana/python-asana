# coding=utf-8
from asana.page_iteratorimport import AuditLogAPIIterator

class AuditLogAPI:

    def __init__(self, client=None):
        self.client = client
    
    def get_audit_log_events(self, workspace_gid, params=None, **options):
        """Get audit log events
        :param str workspace_gid: (required) Globally unique identifier for the workspace or organization.
        :param Object params: Parameters for the request
            - start_at {datetime}:  Filter to events created after this time (inclusive).
            - end_at {datetime}:  Filter to events created before this time (exclusive).
            - event_type {str}:  Filter to events of this type. Refer to the [Supported AuditLogEvents](/docs/supported-auditlogevents) for a full list of values.
            - actor_type {str}:  Filter to events with an actor of this type. This only needs to be included if querying for actor types without an ID. If `actor_gid` is included, this should be excluded.
            - actor_gid {str}:  Filter to events triggered by the actor with this ID.
            - resource_gid {str}:  Filter to events with this resource ID.
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param **options
        :return: Object
        """
        if params is None:
            params = {}
        path = "/workspaces/{workspace_gid}/audit_log_events".replace("{workspace_gid}", workspace_gid)
        options = self.client._merge_options(options)
        iterator_type = options.get('iterator_type')
        if iterator_type == 'items':
            return AuditLogAPIIterator(self.client, path, params, options).items()
        if iterator_type is None:
            return self.client.get(path, params, **options)
        raise Exception(f'Unknown value for "iterator_type" option: {iterator_type}')

        
