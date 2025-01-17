# -*- coding: utf-8 -*-
"""
puma.components.machines.diffusions.furnace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

from lori.components import register_component_type
from puma.components.machines import Machine


@register_component_type("diffusion", "diffusion_furnace")
class DiffusionFurnace(Machine):
    pass
