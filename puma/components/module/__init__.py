# -*- coding: utf-8 -*-
"""
puma.components.module
~~~~~~~~~~~~~~~~~~~~~~


"""

from . import specs  # noqa: F401
from .specs import ModuleSpecifications  # noqa: F401

try:
    from .view import ModuleSpecificationsPage  # noqa: F401

except ImportError:
    pass
