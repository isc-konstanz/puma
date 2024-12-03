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
    Pecvd,
    ModuleSpecifications,
)

from . import system  # noqa: F401
from .system import System  # noqa: F401

from lori import Application  # noqa: F401


def load(name: str = "Puma", factory=System, **kwargs) -> Application:
    return Application.load(name, factory=factory, **kwargs)
