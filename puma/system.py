# -*- coding: utf-8 -*-
"""
puma.system
~~~~~~~~~~~


"""

from __future__ import annotations

import datetime as dt

import lori
import pandas as pd
from lori import ComponentException, Configurations
from puma import Pecvd


class System(lori.System):
    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        if self.has_type(Pecvd):
            self._logger.info("Pecvd type detected. Configuration complete.")

    # noinspection PyShadowingBuiltins, PyUnresolvedReferences
    def run(
        self,
        start: pd.Timestamp | dt.datetime = None,
        end: pd.Timestamp | dt.datetime = None,
        **kwargs,
    ) -> pd.DataFrame:
        try:
            actual_set_temp = []
            for pecvd in self.get_all(Pecvd):
                pecvd.run(start, end, **kwargs)

                for tube in pecvd.tubes:
                    if 'spike_act_set' in tube.temperatures.data:
                        actual_set_temp.append(tube.temperatures.data.spike_act_set)
                    else:
                        self._logger.warning(f"pecvd.data does not have attribute 'spike_act_set'")

            return self.get(start, end, **kwargs)

        except ComponentException as e:
            self._logger.warning(f"Unable to run system '{self.name}': {repr(e)}")
