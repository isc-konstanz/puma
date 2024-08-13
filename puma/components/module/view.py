# -*- coding: utf-8 -*-
"""
loris.components.machines.view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from typing import Dict, List

from dash import Input, Output, html, callback, dcc
from dash import dash_table as dt

from puma.components.module import ModuleSpecifications
from loris.app.view.pages import ComponentPage, register_component_page


@register_component_page(ModuleSpecifications)
class ModuleSpecificationsPage(ComponentPage[ModuleSpecifications]):

    def _create_content_layout(self) -> html.Div:

        # noinspection PyProtectedMember
        def _get_modules() -> List[Dict]:
            return self._component._read_modules().to_dict("records")

        @callback(Output(f"{self.id}-module-data", "data"),
                  Input(f"{self.id}-module-data-update-interval", "n_intervals"))
        def _update_modules(n_intervals: int):
            return _get_modules()

        return html.Div(
            [
                html.H4(self.name),
                dt.DataTable(
                    id=f"{self.id}-module-data",
                    data=_get_modules(),
                    columns=[{"name": c.name, "id": c.id} for c in self._component.columns]
                ),
                dcc.Interval(
                    id=f"{self.id}-module-data-update-interval",
                    interval=60*1000,
                    n_intervals=0,
                )
            ]
        )
