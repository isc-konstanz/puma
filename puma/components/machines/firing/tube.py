# -*- coding: utf-8 -*-
"""
puma.components.machines.firing.tube
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

import pandas as pd
from lori import ChannelState, Configurations
from puma.components.machines.thermal import ThermalTube


class FiringTube(ThermalTube):
    def configure(self, configs: Configurations) -> None:
        super().configure(configs)

        # noinspection PyShadowingBuiltins
        def _add_random(key: str, name: str, min: float, max: float, **kwargs) -> None:
            self.data.add(key, name=name, type=float, connector="dummy", generator="random", min=min, max=max, **kwargs)

        _add_random("temp_front", f"Tube {self.number} temperature (front) [°C]", 5000, 6000)
        _add_random("temp_back", f"Tube {self.number} temperature (back) [°C]", 4000, 5000)

        self.data.add(
            key="temp_mean",
            name=f"Tube {self.number} temperature mean [°C]",
            type=float,
            connector=None,
        )

    def activate(self) -> None:
        super().activate()
        self.data.register(
            self._temperature_callback,
            self.data.temp_front,
            self.data.temp_back,
            how="all",
            unique=False,
        )

    def _temperature_callback(self, data: pd.DataFrame) -> None:
        if not data.empty:
            temperature_mean = data.ffill().bfill().mean(axis="columns")
            if len(temperature_mean) == 1:
                temperature_mean = temperature_mean.iloc[0]
            self.data.temp_mean.value = temperature_mean
        else:
            self.data.temp_mean.state = ChannelState.NOT_AVAILABLE
