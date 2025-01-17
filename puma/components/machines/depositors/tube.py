# -*- coding: utf-8 -*-
"""
puma.components.machines.depositors.tube
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from typing import Collection, List

from lori import Component, Configurations
from lori.util import get_includes
from puma.components.machines import Tube
from puma.components.machines.depositors.zone import ThermalZone


class VacuumTube(Tube):
    zones: List[ThermalZone]

    def __init__(
        self,
        context: Component,
        index: int,
        zones: Collection[ThermalZone] = (),
        **kwargs,
    ) -> None:
        super().__init__(context, index, **kwargs)
        self.zones = list(zones)

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        self.configure_vacuum(configs)
        self.configure_gas_flow(configs)
        self.configure_zones(configs)

    def configure_vacuum(self, configs: Configurations) -> None:
        pass

    def configure_gas_flow(self, configs: Configurations) -> None:
        pass

    def configure_zones(self, configs: Configurations) -> None:
        defaults = configs.get_sections(get_includes(ThermalZone))

        zones_configs = configs.get_section(ThermalZone.SECTION, defaults=defaults, ensure_exists=True)
        self.zones.extend(self.create_zones(zones_configs))
        for zone in self.zones:
            zone.configure(zones_configs.get_section(zone.key, defaults=defaults))

    # noinspection PyUnusedLocal, PyMethodMayBeStatic
    def create_zones(self, configs: Configurations) -> Collection[ThermalZone]:
        return []

    def activate(self) -> None:
        super().activate()
        for zone in self.zones:
            zone.activate()

    def deactivate(self) -> None:
        super().deactivate()
        for zone in self.zones:
            zone.deactivate()
