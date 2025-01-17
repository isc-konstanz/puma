# -*- coding: utf-8 -*-
"""
puma.components.machines.thermal.tube
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from lori import Component


class Tube(Component):
    SECTION: str = "tubes"

    index: int

    def __init__(
        self,
        context: Component,
        index: int,
        **kwargs,
    ) -> None:
        super().__init__(
            context,
            key=f"tube{index}",
            name=f"Tube {index}",
            **kwargs,
        )
        self.index = index
