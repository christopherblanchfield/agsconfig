"""This module contains an implementation of the NAServer extension."""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from enum import Enum
from .max_min_instances_mixin import MaxMinInstancesMixin
from ..editing.edit_prop import EditorProperty
from .extension_base import ExtensionBase

class NAServerExtension(ExtensionBase, MaxMinInstancesMixin):
    """Network Analysis server extension properties for ArcGIS Server services."""

    def __init__(self, editor):
        super().__init__(editor, "NAServer")

    # Capabilities is not implemented for NAServer
    capabilities = EditorProperty(
        {
            "formats": {}
        }
    )
