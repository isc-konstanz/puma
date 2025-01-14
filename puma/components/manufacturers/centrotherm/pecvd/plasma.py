# -*- coding: utf-8 -*-
"""
puma.components.manufacturers.centrotherm.pecvd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

from lori import Configurations
from lori.components import register_component_type
from lori.util import get_includes
from puma.components.machines.depositors import PECVD
from puma.components.manufacturers.centrotherm.pecvd import PlasmaTube

TYPE: str = "c_plasma"


@register_component_type(TYPE)
class CPlasma(PECVD):

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        tubes = configs.get_section(
            PlasmaTube.SECTION,
            defaults=configs.get(get_includes(PlasmaTube)),
            ensure_exists=True
        )
        for i in range(1, tubes.get("number", default=0) + 1):
            tube_configs = tubes.get_section(f"{i}", defaults=tubes.get(get_includes(PlasmaTube)))
            tube = PlasmaTube(self, i)
            tube.configure(tube_configs)
            self.tubes.append(tube)
