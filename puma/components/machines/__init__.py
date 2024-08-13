# -*- coding: utf-8 -*-
"""
puma.components.machines
~~~~~~~~~~~~~~~~~~~~~~~~


"""

from . import machine  # noqa: F401
from .machine import Machine  # noqa: F401

from .furnace import Furnace  # noqa: F401
try:
    from .view import (  # noqa: F401
        FurnacePage,
        MachineGroup,
    )
except ImportError:
    pass
