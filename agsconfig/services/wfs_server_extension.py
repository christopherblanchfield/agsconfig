"""This module contains the WFS Server extension class"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins import *
from future.builtins.disabled import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from enum import Enum
from ..editing.edit_prop import EditorProperty
from .extension_base import ExtensionBase
from .ogc_metadata_extension_mixin import OGCMetadataExtensionMixin
from .custom_get_capabilities_extension_mixin import CustomGetCapabilitiesExtensionMixin

class WFSServerExtension(OGCMetadataExtensionMixin, CustomGetCapabilitiesExtensionMixin, ExtensionBase):
    """ WMS server extension properties for arcGIS services """

    extension_name = None

    class AxisOrder(Enum):
        lat_long = "LatLong"
        long_lat = "LongLat"

    def __init__(self, editor):
        super().__init__(editor, "WFSServer")
        extension_name = super().get_extension_name()

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

    app_schema_uri = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='appSchemaURI']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    app_schema_prefix = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='appSchemaPrefix']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    enable_transactions = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='enableTransactions']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    axis_order_wfs10 = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='axisOrderWFS10']/Value".format(extension_name)
                        }
                    ],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "AxisOrder"
                    }, {
                        "id": "stringToCsv"
                    }]
                }
            }
        })

    axis_order_wfs11 = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='axisOrderWFS11']/Value".format(extension_name)
                        }
                    ],
                    "conversions": [{
                        "id": "enumToString",
                        "enum": "AxisOrder"
                    }, {
                        "id": "stringToCsv"
                    }]
                }
            }
        })

    service_type = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='serviceType']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })

    service_type_version = EditorProperty(
        {
            "formats": {
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            lambda extension_name : "./Configurations/SVCConfiguration/Definition/Extensions/SVCExtension[TypeName='{0}']/Props/PropertyArray/PropertySetProperty[Key='serviceTypeVersion']/Value".format(extension_name)
                        }
                    ]
                }
            }
        })