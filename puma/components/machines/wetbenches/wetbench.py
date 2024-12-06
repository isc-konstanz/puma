# -*- coding: utf-8 -*-
"""
puma.components.machines.wetbenches.wetbench
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

from lori import Configurations
from lori.components import register_component_type
from puma.components.machines import Machine


# noinspection SpellCheckingInspection
@register_component_type("wetbench")
class WetBench(Machine):
    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        self.data.add(
            key="acidity",
            name="Acidity [pH]",
            type=float,
            connector="dummy",
            generator="random",
            min=0,
            max=2,
        )
