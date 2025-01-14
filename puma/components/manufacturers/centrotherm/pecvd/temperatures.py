# -*- coding: utf-8 -*-
"""
puma.components.manufacturers.centrotherm.pecvd.temperatures
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from typing import Any, Dict, Optional

from lori import Component, Configurations


# noinspection SpellCheckingInspection
class PlasmaTemperatures(Component):
    SECTION: str = "temperatures"

    # VALID_FROM: str = "valid_from"
    NUMBER: str = "number"
    SOURCE: str = "source"

    SPIKE_ICEPOINT: str = "spike_icepoint"
    SPIKE_SETPOINT: str = "spike_setpoint"
    SPIKE_ACTUAL_SETPOINT: str = "spike_actual_setpoint"

    SPIKE_LZ_SETPOINT: str = "spike_lz_setpoint"
    SPIKE_LZ_ACTUAL_SETPOINT: str = "spike_lz_actual_setpoint"
    SPIKE_LZ_ACTUAL: str = "spike_lz_actual"
    SPIKE_LZ_CONTROL_OUT: str = "spike_lz_control_out"

    SPIKE_CENTER_SETPOINT: str = "spike_center_setpoint"
    SPIKE_CENTER_ACTUAL_SETPOINT: str = "spike_center_actual_setpoint"
    SPIKE_CENTER_ACTUAL: str = "spike_center_actual"
    SPIKE_CENTER_CONTROL_OUT: str = "spike_center_control_out"

    SPIKE_CENTER_LZ_SETPOINT: str = "spike_center_lz_setpoint"
    SPIKE_CENTER_LZ_ACTUAL_SETPOINT: str = "spike_center_lz_actual_setpoint"
    SPIKE_CENTER_LZ_ACTUAL: str = "spike_center_lz_actual"
    SPIKE_CENTER_LZ_CONTROL_OUT: str = "spike_center_lz_control_out"

    SPIKE_CENTER_GZ_SETPOINT: str = "spike_center_gz_setpoint"
    SPIKE_CENTER_GZ_ACTUAL_SETPOINT: str = "spike_center_gz_actual_setpoint"
    SPIKE_CENTER_GZ_ACTUAL: str = "spike_center_gz_actual"
    SPIKE_CENTER_GZ_CONTROL_OUT: str = "spike_center_gz_control_out"

    SPIKE_GZ_SETPOINT: str = "spike_gz_setpoint"
    SPIKE_GZ_ACTUAL_SETPOINT: str = "spike_gz_actual_setpoint"
    SPIKE_GZ_ACTUAL: str = "spike_gz_actual"
    SPIKE_GZ_CONTROL_OUT: str = "spike_gz_control_out"

    PADDLE_ICEPOINT: str = "paddle_icepoint"
    PADDLE_SETPOINT: str = "paddle_setpoint"
    PADDLE_ACTUAL_SETPOINT: str = "paddle_actual_setpoint"

    PADDLE_LZ_SETPOINT: str = "paddle_lz_setpoint"
    PADDLE_LZ_ACTUAL_SETPOINT: str = "paddle_lz_actual_setpoint"
    PADDLE_LZ_ACTUAL: str = "paddle_lz_actual"

    PADDLE_CENTER_LZ_SETPOINT: str = "paddle_center_lz_setpoint"
    PADDLE_CENTER_LZ_ACTUAL_SETPOINT: str = "paddle_center_lz_actual_setpoint"
    PADDLE_CENTER_LZ_ACTUAL: str = "paddle_center_lz_actual"

    PADDLE_CENTER_SETPOINT: str = "paddle_center_setpoint"
    PADDLE_CENTER_ACTUAL_SETPOINT: str = "paddle_center_actual_setpoint"
    PADDLE_CENTER_ACTUAL: str = "paddle_center_actual"

    PADDLE_CENTER_GZ_SETPOINT: str = "paddle_center_gz_setpoint"
    PADDLE_CENTER_GZ_ACTUAL_SETPOINT: str = "paddle_center_gz_actual_setpoint"
    PADDLE_CENTER_GZ_ACTUAL: str = "paddle_center_gz_actual"

    PADDLE_GZ_SETPOINT: str = "paddle_gz_setpoint"
    PADDLE_GZ_ACTUAL_SETPOINT: str = "paddle_gz_actual_setpoint"
    PADDLE_GZ_ACTUAL: str = "paddle_gz_actual"

    DESC: Dict[str, Dict[str, Any]] = {
        # VALID_FROM: {
        #     "column": "valid_from",
        #     "name": "Valid From",
        #     "type": pd.Timestamp,
        # },
        NUMBER: {
            "primary": True,
            "column": "tube_number",
            "attribute": "tube_number",
            "name": "Tube Number",
            "freq": None,
            "type": int,
            "length": 2,
        },
        SOURCE: {
            "column": "src",
            "name": "Source",
            "type": str,
            "length": 6,
        },
        SPIKE_ICEPOINT: {
            "column": "spike_icepoint",
            "name": "Spike Icepoint",
            "type": float,
        },
        SPIKE_SETPOINT: {
            "column": "spike_setpoint",
            "name": "Spike Setpoint",
            "type": float,
        },
        SPIKE_ACTUAL_SETPOINT: {
            "column": "spike_act_set",
            "name": "Spike Actual Setpoint",
            "type": float,
        },
        SPIKE_LZ_SETPOINT: {
            "column": "spike_lz_setpoint",
            "name": "Spike LZ Setpoint",
            "type": float,
        },
        SPIKE_LZ_ACTUAL_SETPOINT: {
            "column": "spike_lz_act_set",
            "name": "Spike LZ Actual Setpoint",
            "type": float,
        },
        SPIKE_LZ_ACTUAL: {
            "column": "spike_lz_actual",
            "name": "Spike LZ Actual",
            "type": float,
        },
        SPIKE_LZ_CONTROL_OUT: {
            "column": "spike_lz_contr_out",
            "name": "Spike LZ Contr Out",
            "type": float,
        },
        SPIKE_CENTER_LZ_SETPOINT: {
            "column": "spike_center_lz_setpoint",
            "name": "Spike Center LZ Setpoint",
            "type": float,
        },
        SPIKE_CENTER_LZ_ACTUAL_SETPOINT: {
            "column": "spike_center_lz_act_set",
            "name": "Spike Center LZ Actual Setpoint",
            "type": float,
        },
        SPIKE_CENTER_LZ_ACTUAL: {
            "column": "spike_center_lz_actual",
            "name": "Spike Center LZ Actual",
            "type": float,
        },
        SPIKE_CENTER_LZ_CONTROL_OUT: {
            "column": "spike_center_lz_contr_out",
            "name": "Spike Center LZ Contr Out",
            "type": float,
        },
        SPIKE_CENTER_SETPOINT: {
            "column": "spike_center_setpoint",
            "name": "Spike Center Setpoint",
            "type": float,
        },
        SPIKE_CENTER_ACTUAL_SETPOINT: {
            "column": "spike_center_act_set",
            "name": "Spike Center Actual Setpoint",
            "type": float,
        },
        SPIKE_CENTER_ACTUAL: {
            "column": "spike_center_actual",
            "name": "Spike Center Actual",
            "type": float,
        },
        SPIKE_CENTER_CONTROL_OUT: {
            "column": "spike_center_contr_out",
            "name": "Spike Center Contr Out",
            "type": float,
        },
        SPIKE_CENTER_GZ_SETPOINT: {
            "column": "spike_center_gz_setpoint",
            "name": "Spike Center GZ Setpoint",
            "type": float,
        },
        SPIKE_CENTER_GZ_ACTUAL_SETPOINT: {
            "column": "spike_center_gz_act_set",
            "name": "Spike Center GZ Actual Setpoint",
            "type": float,
        },
        SPIKE_CENTER_GZ_ACTUAL: {
            "column": "spike_center_gz_actual",
            "name": "Spike Center GZ Actual",
            "type": float,
        },
        SPIKE_CENTER_GZ_CONTROL_OUT: {
            "column": "spike_center_gz_contr_out",
            "name": "Spike Center GZ Contr Out",
            "type": float,
        },
        SPIKE_GZ_SETPOINT: {
            "column": "spike_gz_setpoint",
            "name": "Spike GZ Setpoint",
            "type": float,
        },
        SPIKE_GZ_ACTUAL_SETPOINT: {
            "column": "spike_gz_act_set",
            "name": "Spike GZ Actual Setpoint",
            "type": float,
        },
        SPIKE_GZ_ACTUAL: {
            "column": "spike_gz_actual",
            "name": "Spike GZ actual",
            "type": float,
        },
        SPIKE_GZ_CONTROL_OUT: {
            "column": "spike_gz_contr_out",
            "name": "Spike GZ Contr Out",
            "type": float,
        },
        PADDLE_ICEPOINT: {
            "column": "paddle_icepoint",
            "name": "Paddle Icepoint",
            "type": float,
        },
        PADDLE_SETPOINT: {
            "column": "paddle_setpoint",
            "name": "Paddle Setpoint",
            "type": float,
        },
        PADDLE_ACTUAL_SETPOINT: {
            "column": "paddle_act_set",
            "name": "Paddle Actual Setpoint",
            "type": float,
        },
        PADDLE_LZ_SETPOINT: {
            "column": "paddle_lz_setpoint",
            "name": "Paddle LZ Setpoint",
            "type": float,
        },
        PADDLE_LZ_ACTUAL_SETPOINT: {
            "column": "paddle_lz_act_set",
            "name": "Paddle LZ Actual Setpoint",
            "type": float,
        },
        PADDLE_LZ_ACTUAL: {
            "column": "paddle_lz_actual",
            "name": "Paddle LZ Actual",
            "type": float,
        },
        PADDLE_CENTER_LZ_SETPOINT: {
            "column": "paddle_center_lz_setpoint",
            "name": "Paddle Center LZ setpoint",
            "type": float,
        },
        PADDLE_CENTER_LZ_ACTUAL_SETPOINT: {
            "column": "paddle_center_lz_act_set",
            "name": "Paddle Center LZ Actual Setpoint",
            "type": float,
        },
        PADDLE_CENTER_LZ_ACTUAL: {
            "column": "paddle_center_lz_actual",
            "name": "Paddle Center LZ Actual",
            "type": float,
        },
        PADDLE_CENTER_SETPOINT: {
            "column": "paddle_center_setpoint",
            "name": "Paddle Center Setpoint",
            "type": float,
        },
        PADDLE_CENTER_ACTUAL_SETPOINT: {
            "column": "paddle_center_act_set",
            "name": "Paddle Center Actual Setpoint",
            "type": float,
        },
        PADDLE_CENTER_ACTUAL: {
            "column": "paddle_center_actual",
            "name": "Paddle Center Actual",
            "type": float,
        },
        PADDLE_CENTER_GZ_SETPOINT: {
            "column": "paddle_center_gz_setpoint",
            "name": "Paddle Center GZ setpoint",
            "type": float,
        },
        PADDLE_CENTER_GZ_ACTUAL_SETPOINT: {
            "column": "paddle_center_gz_act_set",
            "name": "Paddle Center GZ Actual Setpoint",
            "type": float,
        },
        PADDLE_CENTER_GZ_ACTUAL: {
            "column": "paddle_center_gz_actual",
            "name": "Paddle Center GZ actual",
            "type": float,
        },
        PADDLE_GZ_SETPOINT: {
            "column": "paddle_gz_setpoint",
            "name": "Paddle GZ Setpoint",
            "type": float,
        },
        PADDLE_GZ_ACTUAL_SETPOINT: {
            "column": "paddle_gz_act_set",
            "name": "Paddle GZ Actual Setpoint",
            "type": float,
        },
        PADDLE_GZ_ACTUAL: {
            "column": "paddle_gz_actual",
            "name": "Paddle GZ Actual",
            "type": float,
        },
    }

    def __init__(
        self,
        context: Component,
        configs: Optional[Configurations] = None,
        **kwargs,
    ) -> None:
        super().__init__(context, configs, key="temperatures", name="Tube Temperatures", **kwargs)

    @staticmethod
    def get_info(key: str) -> Optional[Dict[str, Any]]:
        return PlasmaTemperatures.DESC.get(key, None)

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)

        for key, channel in PlasmaTemperatures.DESC.items():
            self.data.add(key, **channel)
