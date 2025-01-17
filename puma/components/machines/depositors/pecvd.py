# -*- coding: utf-8 -*-
"""
puma.components.machines.depositors.pecvd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

from typing import Collection, List, Optional

from lori import Configurations, Context
from lori.components import Component, register_component_type
from lori.util import get_includes
from puma.components.machines import Machine
from puma.components.machines.depositors.tube import VacuumTube


# noinspection SpellCheckingInspection
@register_component_type("pecvd")
class Pecvd(Machine):
    tubes: List[VacuumTube]

    def __init__(
        self,
        context: Component | Context,
        configs: Optional[Configurations] = None,
        tubes: Collection[VacuumTube] = (),
        **kwargs,
    ) -> None:
        super().__init__(context, configs, **kwargs)
        self.tubes = list(tubes)

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        self.configure_tubes(configs)

    def configure_tubes(self, configs: Configurations) -> None:
        defaults = configs.get_sections(get_includes(VacuumTube))
        configs = configs.get_section(VacuumTube.SECTION, defaults=defaults, ensure_exists=True)
        self.tubes.extend(self.create_tubes(configs, configs.get("number", default=0)))
        for tube in self.tubes:
            tube.configure(configs.get_section(tube.key, defaults=defaults))

    # noinspection PyUnusedLocal
    def create_tubes(self, configs: Configurations, number: int) -> Collection[VacuumTube]:
        return [VacuumTube(self, i) for i in range(1, number + 1)]

    def activate(self) -> None:
        super().activate()
        for tube in self.tubes:
            tube.activate()

    def deactivate(self) -> None:
        super().deactivate()
        for tube in self.tubes:
            tube.deactivate()
