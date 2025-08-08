# -*- coding: utf-8 -*-
"""
twinline.components.manufacturers.centrotherm.pecvd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

from lori import Configurations
from lori.components import register_component_type
from twinline.components.machines.depositors import Pecvd
from twinline.components.manufacturers.centrotherm.pecvd import CPlasmaTube


@register_component_type("c_plasma")
class CPlasma(Pecvd):
    def _load_tube(self, configs: Configurations, index: int) -> CPlasmaTube:
        return CPlasmaTube(self, configs, index)
