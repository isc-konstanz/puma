# -*- coding: utf-8 -*-
"""
puma.components.module.specs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""

from __future__ import annotations

import pandas as pd
from loris import Configurations, Resource, Resources
from loris.components import Component, register_component_type
from loris.connectors import Connector


# noinspection SpellCheckingInspection
@register_component_type
class ModuleSpecifications(Component):
    TYPE: str = "modules"

    _database: str

    modules: pd.DataFrame
    columns: Resources

    @property
    def database(self) -> Connector:
        return self.connectors.get(self._database)

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        self._database = configs.get("database", default="database")
        database_configs = configs["connectors"][self._database]
        if database_configs["type"].lower() == "csv":
            database_configs["dir"] = str(configs.dirs.conf)

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
        self.modules = pd.DataFrame(columns=[c.key for c in self.columns])

    def activate(self) -> None:
        super().activate()
        self.modules = self._read_module_specs()
        for _, module in self.modules.iterrows():
            self._logger.info(f"Read module spec: {module.to_dict()}")

    # def deactivate(self) -> None:
    #     super().deactivate()

    def _read_module_specs(self) -> pd.DataFrame:
        return self.database.read(self.columns)
