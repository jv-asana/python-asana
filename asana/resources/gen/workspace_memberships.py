# coding=utf-8
class _WorkspaceMemberships:

    def __init__(self, client=None):
        self.client = client

    def get_workspace_membership(self, workspace_membership_gid, params=None, **options):
        """Get a workspace membership
        :param str workspace_membership_gid: (required)
        :param Object params: Parameters for the request
            - opt_fields {[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
        :param **options
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """

        if params is None:
            params = {}
        path = "/workspace_memberships/{workspace_membership_gid}".replace("{workspace_membership_gid}", workspace_membership_gid)
        return self.client.get(path, params, **options)

        
    def get_workspace_memberships_for_user(self, user_gid, params=None, **options):
        """Get workspace memberships for a user
        :param str user_gid: (required) A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
        :param Object params: Parameters for the request
            - opt_fields {[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param **options
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """

        if params is None:
            params = {}
        path = "/users/{user_gid}/workspace_memberships".replace("{user_gid}", user_gid)
        return self.client.get(path, params, **options)

        
    def get_workspace_memberships_for_workspace(self, workspace_gid, params=None, **options):
        """Get the workspace memberships for a workspace
        :param str workspace_gid: (required) Globally unique identifier for the workspace or organization.
        :param Object params: Parameters for the request
            - user {str}:  A string identifying a user. This can either be the string \"me\", an email, or the gid of a user.
            - opt_fields {[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
        :param **options
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """

        if params is None:
            params = {}
        path = "/workspaces/{workspace_gid}/workspace_memberships".replace("{workspace_gid}", workspace_gid)
        return self.client.get(path, params, **options)

        
