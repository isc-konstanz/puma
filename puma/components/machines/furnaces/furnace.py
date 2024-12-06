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


@register_component_type("furnace")
class Furnace(Machine):
    def configure(self, configs: Configurations) -> None:
        super().configure(configs)

        # noinspection PyShadowingBuiltins
        def _add_random(key: str, name: str, min: float, max: float, **kwargs) -> None:
            self.data.add(key, name=name, type=float, connector="dummy", generator="random", min=min, max=max, **kwargs)

        _add_random("tube_temp_front", "Tube temperature (front) [°C]", 5000, 6000)
        _add_random("tube_temp_back", "Tube temperature (back) [°C]", 4000, 5000)

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
