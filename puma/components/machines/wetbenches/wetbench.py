# -*- coding: utf-8 -*-
"""
puma.components.machines.wetbenches.wetbench
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

from lori import Configurations
from lori.components import register_component_type
from puma.components.machines import Machine

TYPE: str = "wetbench"


# noinspection SpellCheckingInspection
@register_component_type(TYPE)
class WetBench(Machine):
    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        self.data.add(
            key="acidity",
            name="Acidity [pH]",
            type=float,
            min=0,
            max=2,
            connector="random",
        )
