# -*- coding: utf-8 -*-
"""
puma.components.machines.firing.furnace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

from lori import Configurations
from lori.components import register_component_type
from lori.util import get_includes
from puma.components.machines.firing.tube import FiringTube
from puma.components.machines.thermal import ThermalMachine


@register_component_type("furnace", "firing_furnace")
class FiringFurnace(ThermalMachine):
    tubes_number: int

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        tubes = configs.get_section(FiringTube.SECTION, ensure_exists=True)
        tubes_number = tubes.get("number", default=0)
        tube_defaults = configs.get(get_includes(FiringTube))

        for i in range(1, tubes_number + 1):
            tube_configs = tubes.get_section(f"{i}", defaults=tube_defaults)
            tube = FiringTube(self, i)
            tube.configure(tube_configs)
            self.tubes.append(tube)
