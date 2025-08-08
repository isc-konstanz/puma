# -*- coding: utf-8 -*-
"""
twinline.application.view.machines.machine
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from lori.application.view import ComponentGroup
from lori.application.view.pages import PageGroup, register_component_group
from twinline.components.machines import Machine


@register_component_group(Machine, name="Machines")  # , custom=True)
class MachineGroup(ComponentGroup[Machine]):
    pass
