# -*- coding: utf-8 -*-
"""
puma.components.module.specs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

import random
from threading import Event, Thread

from loris import Configurations
from loris.components import Component, register_component_type


# noinspection SpellCheckingInspection
@register_component_type
class Furnace(Component, Thread):
    TYPE: str = "furnace"

    _interval: int = 1
    __interrupt: Event = Event()

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        self.data.add("temp_low", name=f"{self.name} Temperature Low [0-50]", connector=None, type=int)
        self.data.add("temp_high", name=f"{self.name} Temperature High [30-100]", connector=None, type=float)

    def activate(self) -> None:
        super().activate()
        self.__interrupt.clear()
        self.start()

    def deactivate(self) -> None:
        super().deactivate()
        self.interrupt()

    def interrupt(self) -> None:
        self.__interrupt.set()

    def run(self) -> None:
        while not self.__interrupt.is_set():
            try:
                if self.data.temp_low.is_valid():
                    self.data.temp_low.value = int(_lim(0, self.data.temp_low.value + random.randrange(-10, 10)/10, 50))
                else:
                    self.data.temp_low.value = random.randrange(0, 50)

                if self.data.temp_high.is_valid():
                    self.data.temp_high.value = _lim(30, self.data.temp_high.value + random.randrange(-50, 50)/10., 70)
                else:
                    self.data.temp_high.value = random.random() * 70. + 30

                self.__interrupt.wait(self._interval)

            except KeyboardInterrupt:
                self.interrupt()
                break


def _lim(min_val, val, max_val):
    if val <= min_val:
        return min_val
    if val >= max_val:
        return max_val
    return val
