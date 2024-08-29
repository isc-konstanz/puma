# -*- coding: utf-8 -*-
"""
puma.components.machines
~~~~~~~~~~~~~~~~~~~~~~~~


"""

from . import machine  # noqa: F401
from .machine import Machine  # noqa: F401

from . import furnaces  # noqa: F401
from .furnaces import Furnace  # noqa: F401

from . import wetbenches  # noqa: F401
from .wetbenches import WetBench  # noqa: F401

try:
    from .view import MachineGroup  # noqa: F401
    from .furnaces.view import FurnacePage  # noqa: F401
    from .wetbenches.view import WetBenchPage  # noqa: F401

except ImportError:
    pass
