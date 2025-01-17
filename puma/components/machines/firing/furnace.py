# -*- coding: utf-8 -*-
"""
puma.components.machines.firing.furnace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

from typing import Collection, List, Optional

from lori import Component, Configurations, Context
from lori.components import register_component_type
from lori.util import get_includes
from puma.components.machines import Machine
from puma.components.machines.firing.tube import FiringTube


@register_component_type("furnace", "firing_furnace")
class FiringFurnace(Machine):
    tubes: List[FiringTube]

    def __init__(
        self,
        context: Component | Context,
        configs: Optional[Configurations] = None,
        tubes: Collection[FiringTube] = (),
        **kwargs,
    ) -> None:
        super().__init__(context, configs, **kwargs)
        self.tubes = list(tubes)

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        self.configure_tubes(configs)

    def configure_tubes(self, configs: Configurations) -> None:
        defaults = configs.get_sections(get_includes(FiringTube))
        configs = configs.get_section(FiringTube.SECTION, defaults=defaults, ensure_exists=True)
        self.tubes.extend(self.create_tubes(configs, configs.get("number", default=0)))
        for tube in self.tubes:
            tube.configure(configs.get_section(tube.key, defaults=defaults))

    # noinspection PyUnusedLocal
    def create_tubes(self, configs: Configurations, number: int) -> Collection[FiringTube]:
        return [FiringTube(self, i) for i in range(1, number + 1)]

    def activate(self) -> None:
        super().activate()
        for tube in self.tubes:
            tube.activate()

    def deactivate(self) -> None:
        super().deactivate()
        for tube in self.tubes:
            tube.deactivate()
