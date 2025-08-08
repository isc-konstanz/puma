# -*- coding: utf-8 -*-
"""
twinline.components.machines.depositors.pecvd.zone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from lori import Channel, Configurations
from twinline.components.machines.depositors import ThermalZone


# noinspection SpellCheckingInspection
class CPlasmaZone(ThermalZone):
    SPIKE_TEMP_CONTROL_OUT: str = "spike_temp_control_out"

    @property
    def spike_temp_control_out(self) -> Channel:
        return self.data[self.SPIKE_TEMP_CONTROL_OUT]

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)

        def _add_temperature(key: str, column: str, name: str) -> None:
            self.data.add(
                key=key,
                name=name,
                column=column,
                table="tube_temperature_overview",
                type=float,
            )

        _add_temperature(
            key=self.PADDLE_TEMP,
            column=f"paddle_{self.key}_actual",
            name=f"Paddle {self.name} Temperature [°C]",
        )
        _add_temperature(
            key=self.PADDLE_TEMP_SETPOINT,
            column=f"paddle_{self.key}_setpoint",
            name=f"Paddle {self.name} Setpoint Temperature [°C]",
        )
        _add_temperature(
            key=self.PADDLE_TEMP_SETPOINT_ACTUAL,
            column=f"paddle_{self.key}_act_set",
            name=f"Paddle {self.name} Actual Setpoint Temperature [°C]",
        )

        _add_temperature(
            key=self.SPIKE_TEMP,
            column=f"spike_{self.key}_actual",
            name=f"Spike {self.name} Temperature [°C]",
        )
        _add_temperature(
            key=self.SPIKE_TEMP_SETPOINT,
            column=f"spike_{self.key}_setpoint",
            name=f"Spike {self.name} Setpoint Temperature [°C]",
        )
        _add_temperature(
            key=self.SPIKE_TEMP_SETPOINT_ACTUAL,
            column=f"spike_{self.key}_act_set",
            name=f"Spike {self.name} Actual Setpoint Temperature [°C]",
        )
        _add_temperature(
            key=self.SPIKE_TEMP_CONTROL_OUT,
            column=f"spike_{self.key}_contr_out",
            name=f"Spike {self.name} Control Out Temperature [°C]",
        )
