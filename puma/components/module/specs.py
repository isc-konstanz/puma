# -*- coding: utf-8 -*-
"""
puma.components.module.specs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

import pandas as pd
from loris import Configurations, Resource, Resources
from loris.components import Component, register_component_type


# noinspection SpellCheckingInspection
@register_component_type
class ModuleSpecifications(Component):
    TYPE: str = "modules"

    modules: pd.DataFrame
    columns: Resources

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        database = configs["connectors"]["database"]
        if database["type"].lower() == "csv":
            database["dir"] = str(configs.dirs.conf)

        self.columns = Resources()
        for column in [
            "Name",
            "Technology",
            "Length",
            "Width",
            "N_s",
            "I_mp_ref",
            "V_mp_ref",
            "I_sc_ref",
            "V_oc_ref",
            "alpha_sc",
            "beta_oc",
            "gamma_mp",
        ]:
            self.columns.append(
                Resource(
                    key=column.lower(),
                    name=column,
                    type=str if column in ["Name", "Technology"] else int if column in ["N_s"] else float,
                )
            )

    def activate(self) -> None:
        super().activate()
        self.modules = self.connectors.get_first().read(self.columns)
        for _, module in self.modules.iterrows():
            self._logger.info(f"Read module spec: {module.to_dict()}")

    # def deactivate(self) -> None:
    #     super().deactivate()
