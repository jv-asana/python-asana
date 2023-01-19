# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3

import asana
from asana.paths.workspaces_workspace_gid_workspace_memberships import get  # noqa: E501
from asana import configuration, schemas, api_client

from .. import ApiTestMixin


class TestWorkspacesWorkspaceGidWorkspaceMemberships(ApiTestMixin, unittest.TestCase):
    """
    WorkspacesWorkspaceGidWorkspaceMemberships unit test stubs
        Get the workspace memberships for a workspace  # noqa: E501
    """
    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200




if __name__ == '__main__':
    unittest.main()
