# -*- coding: utf-8 -*-
"""
puma.components.module.specs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

import random

from loris import Configurations
from loris.components import Component


# noinspection SpellCheckingInspection
class ModuleSpecifications(Component):
    TYPE = "module"

    _offset: int = 0

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        self.data.add("random_int", name=f"{self.name} Integer [0-10]", connector=None, value_type=int)
        self.data.add("random_float", name=f"{self.name} Float [0-100]", connector=None, value_type=float)

    def activate(self) -> None:
        super().activate()
        # ToDo:

    def deactivate(self) -> None:
        super().deactivate()
        # ToDo:

    def run(self) -> None:
        self.data.random_int.value = random.randrange(0, 10)
        self.data.random_float.value = random.random() * 100.

    @property
    def type(self) -> str:
        return self.TYPE
