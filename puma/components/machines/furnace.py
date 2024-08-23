# -*- coding: utf-8 -*-
"""
puma.components.machines.furnace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

import datetime as dt

import numpy as np
import pandas as pd
from loris import ChannelState, Configurations
from loris.components import register_component_type
from puma.components.machines import Machine


# noinspection SpellCheckingInspection
@register_component_type
class Furnace(Machine):
    TYPE: str = "furnace"

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)

        # noinspection PyShadowingBuiltins
        def _add_channel(key: str, name: str, min: float, max: float, **kwargs) -> None:
            self.data.add(key, name=name, connector="random", type=float, min=min, max=max, **kwargs)

        _add_channel("temp_low", f"{self.name} Temperature Low [0-50]", 5, 55)
        _add_channel("temp_high", f"{self.name} Temperature High [30-100]", 30, 100)

        self.data.add(
            key="temp_mean",
            name=f"{self.name} Temperature Mean",
            type=float,
            connector=None
        )

    def run(
        self,
        start: pd.Timestamp | dt.datetime = None,
        end: pd.Timestamp | dt.datetime = None,
        **kwargs
    ) -> pd.DataFrame:
        module_temps = [self.data.temp_low, self.data.temp_high]
        if all(c.is_valid() for c in module_temps):
            self.data.temp_mean.set(
                np.array([t.timestamp for t in module_temps]).max(),
                np.array([t.value for t in module_temps]).mean(),
            )
        else:
            self.data.temp_mean.state = ChannelState.NOT_AVAILABLE
        return self.get(start, end, **kwargs)
