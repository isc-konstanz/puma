# -*- coding: utf-8 -*-
"""
loris.components.machines.view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from typing import Dict, List

import dash_bootstrap_components as dbc
from dash import Input, Output, callback
from dash import dash_table as dt
from dash import dcc, html

import pandas as pd
from loris import Connector
from loris.app.view.pages import ComponentPage, PageLayout, register_component_page
from puma.components.module import ModuleSpecifications


@register_component_page(ModuleSpecifications)
class ModuleSpecificationsPage(ComponentPage[ModuleSpecifications]):
    order: int = 90

    @property
    def database(self) -> Connector:
        return self._component.database

    # noinspection PyProtectedMember
    def read_module_specs(self) -> pd.DataFrame:
        # return self.database.read()
        return self._component._read_module_specs()

    def create_layout(self, layout: PageLayout) -> None:
        super().create_layout(layout)

        @callback(Output(f"{self.id}-module-specs", "data"),
                  Input(f"{self.id}-module-specs-update", "n_intervals"))
        def _update_specs(*_) -> List[Dict]:
            return self.read_module_specs().to_dict("records")

        overview = self._build_overview()
        layout.card.append(overview, focus=True)
        layout.append(
            dbc.Row(
                dbc.Col(overview, width="auto")
            )
        )

        layout.append(html.Hr())
        layout.append(
            dbc.Row(
                dbc.Col(
                    html.Div(
                        [
                            dt.DataTable(
                                id=f"{self.id}-module-specs",
                                data=self._component.modules.to_dict("records"),
                                columns=[{"name": c.name, "id": c.id} for c in self._component.columns],
                            ),
                            dcc.Interval(
                                id=f"{self.id}-module-specs-update",
                                interval=60 * 1000,
                                n_intervals=0,
                            ),
                        ]
                    ),
                    width="auto",
                )
            )
        )

    def _build_overview(self) -> html.Div:

        @callback(Output(f"{self.id}-modules-overview", "children"),
                  Input(f"{self.id}-modules-overview-update", "n_intervals"))
        def _update_overview(*_) -> html.Span:
            module_specs = self.read_module_specs()
            return html.Span(len(module_specs.index), style={"fontSize": "4rem"})

        return html.Div(
            [
                html.H5("Database entries"),
                html.Div(
                    dbc.Spinner(),
                    id=f"{self.id}-modules-overview",
                ),
                dcc.Interval(
                    id=f"{self.id}-modules-overview-update",
                    interval=60 * 1000,
                    n_intervals=0,
                ),
            ]
        )
