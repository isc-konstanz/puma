# -*- coding: utf-8 -*-
"""
puma.application.view.machines.machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from lori.application.view.pages import PageGroup, register_component_group
from puma.components.machines import Machine


@register_component_group(Machine, custom=True)
class MachineGroup(PageGroup[Machine]):
    pass
