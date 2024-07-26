# -*- coding: utf-8 -*-
"""
    puma.system
    ~~~~~~~~~~~


"""
from __future__ import annotations

import datetime as dt


import loris
import pandas as pd
from loris import ComponentException, Configurations
from puma import ModuleSpecifications


class System(loris.System):

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        for module in self.get_all(ModuleSpecifications):
            self.data.add(
                id=f"{module.id}_total",
                name=f"{module.name} Total",
                value_type=float,
                connector=None
            )
            self.data.add(
                id=f"{module.id}_sum",
                name=f"{module.name} Sum",
                value_type=float,
                connector=None
            )
            self.data.add(
                id=f"{module.id}_latest",
                name=f"{module.name} Latest",
                column=f"{module.id}_sum",
                value_type=float,
                connector="csv",
                logger=None
            )

    # noinspection PyShadowingBuiltins, PyUnresolvedReferences
    def run(
        self,
        start: pd.Timestamp | dt.datetime = None,
        end: pd.Timestamp | dt.datetime = None,
        **kwargs
    ) -> pd.DataFrame:
        try:
            for module in self.get_all(ModuleSpecifications):
                module.run()
                module_sum = self.data[f"{module.id}_sum"]
                module_latest = self.data[f"{module.id}_latest"]
                module_total = self.data[f"{module.id}_total"]

                if all(c.is_valid() for c in [module.data.random_int, module.data.random_float]):
                    module_sum.value = module.data.random_int.value + module.data.random_float.value
                    module_total.value = module_sum.value + module_latest.value if module_latest.is_valid() else 0
                else:
                    module_sum.state = ChannelState.NOT_AVAILABLE
                    module_total.state = ChannelState.NOT_AVAILABLE

            return self.get(start, end, **kwargs)

        except ComponentException as e:
            self._logger.warning(f"Unable to run system '{self.name}': {str(e)}")
