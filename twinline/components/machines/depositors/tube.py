# -*- coding: utf-8 -*-
"""
twinline.components.machines.depositors.tube
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from typing import Collection, Optional, Sequence

from lori import Component, Configurations
from twinline.components.machines import Tube
from twinline.components.machines.depositors.zone import ThermalZone


class VacuumTube(Tube):
    # noinspection PyTypeChecker
    @property
    def zones(self) -> Sequence[ThermalZone]:
        return self.components.get_all(ThermalZone)

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
        defaults = Component._build_defaults(configs, strict=True)
        section = configs.get_section(VacuumTube.SECTION, defaults=defaults, ensure_exists=True)
        self._load_zones(section, section.get("number", default=0))

    # noinspection PyUnusedLocal
    def _load_zones(self, configs: Configurations, number: int) -> Collection[ThermalZone]:
        defaults = ThermalZone._build_defaults(configs, strict=True)
        zones = []
        for i in range(...):
            zone = self._load_zone(configs.get_section(str(i), defaults=defaults), i)
            zones.append(zone)
            self.components.add(zone)
        return zones

    def _load_zone(
        self,
        configs: Configurations,
        index: int,
        key: Optional[str] = None,
        name: Optional[str] = None,
    ) -> ThermalZone:
        return ThermalZone(self, configs, index, key, name)
