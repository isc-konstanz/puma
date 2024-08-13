# -*- coding: utf-8 -*-
"""
loris.components.machines.view
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from typing import Collection

import dash_bootstrap_components as dbc
from dash import Input, Output, html, callback, dcc

from puma.components.machines import Furnace, Machine
from loris.app.view.pages import ComponentGroup, ComponentPage, register_component_group, register_component_page


@register_component_page(Furnace)
class FurnacePage(ComponentPage[Furnace]):

    def _create_focus_layout(self) -> html.Div:

        def _get_temperatures() -> Collection[html.Col]:
            style = {
                "color": "#f6ac69",
                "fontSize": "5rem"
            }
            return [
                dbc.Col(html.Span(f"{round(self.data.temp_low.value, 2)}°C", style=style), width=3),
                dbc.Col(html.Span(f"{round(self.data.temp_high.value, 2)}°C", style=style), width=3),
            ]

        @callback(Output(f"{self.id}-temp-data", "children"),
                  Input(f"{self.id}-temp-data-update-interval", "n_intervals"))
        def _update_data(n_intervals: int):
            return _get_temperatures()

        return html.Div(
            [
                html.H4(self.name),
                dbc.Row(
                    [
                        dbc.Col(html.H5("Low"), width=3),
                        dbc.Col(html.H5("High"), width=3),
                    ],
                ),
                dbc.Row(id=f"{self.id}-temp-data"),
                dcc.Interval(
                    id=f"{self.id}-temp-data-update-interval",
                    interval=1000,
                    n_intervals=0,
                ),
            ]
        )


@register_component_group(Machine)
class MachineGroup(ComponentGroup[Machine]):
    pass
