# -*- coding: utf-8 -*-
"""
puma.components.module.specs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

import random
import threading

from loris import Configurations
from loris.components import Component, register_component_type


# noinspection SpellCheckingInspection
@register_component_type
class Furnace(Component):
    TYPE: str = "furnace"

    timer: threading.Timer

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        self.data.add("temp_low", name=f"{self.name} Temperature Low [0-50]", connector=None, type=int)
        self.data.add("temp_high", name=f"{self.name} Temperature High [30-100]", connector=None, type=float)

    def activate(self) -> None:
        super().activate()
        self.run()
        self.timer = threading.Timer(5.0, self.run)
        self.timer.start()

    def deactivate(self) -> None:
        super().deactivate()
        self.timer.cancel()

    def run(self) -> None:
        self.data.temp_low.value = random.randrange(0, 50)
        self.data.temp_high.value = random.random() * 70. + 30
