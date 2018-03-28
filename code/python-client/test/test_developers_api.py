# coding: utf-8

"""
    GNBR

    This API provides access to the relationships between entities in the global network of biomedical relationships (GNBR) derived from text  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: alavertu@stanford.edu
    Generated by: https://github.com/swagger-api/swagger-codegen.git

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.developers_api import DevelopersApi  # noqa: E501
from swagger_client.rest import ApiException


class TestDevelopersApi(unittest.TestCase):
    """DevelopersApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.developers_api.DevelopersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_edge(self):
        """Test case for get_edge

        Query for an edge  # noqa: E501
        """
        pass

    def test_get_identifier(self):
        """Test case for get_identifier

        Find GNBR identifier  # noqa: E501
        """
        pass

    def test_get_node_neighbors(self):
        """Test case for get_node_neighbors

        Get all neighbors of a particular node  # noqa: E501
        """
        pass

    def test_get_subgraph(self):
        """Test case for get_subgraph

        Get a GNBR subgraph  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()