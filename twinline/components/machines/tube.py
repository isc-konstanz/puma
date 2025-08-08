# -*- coding: utf-8 -*-
"""
twinline.components.machines.thermal.tube
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from lori import Component, Configurations


class Tube(Component):
    SECTION: str = "tubes"

    index: int

    def __init__(
        self,
        context: Component,
        configs: Configurations,
        index: int,
        **kwargs,
    ) -> None:
        super().__init__(
            context,
            configs,
            key=f"tube{index}",
            name=f"Tube {index}",
            **kwargs,
        )
        self.index = index
