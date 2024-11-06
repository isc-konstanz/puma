# -*- coding: utf-8 -*-
"""
puma.application.view.machines.furnace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from typing import Collection, Tuple

import dash_bootstrap_components as dbc
from dash import Input, Output, callback, dcc, html

from lori.application.view.pages import ComponentPage, PageLayout, register_component_page
from puma.components.machines.furnaces import Furnace


@register_component_page(Furnace)
class FurnacePage(ComponentPage[Furnace]):
    def create_layout(self, layout: PageLayout) -> None:
        super().create_layout(layout)

        overview = self._build_overview()
        layout.card.append(overview, focus=True)

        layout.append(dbc.Row(dbc.Col(self._build_tubes(), width="auto")))

    def _build_tubes(self) -> html.Div:
        @callback(
            Output(f"{self.id}-tube-temp-front", "children"),
            Output(f"{self.id}-tube-temp-back", "children"),
            Input(f"{self.id}-tube-temp-update", "n_intervals"),
        )
        def _update_tubes(*_) -> Tuple[Collection[html.Span], Collection[html.Span]]:
            return (
                self._get_temperatures("tube_temp_front"),
                self._get_temperatures("tube_temp_back"),
            )

        return html.Div(
            [
                html.H4("Tube temperatures"),
                dbc.Row(
                    [
                        dbc.Col(html.H5("Front")),
                        dbc.Col(html.H5("Back")),
                    ],
                    align="start",
                ),
                dbc.Row(
                    [
                        dbc.Col(id=f"{self.id}-tube-temp-front"),
                        dbc.Col(id=f"{self.id}-tube-temp-back"),
                    ],
                    align="start",
                ),
                dcc.Interval(
                    id=f"{self.id}-tube-temp-update",
                    interval=1000,
                    n_intervals=0,
                ),
            ]
        )

    def _build_overview(self) -> html.Div:
        @callback(
            Output(f"{self.id}-overview", "children"),
            Input(f"{self.id}-overview-update", "n_intervals"),
        )
        def _update_overview(*_) -> Collection[html.Span]:
            return self._get_temperatures("tube_temp_mean")

        return html.Div(
            [
                html.H5("Tube temperature"),
                html.Div(
                    _update_overview(),
                    id=f"{self.id}-overview",
                ),
                dcc.Interval(
                    id=f"{self.id}-overview-update",
                    interval=1000,
                    n_intervals=0,
                ),
            ]
        )

    def _get_temperatures(self, key: str) -> Collection[html.Span]:
        temperature = self.data[key]
        value = round(temperature.value, 0) if temperature.is_valid() else dbc.Spinner()
        style = {
            "color": "#ff746c",
            "fontSize": "4rem",
        }
        return [
            html.Span(value, style=style),
            html.Span("°C", style=style),
        ]
