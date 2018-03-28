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

import pprint
import re  # noqa: F401

import six


class GnbrEntity(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'entity_id': 'str',
        'synonyms': 'list[ERRORUNKNOWN]',
        'entity_type': 'str'
    }

    attribute_map = {
        'entity_id': 'entityID',
        'synonyms': 'synonyms',
        'entity_type': 'entityType'
    }

    def __init__(self, entity_id=None, synonyms=None, entity_type=None):  # noqa: E501
        """GnbrEntity - a model defined in Swagger"""  # noqa: E501

        self._entity_id = None
        self._synonyms = None
        self._entity_type = None
        self.discriminator = None

        if entity_id is not None:
            self.entity_id = entity_id
        if synonyms is not None:
            self.synonyms = synonyms
        if entity_type is not None:
            self.entity_type = entity_type

    @property
    def entity_id(self):
        """Gets the entity_id of this GnbrEntity.  # noqa: E501


        :return: The entity_id of this GnbrEntity.  # noqa: E501
        :rtype: str
        """
        return self._entity_id

    @entity_id.setter
    def entity_id(self, entity_id):
        """Sets the entity_id of this GnbrEntity.


        :param entity_id: The entity_id of this GnbrEntity.  # noqa: E501
        :type: str
        """

        self._entity_id = entity_id

    @property
    def synonyms(self):
        """Gets the synonyms of this GnbrEntity.  # noqa: E501


        :return: The synonyms of this GnbrEntity.  # noqa: E501
        :rtype: list[ERRORUNKNOWN]
        """
        return self._synonyms

    @synonyms.setter
    def synonyms(self, synonyms):
        """Sets the synonyms of this GnbrEntity.


        :param synonyms: The synonyms of this GnbrEntity.  # noqa: E501
        :type: list[ERRORUNKNOWN]
        """

        self._synonyms = synonyms

    @property
    def entity_type(self):
        """Gets the entity_type of this GnbrEntity.  # noqa: E501


        :return: The entity_type of this GnbrEntity.  # noqa: E501
        :rtype: str
        """
        return self._entity_type

    @entity_type.setter
    def entity_type(self, entity_type):
        """Sets the entity_type of this GnbrEntity.


        :param entity_type: The entity_type of this GnbrEntity.  # noqa: E501
        :type: str
        """

        self._entity_type = entity_type

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GnbrEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other