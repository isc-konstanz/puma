# -*- coding: utf-8 -*-
"""
puma.components.manufacturers.centrotherm.pecvd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

from typing import Collection

from lori import Configurations
from lori.components import register_component_type
from puma.components.machines.depositors import Pecvd
from puma.components.manufacturers.centrotherm.pecvd import CPlasmaTube


@register_component_type("c_plasma")
class CPlasma(Pecvd):
    def create_tubes(self, configs: Configurations, number: int) -> Collection[CPlasmaTube]:
        return [CPlasmaTube(self, i) for i in range(1, number + 1)]
