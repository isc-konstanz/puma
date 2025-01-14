# -*- coding: utf-8 -*-
"""
puma.components.machines.thermal.machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

from typing import Collection, List

from lori import Configurations
from lori.data import DataAccess
from puma.components.machines import Machine
from puma.components.machines.thermal.tube import ThermalTube


# noinspection SpellCheckingInspection
class ThermalMachine(Machine):
    tubes: List[ThermalTube]

    def __init__(
        self,
        context: Machine,
        configs: Configurations,
        tubes: Collection[ThermalTube] = (),
        **kwargs,
    ) -> None:
        super().__init__(context, configs, **kwargs)
        self.tubes = list(tubes)

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        defaults = configs.get_sections([DataAccess.SECTION])
        for tube in self.tubes:
            tube.configure(configs.get_section(ThermalTube.SECTION, defaults=defaults, ensure_exists=True))

    def activate(self) -> None:
        super().activate()
        for tube in self.tubes:
            tube.activate()

    def deactivate(self) -> None:
        super().deactivate()
        for tube in self.tubes:
            tube.deactivate()
