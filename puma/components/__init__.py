# -*- coding: utf-8 -*-
"""
puma.components
~~~~~~~~~~~~~~~


"""

from . import module  # noqa: F401
from .module import ModuleSpecifications  # noqa: F401

from loris.components import registry

registry.register(ModuleSpecifications, ModuleSpecifications.TYPE)
del registry
