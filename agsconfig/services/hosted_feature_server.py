# coding=utf-8
"""This module contains the HostedFeatureServer class
for editing HostedFeatureServer configuration pre or post publish"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position,no-name-in-module,import-error
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position,no-name-in-module,import-error

from enum import Enum

from .max_min_instances_mixin import MaxMinInstancesMixin
from .cacheable_core_mixin import CacheableCoreMixin
from .cacheable_ext_mixin import CacheableExtMixin
from .image_dimensions_mixin import ImageDimensionsMixin
from .max_record_count_mixin import MaxRecordCountMixin
from .service_base import ServiceBase
from ..editing.edit_prop import EditorProperty
from ..services.feature_server_extension import FeatureServerExtension


class HostedFeatureServer(
    MaxRecordCountMixin, MaxMinInstancesMixin, CacheableCoreMixin, ServiceBase
):
    """ Class for editing hosted feature services."""
    _feature_server_extension = None

    class Capability(Enum):
        create = "Create"
        query = "Query"
        update = "Update"
        delete = "Delete"
        sync = "Sync"
        extract = "Extract"
        editing = "Editing"

    def __init__(self, editor):
        super().__init__(editor)
        self._feature_server_extension = FeatureServerExtension(editor)

    capabilities = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "path": "$.capabilities"
                    }],
                    "conversions": [{
                        "id": "enumToString", "enum": "Capability"
                    }, {
                        "id": "stringToCsv"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Info/PropertyArray/PropertySetProperty[Key='webCapabilities']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "enumToString", "enum": "Capability"
                    }, {
                        "id": "stringToCsv"
                    }]
                }
            }
        }
    )

    # Not to be confused with allowGeometryUpdates from the feature server extension
    allow_geometry_updates = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.properties.allowGeometryUpdates"  # TODO: Verify
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='allowGeometryUpdates']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    # Not to be confused with allowTrueCurvesUpdates from the feature server extension
    allow_true_curves_updates = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "path": "$.properties.allowTrueCurvesUpdates"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='allowTrueCurvesUpdates']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    only_allow_true_curve_updates_by_true_curve_clients = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "path": "$.properties.onlyAllowTrueCurveUpdatesByTrueCurveClients"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='onlyAllowTrueCurveUpdatesByTrueCurveClients']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    enable_z_defaults = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "path": "$.properties.enableZDefaults"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='EnableZDefaults']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    z_default_value = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "path": "$.properties.zDefaultValue"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='zDefaultValue']/Value"
                        }
                    ]
                }
            }
        }
    )

    allow_update_without_m_values = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "path": "$.properties.allowUpdateWithoutMValues"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='allowUpdateWithoutMValues']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    dataset_inspected = EditorProperty(
        {
            "formats": {
                # Apparently no json implementation
                "sddraft": {
                    "paths":
                    [{
                        "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='datasetInspected']/Value"
                    }],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    creator_present = EditorProperty(
        {
            "formats": {
                # Not found in json file
                "sddraft": {
                    "paths":
                    [{
                        "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='creatorPresent']/Value"
                    }],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    data_in_gdb = EditorProperty(
        {
            "formats": {
                # Not found in json file
                "sddraft": {
                    "paths": [{
                        "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='dataInGdb']/Value"
                    }],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    sync_enabled = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "path": "$.properties.syncEnabled"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/ConfigurationProperties/PropertyArray/PropertySetProperty[Key='syncEnabled']/Value"
                        }
                    ],
                    "conversions": [{
                        "id": "boolToString"
                    }]
                }
            }
        }
    )

    portal_url = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "parentPath": "$.properties", "path": "$.properties.portalURL"
                    }]
                },
                "sddraft": {
                    "paths": [
                            {
                            "parentPath": "./StagingSettings/PropertyArray",
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='PortalURL']/Value",
                            "tag": "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "PortalURL"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )

    user_name = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "parentPath": "$.properties", "path": "$.properties.userName"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "parentPath": "./StagingSettings/PropertyArray",
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='UserName']/Value",
                            "tag": "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "UserName"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )

    package_table_list = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "parentPath": "$.properties", "path": "$.properties.packageTableList"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "parentPath": "./StagingSettings/PropertyArray",
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='PackageTableList']/Value",
                            "tag": "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "PackageTableList"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )

    is_portal = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "parentPath": "$.properties", "path": "$.properties.isPortal"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "parentPath": "./StagingSettings/PropertyArray",
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='IsPortal']/Value",
                            "tag": "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "IsPortal"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )

    enable_wfs_server = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "parentPath": "$.properties", "path": "$.properties.enableWFSServer"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "parentPath": "./StagingSettings/PropertyArray",
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='EnableWFSServer']/Value",
                            "tag": "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "EnableWFSServer"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )

    cook_tiles_locally = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "parentPath": "$.properties", "path": "$.properties.cookTilesLocally"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "parentPath": "./StagingSettings/PropertyArray",
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='CookTilesLocally']/Value",
                            "tag": "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "CookTilesLocally"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )

    avoid_data_projection = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "parentPath": "$.properties", "path": "$.properties.avoidDataProjection"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "parentPath": "./StagingSettings/PropertyArray",
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='avoidDataProjection']/Value",
                            "tag": "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "avoidDataProjection"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )

    scene_service_name = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "parentPath": "$.properties", "path": "$.properties.sceneServiceName"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "parentPath": "./StagingSettings/PropertyArray",
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='SceneServiceName']/Value",
                            "tag": "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "SceneServiceName"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )

    portal_version = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "parentPath": "$.properties", "path": "$.properties.sceneServiceName"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "parentPath": "./StagingSettings/PropertyArray",
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='PortalVersion']/Value",
                            "tag": "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "PortalVersion"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )

    server_runtime_version = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "parentPath": "$.properties", "path": "$.properties.serverRuntimeVersion"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "parentPath": "./StagingSettings/PropertyArray",
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='ServerRunTimeVersion']/Value",
                            "tag": "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "ServerRunTimeVersion"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )

    ags_server_version = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "parentPath": "$.properties", "path": "$.properties.agsServerVersion"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "parentPath": "./StagingSettings/PropertyArray",
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='AGSServerVersion']/Value",
                            "tag": "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "AGSServerVersion"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )

    admin_version = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "parentPath": "$.properties", "path": "$.properties.adminVersion"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "parentPath": "./StagingSettings/PropertyArray",
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='AdminVersion']/Value",
                            "tag": "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "AdminVersion"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )

    wfs_properties = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "parentPath": "$.properties", "path": "$.properties.wfsProperties"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "parentPath": "./StagingSettings/PropertyArray",
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='WFSProperties']/Value",
                            "tag": "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "WFSProperties"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )

    tile_cache_path = EditorProperty(
        {
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main", "parentPath": "$.properties", "path": "$.properties.tileCachePath"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "parentPath": "./StagingSettings/PropertyArray",
                            "path": "./StagingSettings/PropertyArray/PropertySetProperty[Key='TileCachePath']/Value",
                            "tag": "PropertySetProperty",
                            "attributes": {
                                "{http://www.w3.org/2001/XMLSchema-instance}type": "typens:PropertySetProperty"
                            },
                            "children": [
                                {
                                    "tag": "Key",
                                    "value": "TileCachePath"
                                },
                                {
                                    "tag": "Value",
                                    "attributes": {
                                        "{http://www.w3.org/2001/XMLSchema-instance}type": "xs:string"
                                    }
                                }
                            ]
                        }
                    ]
                }
            }
        }
    )
