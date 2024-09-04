# -*- coding: utf-8 -*-
"""
puma.components.machines.furnaces.furnace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

import datetime as dt

import numpy as np
import pandas as pd
from loris import ChannelState, Configurations
from loris.components import register_component_type
from puma.components.machines import Machine


@register_component_type
class Furnace(Machine):
    TYPE: str = "furnace"

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

    def run(
        self,
        start: pd.Timestamp | dt.datetime = None,
        end: pd.Timestamp | dt.datetime = None,
        **kwargs,
    ) -> pd.DataFrame:
        tube_temps = [self.data.tube_temp_front, self.data.tube_temp_back]
        if all(c.is_valid() for c in tube_temps):
            self.data.tube_temp_mean.set(
                np.array([t.timestamp for t in tube_temps]).max(),
                np.array([t.value for t in tube_temps]).mean(),
            )
        else:
            self.data.tube_temp_mean.state = ChannelState.NOT_AVAILABLE
        return self.get(start, end, **kwargs)
