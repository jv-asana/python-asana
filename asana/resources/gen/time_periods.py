# coding=utf-8
class _TimePeriods:

    def __init__(self, client=None):
        self.client = client

    def get_time_period(self, time_period_gid, params=None, **options):
        """Get a time period
        :param str time_period_gid: (required) Globally unique identifier for the time period.
        :param Object params: Parameters for the request
            - opt_fields {[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
        :param **options
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """

        if params is None:
            params = {}
        path = "/time_periods/{time_period_gid}".replace("{time_period_gid}", time_period_gid)
        return self.client.get(path, params, **options)

        
    def get_time_periods(self, params=None, **options):
        """Get time periods
        :param Object params: Parameters for the request
            - opt_fields {[str]}:  Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
            - limit {int}:  Results per page. The number of objects to return per page. The value must be between 1 and 100.
            - offset {str}:  Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. 'Note: You can only pass in an offset that was returned to you via a previously paginated request.'
            - start_on {date}:  ISO 8601 date string
            - end_on {date}:  ISO 8601 date string
            - workspace {str}:  (required) Globally unique identifier for the workspace.
        :param **options
            - opt_pretty {bool}:  Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
        :return: Object
        """

        if params is None:
            params = {}
        path = "/time_periods"
        return self.client.get_collection(path, params, **options)

        
