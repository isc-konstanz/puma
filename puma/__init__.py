# -*- coding: utf-8 -*-
"""
puma
~~~~


"""

from . import _version

__version__ = _version.get_versions().get("version")
del _version

from . import components  # noqa: F401
from .components import (  # noqa: F401
    DiffusionFurnace,
    FiringFurnace,
    Pecvd,
    Machine,
    ModuleSpecifications,
)

from .components import manufacturers  # noqa: F401

from . import application  # noqa: F401
from .application import Application


def load(name: str = "Puma", **kwargs) -> Application:
    return Application.load(name, **kwargs)
