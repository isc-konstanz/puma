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
    PECVD,
    Machine,
    ModuleSpecifications,
)


from lori import Application  # noqa: F401


def load(name: str = "Puma", **kwargs) -> Application:
    return Application.load(name, **kwargs)
