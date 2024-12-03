# -*- coding: utf-8 -*-
"""
puma.components.machines.pecvds.tubes.temperaturs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""
from typing import Any, Dict, Optional, Tuple

from lori import Component, Configurations


class Temperatures(Component):
    """Column Data Field Types and names."""
    TYPE: str = "pecvd_tube_temperatures"
    SECTION: str = "temperatures"

    VALID_FROM: Tuple[str, str] = ("timestamp without time zone", "Valid From [ts]")
    SRC: Tuple[str, str] = ("character varying", "Source")
    TS_DB: Tuple[str, str] = ("timestamp without time zone", "Timestamp of Database [ts]")
    TUBE_NUMBER: Tuple[str, str] = ("smallint", "Tube Number")
    SPIKE_ICEPOINT: Tuple[str, str] = ("double precision", "Spike Icepoint")
    SPIKE_SETPOINT: Tuple[str, str] = ("double precision", "Spike Setpoint")
    SPIKE_ACT_SET: Tuple[str, str] = ("double precision", "Spike Actual Setpoint")
    SPIKE_LZ_SETPOINT: Tuple[str, str] = ("double precision", "Spike LZ Setpoint")
    SPIKE_LZ_ACT_SET: Tuple[str, str] = ("double precision", "Spike LZ Actual Setpoint")
    SPIKE_LZ_ACTUAL: Tuple[str, str] = ("double precision", "Spike LZ Actual")
    SPIKE_LZ_CONTR_OUT: Tuple[str, str] = ("double precision", "Spike LZ Contr Out")
    SPIKE_CENTER_LZ_SETPOINT: Tuple[str, str] = ("double precision", "Spike Center LZ Setpoint")
    SPIKE_CENTER_LZ_ACT_SET: Tuple[str, str] = ("double precision", "Spike Center LZ Actual Setpoint")
    SPIKE_CENTER_LZ_ACTUAL: Tuple[str, str] = ("double precision", "Spike Center LZ Actual")
    SPIKE_CENTER_LZ_CONTR_OUT: Tuple[str, str] = ("double precision", "Spike Center LZ Contr Out")
    SPIKE_CENTER_SETPOINT: Tuple[str, str] = ("double precision", "Spike Center Setpoint")
    SPIKE_CENTER_ACT_SET: Tuple[str, str] = ("double precision", "Spike Center Actual Setpoint")
    SPIKE_CENTER_ACTUAL: Tuple[str, str] = ("double precision", "Spike Center Actual")
    SPIKE_CENTER_CONTR_OUT: Tuple[str, str] = ("double precision", "Spike Center Contr Out")
    SPIKE_CENTER_GZ_SETPOINT: Tuple[str, str] = ("double precision", "Spike Center GZ Setpoint")
    SPIKE_CENTER_GZ_ACT_SET: Tuple[str, str] = ("double precision", "Spike Center GZ Actual Setpoint")
    SPIKE_CENTER_GZ_ACTUAL: Tuple[str, str] = ("double precision", "Spike Center GZ Actual")
    SPIKE_CENTER_GZ_CONTR_OUT: Tuple[str, str] = ("double precision", "Spike Center GZ Contr Out")
    SPIKE_GZ_SETPOINT: Tuple[str, str] = ("double precision", "Spike GZ Setpoint")
    SPIKE_GZ_ACT_SET: Tuple[str, str] = ("double precision", "Spike GZ Actual Setpoint")
    SPIKE_GZ_ACTUAL: Tuple[str, str] = ("double precision", "Spike GZ actual")
    SPIKE_GZ_CONTR_OUT: Tuple[str, str] = ("double precision", "Spike GZ Contr Out")
    PADDLE_ICEPOINT: Tuple[str, str] = ("double precision", "Paddle Icepoint")
    PADDLE_SETPOINT: Tuple[str, str] = ("double precision", "Paddle Setpoint")
    PADDLE_ACT_SET: Tuple[str, str] = ("double precision", "Paddle Actual Setpoint")
    PADDLE_LZ_SETPOINT: Tuple[str, str] = ("double precision", "Paddle LZ Setpoint")
    PADDLE_LZ_ACT_SET: Tuple[str, str] = ("double precision", "Paddle LZ Actual Setpoint")
    PADDLE_LZ_ACTUAL: Tuple[str, str] = ("double precision", "Paddle LZ Actual")
    PADDLE_CENTER_LZ_SETPOINT: Tuple[str, str] = ("double precision", "Paddle Center LZ setpoint")
    PADDLE_CENTER_LZ_ACT_SET: Tuple[str, str] = ("double precision", "Paddle Center LZ Actual Setpoint")
    PADDLE_CENTER_LZ_ACTUAL: Tuple[str, str] = ("double precision", "Paddle Center LZ Actual")
    PADDLE_CENTER_SETPOINT: Tuple[str, str] = ("double precision", "Paddle Center Setpoint")
    PADDLE_CENTER_ACT_SET: Tuple[str, str] = ("double precision", "Paddle Center Actual Setpoint")
    PADDLE_CENTER_ACTUAL: Tuple[str, str] = ("double precision", "Paddle Center Actual")
    PADDLE_CENTER_GZ_SETPOINT: Tuple[str, str] = ("double precision", "Paddle Center GZ setpoint")
    PADDLE_CENTER_GZ_ACT_SET: Tuple[str, str] = ("double precision", "Paddle Center GZ Actual Setpoint")
    PADDLE_CENTER_GZ_ACTUAL: Tuple[str, str] = ("double precision", "Paddle Center GZ actual")
    PADDLE_GZ_SETPOINT: Tuple[str, str] = ("double precision", "Paddle GZ Setpoint")
    PADDLE_GZ_ACT_SET: Tuple[str, str] = ("double precision", "Paddle GZ Actual Setpoint")
    PADDLE_GZ_ACTUAL: Tuple[str, str] = ("double precision", "Paddle GZ Actual")

    desc: Dict[str, Tuple[str, str]] = {
        "valid_from": VALID_FROM,
        "src": SRC,
        "ts_db": TS_DB,
        "tube_number": TUBE_NUMBER,
        "spike_icepoint": SPIKE_ICEPOINT,
        "spike_setpoint": SPIKE_SETPOINT,
        "spike_act_set": SPIKE_ACT_SET,
        "spike_lz_setpoint": SPIKE_LZ_SETPOINT,
        "spike_lz_act_set": SPIKE_LZ_ACT_SET,
        "spike_lz_actual": SPIKE_LZ_ACTUAL,
        "spike_lz_contr_out": SPIKE_LZ_CONTR_OUT,
        "spike_center_lz_setpoint": SPIKE_CENTER_LZ_SETPOINT,
        "spike_center_lz_act_set": SPIKE_CENTER_LZ_ACT_SET,
        "spike_center_lz_actual": SPIKE_CENTER_LZ_ACTUAL,
        "spike_center_lz_contr_out": SPIKE_CENTER_LZ_CONTR_OUT,
        "spike_center_setpoint": SPIKE_CENTER_SETPOINT,
        "spike_center_act_set": SPIKE_CENTER_ACT_SET,
        "spike_center_actual": SPIKE_CENTER_ACTUAL,
        "spike_center_contr_out": SPIKE_CENTER_CONTR_OUT,
        "spike_center_gz_setpoint": SPIKE_CENTER_GZ_SETPOINT,
        "spike_center_gz_act_set": SPIKE_CENTER_GZ_ACT_SET,
        "spike_center_gz_actual": SPIKE_CENTER_GZ_ACTUAL,
        "spike_center_gz_contr_out": SPIKE_CENTER_GZ_CONTR_OUT,
        "spike_gz_setpoint": SPIKE_GZ_SETPOINT,
        "spike_gz_act_set": SPIKE_GZ_ACT_SET,
        "spike_gz_actual": SPIKE_GZ_ACTUAL,
        "spike_gz_contr_out": SPIKE_GZ_CONTR_OUT,
        "paddle_icepoint": PADDLE_ICEPOINT,
        "paddle_setpoint": PADDLE_SETPOINT,
        "paddle_act_set": PADDLE_ACT_SET,
        "paddle_lz_setpoint": PADDLE_LZ_SETPOINT,
        "paddle_lz_act_set": PADDLE_LZ_ACT_SET,
        "paddle_lz_actual": PADDLE_LZ_ACTUAL,
        "paddle_center_lz_setpoint": PADDLE_CENTER_LZ_SETPOINT,
        "paddle_center_lz_act_set": PADDLE_CENTER_LZ_ACT_SET,
        "paddle_center_lz_actual": PADDLE_CENTER_LZ_ACTUAL,
        "paddle_center_setpoint": PADDLE_CENTER_SETPOINT,
        "paddle_center_act_set": PADDLE_CENTER_ACT_SET,
        "paddle_center_actual": PADDLE_CENTER_ACTUAL,
        "paddle_center_gz_setpoint": PADDLE_CENTER_GZ_SETPOINT,
        "paddle_center_gz_act_set": PADDLE_CENTER_GZ_ACT_SET,
        "paddle_center_gz_actual": PADDLE_CENTER_GZ_ACTUAL,
        "paddle_gz_setpoint": PADDLE_GZ_SETPOINT,
        "paddle_gz_act_set": PADDLE_GZ_ACT_SET,
        "paddle_gz_actual": PADDLE_GZ_ACTUAL
    }

    @staticmethod
    def get_info(column_name: Any) -> Optional[Tuple[str, str]]:
        for key, value in Temperatures.desc.items():
            if value[0] == column_name:
                return value
        return None

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)

        # noinspection PyShadowingBuiltins
        def _add_channel(key: str, name: str, **kwargs) -> None:
            self.data.add(key, name=name, type=float, table="tube_temperature_overview", **kwargs)

        # Add all table columns to channels
        for column_name, (_, column_desc) in Temperatures.desc.items():
            _add_channel(column_name, column_desc)
