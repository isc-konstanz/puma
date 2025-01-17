# -*- coding: utf-8 -*-
"""
puma.components.machines.depositors.pecvd.tube
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from typing import Collection

import pandas as pd
from lori import Channel, Configurations
from puma.components.machines.depositors import VacuumTube
from puma.components.manufacturers.centrotherm.pecvd import CPlasmaZone


# noinspection SpellCheckingInspection
class CPlasmaTube(VacuumTube):
    # VALID_FROM: str = "valid_from"
    # NUMBER: str = "number"
    SOURCE: str = "source"

    PADDLE_TEMP_ICING: str = "paddle_temp_icepoint"
    PADDLE_TEMP_SETPOINT: str = "paddle_temp_setpoint"
    PADDLE_TEMP_SETPOINT_ACTUAL: str = "paddle_temp_actual_setpoint"

    SPIKE_TEMP_ICING: str = "spike_temp_icepoint"
    SPIKE_TEMP_SETPOINT: str = "spike_temp_setpoint"
    SPIKE_TEMP_SETPOINT_ACTUAL: str = "spike_temp_actual_setpoint"

    @property
    def paddle_temp_setpoint(self) -> Channel:
        return self.data[self.PADDLE_TEMP_SETPOINT]

    @property
    def spike_temp_setpoint(self) -> Channel:
        return self.data[self.SPIKE_TEMP_SETPOINT]

    def configure(self, configs: Configurations) -> None:
        channel_section = configs.get_section("data", ensure_exists=True).get_section("channels", ensure_exists=True)
        channel_section["tube_number"] = self.index
        super().configure(configs)

        # self.data.add(
        #     key=self.VALID_FROM,
        #     column="valid_from",
        #     name="Valid From",
        #     table="tube_temperature_overview",
        #     type=pd.Timestamp,
        # )
        # self.data.add(
        #     key=self.NUMBER,
        #     primary=True,
        #     column="tube_number",
        #     attribute="tube_number",
        #     name="Tube Number",
        #     table="tube_temperature_overview",
        #     freq=None,
        #     type=int,
        #     length=2,
        # )
        self.data.add(
            key=self.SOURCE,
            column="src",
            name="Source",
            table="tube_temperature_overview",
            type=str,
            length=6,
        )

        def _add_temperature(key: str, column: str, name: str) -> None:
            self.data.add(
                key=key,
                name=name,
                column=column,
                table="tube_temperature_overview",
                type=float,
            )

        _add_temperature(
            key=self.PADDLE_TEMP_ICING,
            column="paddle_icepoint",
            name="Paddle Icing Temperature [°C]",
        )
        _add_temperature(
            key=self.PADDLE_TEMP_SETPOINT,
            column="paddle_setpoint",
            name="Paddle Setpoint Temperature [°C]",
        )
        _add_temperature(
            key=self.PADDLE_TEMP_SETPOINT_ACTUAL,
            column="paddle_act_set",
            name="Paddle Actual Setpoint Temperature [°C]",
        )

        _add_temperature(
            key=self.SPIKE_TEMP_ICING,
            column="spike_icepoint",
            name="Spike Icing Temperature [°C]",
        )
        _add_temperature(
            key=self.SPIKE_TEMP_SETPOINT,
            column="spike_setpoint",
            name="Spike Setpoint Temperature [°C]",
        )
        _add_temperature(
            key=self.SPIKE_TEMP_SETPOINT_ACTUAL,
            column="spike_act_set",
            name="Spike Actual Setpoint Temperature [°C]",
        )

    def create_zones(self, configs: Configurations) -> Collection[CPlasmaZone]:
        # fmt: off
        return [
            CPlasmaZone(self, 1, key="lz",        name="Load"),
            CPlasmaZone(self, 2, key="center_lz", name="Center Load"),
            CPlasmaZone(self, 3, key="center",    name="Center"),
            CPlasmaZone(self, 4, key="center_gz", name="Center Gas"),
            CPlasmaZone(self, 5, key="gz",        name="Gas"),
        ]
        # fmt: on

    def activate(self) -> None:
        super().activate()
        temperature_channels = [zone.paddle_temp for zone in self.zones]
        self.data.register(self._temperature_callback, *temperature_channels, how="all", unique=True)

    def _temperature_callback(self, data: pd.DataFrame) -> None:
        self._logger.info(f"C.Plasma Tube{self.index} temperatures:\n{data.T}")
