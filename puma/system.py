# -*- coding: utf-8 -*-
"""
puma.system
~~~~~~~~~~~


"""

from __future__ import annotations

import datetime as dt

import lori
import numpy as np
import pandas as pd
from lori import ChannelState, ComponentException, Configurations
from puma import Furnace


class System(lori.System):
    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        if self.has_type(Furnace):
            self.data.add(
                key="furnaces_tube_temp_mean",
                name="Furnaces tube temperature [°C]",
                type=float,
                connector=None,
            )

    def activate(self) -> None:
        super().activate()
        if self.has_type(Furnace):
            furnace_temp_channels = [f.data.tube_temp_mean for f in self.get_all(Furnace)]
            self.data.register(self._furnace_tube_callback, *furnace_temp_channels, how="all", unique=True)

    def _furnace_tube_callback(self, data: pd.DataFrame) -> None:
        temperatures = data[[c for c in data.columns if "temp" in c]]
        if not temperatures.empty:
            temperature_mean = temperatures.ffill().bfill().mean(axis="columns")
            if len(temperature_mean) == 1:
                temperature_mean = temperature_mean.iloc[0]
            self.data.furnaces_tube_temp_mean.value = temperature_mean
        else:
            self.data.furnaces_tube_temp_mean.state = ChannelState.NOT_AVAILABLE
