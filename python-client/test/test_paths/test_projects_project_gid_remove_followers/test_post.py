# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import asana
from asana.paths.projects_project_gid_remove_followers import post  # noqa: E501
from asana import configuration, schemas, api_client

from .. import ApiTestMixin


class TestProjectsProjectGidRemoveFollowers(ApiTestMixin, unittest.TestCase):
    """
    ProjectsProjectGidRemoveFollowers unit test stubs
        Remove followers from a project  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = post.ApiForpost(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200






if __name__ == '__main__':
    unittest.main()
