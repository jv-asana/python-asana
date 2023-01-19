# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import asana
from asana.paths.status_updates_status_gid import delete  # noqa: E501
from asana import configuration, schemas, api_client

from .. import ApiTestMixin


class TestStatusUpdatesStatusGid(ApiTestMixin, unittest.TestCase):
    """
    StatusUpdatesStatusGid unit test stubs
        Delete a status update  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = delete.ApiFordelete(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
