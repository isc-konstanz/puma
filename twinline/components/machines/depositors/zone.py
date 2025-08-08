# -*- coding: utf-8 -*-
"""
twinline.components.machines.depositors.zone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from lori import Channel, Component, Configurations
from lori.util import parse_name, validate_key


# noinspection SpellCheckingInspection
class ThermalZone(Component):
    SECTION: str = "zones"

    PADDLE_TEMP: str = "paddle_temp"
    PADDLE_TEMP_SETPOINT: str = "paddle_temp_set"
    PADDLE_TEMP_SETPOINT_ACTUAL: str = "paddle_temp_set_act"

    SPIKE_TEMP: str = "spike_temp"
    SPIKE_TEMP_SETPOINT: str = "spike_temp_set"
    SPIKE_TEMP_SETPOINT_ACTUAL: str = "spike_temp_set_act"

    index: int

    def __init__(
        self,
        context: Component,
        configs: Configurations,
        index: int,
        key: str,
        name: str,
        **kwargs,
    ) -> None:
        super().__init__(
            context,
            configs,
            key=f"zone{index}" if key is None else validate_key(key),
            name=f"Zone {index}" if name is None else f"{parse_name(key) if name is None else name} Zone",
            **kwargs,
        )
        self.index = index

    @property
    def paddle_temp(self) -> Channel:
        return self.data[self.PADDLE_TEMP]

    @property
    def paddle_temp_setpoint(self) -> Channel:
        return self.data[self.PADDLE_TEMP_SETPOINT]

    @property
    def paddle_temp_actual_setpoint(self) -> Channel:
        return self.data[self.PADDLE_TEMP_SETPOINT_ACTUAL]

    @property
    def spike_temp(self) -> Channel:
        return self.data[self.SPIKE_TEMP]

    @property
    def spike_temp_setpoint(self) -> Channel:
        return self.data[self.SPIKE_TEMP_SETPOINT]

    @property
    def spike_temp_actual_setpoint(self) -> Channel:
        return self.data[self.SPIKE_TEMP_SETPOINT_ACTUAL]
