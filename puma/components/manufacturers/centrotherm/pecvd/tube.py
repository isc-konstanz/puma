# -*- coding: utf-8 -*-
"""
puma.components.machines.thermal.tube
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from typing import List

import pandas as pd
from lori import Configurations
from lori.util import get_includes
from puma.components.machines import Machine
from puma.components.machines.thermal import ThermalTube
from puma.components.manufacturers.centrotherm.pecvd import PlasmaTemperatures


class PlasmaTube(ThermalTube):
    INCLUDES: List[str] = [PlasmaTemperatures.SECTION]

    NUMBER: str = "number"

    def __init__(
        self,
        context: Machine,
        number: int,
        **kwargs,
    ) -> None:
        super().__init__(context, number, **kwargs)
        self.temperatures = PlasmaTemperatures(self)

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        number_attr = PlasmaTemperatures.DESC[PlasmaTemperatures.NUMBER]["attribute"]
        channel_section = configs.get_section("data", ensure_exists=True).get_section("channels", ensure_exists=True)
        channel_section[number_attr] = self.number

        temperatures_defaults = configs.get(get_includes(PlasmaTemperatures))
        self.temperatures.configure(configs.get_section(PlasmaTemperatures.SECTION, defaults=temperatures_defaults))

    def activate(self) -> None:
        super().activate()
        self.temperatures.activate()
        temperature_channels = self.temperatures.data[
            [
                PlasmaTemperatures.SPIKE_LZ_ACTUAL,
                PlasmaTemperatures.SPIKE_CENTER_ACTUAL,
                PlasmaTemperatures.SPIKE_CENTER_LZ_ACTUAL,
                PlasmaTemperatures.SPIKE_CENTER_GZ_ACTUAL,
                PlasmaTemperatures.SPIKE_GZ_ACTUAL,
            ]
        ]
        self.data.register(self._temperature_callback, *temperature_channels, how="all", unique=False)

    def deactivate(self) -> None:
        super().deactivate()
        self.temperatures.deactivate()

    def _temperature_callback(self, data: pd.DataFrame) -> None:
        self._logger.info(f"C.Plasma Tube{self.number} temperatures:\n{data.T}")
