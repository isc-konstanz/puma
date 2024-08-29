# -*- coding: utf-8 -*-
"""
loris.components.machines.view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from loris.app.view.pages import ComponentGroup, register_component_group
from puma.components.machines import Machine


@register_component_group(Machine)
class MachineGroup(ComponentGroup[Machine]):
    pass
