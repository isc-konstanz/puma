# -*- coding: utf-8 -*-
"""
puma.components.machines.thermal.tube
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from typing import Optional

from lori import Component, Configurations
from puma.components.machines import Machine


class ThermalTube(Component):
    SECTION: str = "tubes"

    number: int

    def __init__(
        self,
        context: Machine,
        number: int,
        configs: Optional[Configurations] = None,
        **kwargs,
    ) -> None:
        super().__init__(context, configs=configs, key=f"tube{number}", name=f"Tube {number}", **kwargs)
        self.number = number
