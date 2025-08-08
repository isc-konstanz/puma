# -*- coding: utf-8 -*-
"""
twinline.components.machines.firing.furnace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

from typing import Collection, Sequence

from lori import Component, Configurations
from lori.components import register_component_type
from twinline.components.machines import Machine
from twinline.components.machines.firing.tube import FiringTube


@register_component_type("furnace", "firing_furnace")
class FiringFurnace(Machine):
    # noinspection PyTypeChecker
    @property
    def tubes(self) -> Sequence[FiringTube]:
        return self.components.get_all(FiringTube)

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        self.configure_tubes(configs)

    def configure_tubes(self, configs: Configurations) -> None:
        defaults = Component._build_defaults(configs, strict=True)
        section = configs.get_section(FiringTube.SECTION, defaults=defaults, ensure_exists=True)
        self._load_tubes(section, section.get("number", default=0))

    # noinspection PyUnusedLocal
    def _load_tubes(self, configs: Configurations, number: int) -> Collection[FiringTube]:
        defaults = FiringTube._build_defaults(configs, strict=True)
        tubes = []
        for i in range(1, number + 1):
            tube = self._load_tube(configs.get_section(str(i), defaults=defaults), i)
            tubes.append(tube)
            self.components.add(tube)
        return tubes

    def _load_tube(self, configs: Configurations, index: int) -> FiringTube:
        return FiringTube(self, configs, index)
