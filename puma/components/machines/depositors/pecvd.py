# -*- coding: utf-8 -*-
"""
puma.components.machines.depositors.pecvd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

from lori.components import register_component_type
from puma.components.machines.thermal import ThermalMachine


# noinspection SpellCheckingInspection
@register_component_type("pecvd")
class PECVD(ThermalMachine):
    pass
