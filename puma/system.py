# -*- coding: utf-8 -*-
"""
    puma.system
    ~~~~~~~~~~~


"""
from __future__ import annotations

import datetime as dt

import loris
import numpy as np
import pandas as pd
from loris import ChannelState, ComponentException, Configurations
from puma import Furnace


class System(loris.System):
    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        if self.has_type(Furnace):
            self.data.add(
                key=f"furnace_temp_mean",
                name=f"Furnaces Temperature Mean",
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
            furnace_temp_means = []
            for furnace in self.get_all(Furnace):
                furnace.run(start, end, **kwargs)
                furnace_temp_means.append(furnace.data.temp_mean)
            if len(furnace_temp_means) > 0 and all(c.is_valid() for c in furnace_temp_means):
                self.data.furnace_temp_mean.set(
                    np.array([t.timestamp for t in furnace_temp_means]).max(),
                    np.array([t.value for t in furnace_temp_means]).mean(),
                )
            else:
                self.data.furnace_temp_mean.state = ChannelState.NOT_AVAILABLE
            return self.get(start, end, **kwargs)

        except ComponentException as e:
            self._logger.warning(f"Unable to run system '{self.name}': {repr(e)}")
