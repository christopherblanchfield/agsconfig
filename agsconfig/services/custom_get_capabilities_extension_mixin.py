"""This module contains the Custom Get Capabilities extension mixin"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from ..editing.edit_prop import EditorProperty
from .extension_base import ExtensionBase

class CustomGetCapabilitiesExtensionMixin(object):
    """ Attributes for custom Get Capabilities on ArcGIS services """

    custom_get_capabilities = EditorProperty(
        {
            "formats": {
                 "agsJson": {
                    "paths": [
                        {
                            "document": "main",
                            "path": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties.customGetCapabilities".format(extension_name),
                            "parentPath": lambda extension_name: "$.extensions[?(@.typeName = '{0}')].properties".format(extension_name),
                            "key": "customGetCapabilities"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }],
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='customGetCapabilities']/Value".format(extension_name)
                        }
                    ],
                    "conversions": [
                        {
                            "id": "boolToString"
                        }
                    ]
                }
            }
        })

    path_to_custom_get_capabilities_files = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name: "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='pathToCustomGetCapabilitiesFiles']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })
