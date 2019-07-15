# coding=utf-8
"""This module contains a mixin for max and min service instances"""

# Python 2/3 compatibility
# pylint: disable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position
from __future__ import (absolute_import, division, print_function, unicode_literals)
from future.builtins.disabled import *
from future.builtins import *
from future.standard_library import install_aliases
install_aliases()
# pylint: enable=wildcard-import,unused-wildcard-import,wrong-import-order,wrong-import-position

from ..editing.edit_prop import EditorProperty

def max_instances_constraint(self, value):
    if value < self.min_instances:
        # Max instances can't be smaller than min instances, so bring min instances down to the same size if smaller
        self.min_instances = value

    return value


def min_instances_constraint(self, value):
    if value > self.max_instances:
        # Min instances can't be bigger than max instances, so make the same size
        self.max_instances = value

    return value

class MaxMinInstancesMixin(object):

    max_instances = EditorProperty(
        {
            "constraints": {
                "int": True,
                "min": 1,
                "func": max_instances_constraint
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.maxInstancesPerNode"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'MaxInstances']/Value"
                        }
                    ]
                }
            }
        }
    )

    min_instances = EditorProperty(
        {
            "constraints": {
                "int": True,
                "min": 0,
                "func": min_instances_constraint
            },
            "formats": {
                "agsJson": {
                    "paths": [{
                        "document": "main",
                        "path": "$.minInstancesPerNode"
                    }]
                },
                "sddraft": {
                    "paths": [
                        {
                            "path":
                            "./Configurations/SVCConfiguration/Definition/Props/PropertyArray/PropertySetProperty[Key = 'MinInstances']/Value"
                        }
                    ]
                }
            }
        }
    )