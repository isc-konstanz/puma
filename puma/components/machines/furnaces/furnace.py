# -*- coding: utf-8 -*-
"""
puma.components.machines.furnaces.furnace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

import pandas as pd
from lori import ChannelState, Configurations
from lori.components import register_component_type
from puma.components.machines import Machine

TYPE: str = "furnace"


@register_component_type(TYPE)
class Furnace(Machine):
    def configure(self, configs: Configurations) -> None:
        super().configure(configs)

        # noinspection PyShadowingBuiltins
        def _add_channel(key: str, name: str, min: float, max: float, **kwargs) -> None:
            self.data.add(key, name=name, connector="random", type=float, min=min, max=max, **kwargs)

        _add_channel("tube_temp_front", "Tube temperature (front) [°C]", 5000, 6000)
        _add_channel("tube_temp_back", "Tube temperature (back) [°C]", 4000, 5000)

        self.data.add(
            key="tube_temp_mean",
            name="Tube temperature mean [°C]",
            type=float,
            connector=None,
        )

    def activate(self) -> None:
        super().activate()
        tube_temp_channels = [self.data.tube_temp_front, self.data.tube_temp_back]
        self.data.register(self._tube_callback, *tube_temp_channels, how="all", unique=True)

    def _tube_callback(self, data: pd.DataFrame) -> None:
        temperatures = data[[c for c in data.columns if "temp" in c]]
        if not temperatures.empty:
            temperature_mean = temperatures.ffill().bfill().mean(axis="columns")
            if len(temperature_mean) == 1:
                temperature_mean = temperature_mean.iloc[0]
            self.data.tube_temp_mean.value = temperature_mean
        else:
            self.data.tube_temp_mean.state = ChannelState.NOT_AVAILABLE
