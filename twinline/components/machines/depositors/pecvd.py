# -*- coding: utf-8 -*-
"""
twinline.components.machines.depositors.pecvd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

from typing import Collection, Sequence

from lori import Configurations
from lori.components import Component, register_component_type
from twinline.components.machines import Machine
from twinline.components.machines.depositors.tube import VacuumTube


# noinspection SpellCheckingInspection
@register_component_type("pecvd")
class Pecvd(Machine):
    # noinspection PyTypeChecker
    @property
    def tubes(self) -> Sequence[VacuumTube]:
        return self.components.get_all(VacuumTube)

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        self.configure_tubes(configs)

    def configure_tubes(self, configs: Configurations) -> None:
        defaults = Component._build_defaults(configs, strict=True)
        section = configs.get_section(VacuumTube.SECTION, defaults=defaults, ensure_exists=True)
        self._load_tubes(section, section.get("number", default=0))

    # noinspection PyUnusedLocal
    def _load_tubes(self, configs: Configurations, number: int) -> Collection[VacuumTube]:
        defaults = VacuumTube._build_defaults(configs, strict=True)
        tubes = []
        for i in range(1, number + 1):
            tube = self._load_tube(configs.get_section(str(i), defaults=defaults), i)
            tubes.append(tube)
            self.components.add(tube)
        return tubes

    def _load_tube(self, configs: Configurations, index: int) -> VacuumTube:
        return VacuumTube(self, configs, index)
