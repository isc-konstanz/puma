# -*- coding: utf-8 -*-
"""
    puma.system
    ~~~~~~~~~~~


"""
from __future__ import annotations

import datetime as dt

import numpy as np

import loris
import pandas as pd
from loris import ComponentException, Configurations
from puma import Furnace


class System(loris.System):

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        for module in self.get_all(Furnace):
            self.data.add(
                id=f"{module.id}_temp_mean",
                name=f"{module.name} Temperature Mean",
                type=float,
                connector=None
            )

    # noinspection PyShadowingBuiltins, PyUnresolvedReferences
    def run(
        self,
        start: pd.Timestamp | dt.datetime = None,
        end: pd.Timestamp | dt.datetime = None,
        **kwargs
    ) -> pd.DataFrame:
        try:
            for module in self.get_all(Furnace):
                module_temp_mean = self.data[f"{module.id}_temp_mean"]
                module_temps = [module.data.temp_low, module.data.temp_high]
                if all(c.is_valid() for c in module_temps):
                    module_temp_mean.set(
                        np.array([t.timestamp for t in module_temps]).max(),
                        np.array([t.value for t in module_temps]).mean()
                    )
                else:
                    module_temp_mean.state = ChannelState.NOT_AVAILABLE
                if module_temp_mean.value > 60:
                    self._logger.warning(f"{module.name} Temperature high: {module_temp_mean.value}")

            return self.get(start, end, **kwargs)

        except ComponentException as e:
            self._logger.warning(f"Unable to run system '{self.name}': {str(e)}")
