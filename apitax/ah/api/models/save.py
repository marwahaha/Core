# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from apitax.ah.api.models.base_model_ import Model
from apitax.ah.api.models.script import Script  # noqa: F401,E501
from apitax.ah.api import util


class Save(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, script=None):  # noqa: E501
        """Save - a model defined in Swagger

        :param script: The script of this Save.  # noqa: E501
        :type script: Script
        """
        self.swagger_types = {
            'script': Script
        }

        self.attribute_map = {
            'script': 'script'
        }

        self._script = script

    @classmethod
    def from_dict(cls, dikt):
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The save of this Save.  # noqa: E501
        :rtype: Save
        """
        return util.deserialize_model(dikt, cls)

    @property
    def script(self):
        """Gets the script of this Save.


        :return: The script of this Save.
        :rtype: Script
        """
        return self._script

    @script.setter
    def script(self, script):
        """Sets the script of this Save.


        :param script: The script of this Save.
        :type script: Script
        """
        if script is None:
            raise ValueError("Invalid value for `script`, must not be `None`")  # noqa: E501

        self._script = script
