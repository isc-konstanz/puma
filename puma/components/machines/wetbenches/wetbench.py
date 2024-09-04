# -*- coding: utf-8 -*-
"""
puma.components.machines.wetbenches.wetbench
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

from loris import Configurations
from loris.components import register_component_type
from puma.components.machines import Machine


# noinspection SpellCheckingInspection
@register_component_type
class WetBench(Machine):
    TYPE: str = "wetbench"

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
