# coding=utf-8
"""This module contains the ServiceBase abstract base class for implementing ArcGIS Server service configuration models."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

# Python lib imports
from abc import ABCMeta

# Third-party package imports
from enum import Enum

# Local package imports
from ..editing.edit_prop import EditorProperty
from ..model_base import ModelBase


class ExtensionBase(ModelBase):
    """Contains base settings/configuration that are common across ArcGIS Service extensions."""

    __metaclass__ = ABCMeta

    _editor = None
    _extension_name = None

    class Capability(Enum):
        """Must be overridden by sub-classes if any capabilities are supported."""
        pass

    def __init__(self, editor, extension_name):
        """Initilises the class.

        Args:
            editor: An editor object that will receive metadata about each property
            extension_name: Used to find xpaths in sddrafts where there is more than one extension
        """

        self._editor = editor
        self._extension_name = extension_name

    @property
    def extension_name(self):
        return self._extension_name

    enabled = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Enabled".format(extension_name)
                        }
                    ]
                }
            }
        })
