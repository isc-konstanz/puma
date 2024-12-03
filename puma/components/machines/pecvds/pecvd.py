# -*- coding: utf-8 -*-
"""
puma.components.machines.pecvds.Pecvd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

import datetime as dt
from typing import List

import pandas as pd
from lori import Configurations, Context
from lori.components import register_component_type
from puma.components.machines import Machine

from puma.components.machines.pecvds.tubes import Tube


@register_component_type
class Pecvd(Machine):
    TYPE: str = "pecvd"

    tubes: List[Tube]

    def __init__(self, context: Context, configs: Configurations, *args, **kwargs) -> None:
        super().__init__(context, configs, *args, **kwargs)

        self.tubes = [
            Tube(
                1,
                context,
                configs.get_section(
                    Tube.SECTION,
                    defaults={"data": configs.get_section("data")},
                    ensure_exists=True
                ),
            )
        ]

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        for tube in self.tubes:
           tube.configure(
               configs.get_section(
                   Tube.SECTION,
                   defaults={"data": configs.get_section("data")},
                   ensure_exists=True
               )
           )

    def activate(self) -> None:
        super().activate()
        for tube in self.tubes:
           tube.activate()

    def deactivate(self) -> None:
        super().deactivate()
        for tube in self.tubes:
           tube.deactivate()

    def run(
            self,
            start: pd.Timestamp | dt.datetime = None,
            end: pd.Timestamp | dt.datetime = None,
            **kwargs,
    ) -> pd.DataFrame:
        for tube in self.tubes:
            self._logger.info(tube.temperatures.data.to_frame())
        return self.get(start, end, **kwargs)
