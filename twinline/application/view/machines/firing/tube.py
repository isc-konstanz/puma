# -*- coding: utf-8 -*-
"""
twinline.application.view.machines.firing.tube
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from typing import Collection, Tuple

import dash_bootstrap_components as dbc
from dash import Input, Output, callback, html

from lori.application.view.pages import ComponentPage, PageLayout, register_component_page
from twinline.components.machines.firing import FiringTube


@register_component_page(FiringTube)
class FiringTubePage(ComponentPage[FiringTube]):
    def create_layout(self, layout: PageLayout) -> None:
        super().create_layout(layout)

        overview = self._build_overview()
        layout.card.append(overview, focus=True)

        layout.append(dbc.Row(dbc.Col(self._build_temperatures(), width="auto")))

    def _build_overview(
        self,
    ) -> html.Div:
        @callback(
            Output(f"{self.id}-overview", "children"),
            Input("view-update", "n_intervals"),
        )
        def _update_overview(*_) -> Collection[html.Span]:
            return self.get_temperature("temp_mean")

        return html.Div(
            [
                html.H5("Mean Temperature"),
                html.Div(
                    _update_overview(),
                    id=f"{self.id}-overview",
                ),
            ]
        )

    def _build_temperatures(self) -> html.Div:
        @callback(
            Output(f"{self.id}-temp-front", "children"),
            Output(f"{self.id}-temp-back", "children"),
            Input("view-update", "n_intervals"),
        )
        def _update_temperatures(*_) -> Tuple[Collection[html.Span], Collection[html.Span]]:
            return (
                self.get_temperature("temp_front"),
                self.get_temperature("temp_back"),
            )

        return html.Div(
            [
                html.H4("Temperatures"),
                dbc.Row(
                    [
                        dbc.Col(html.H5("Front")),
                        dbc.Col(html.H5("Back")),
                    ],
                    align="start",
                ),
                dbc.Row(
                    [
                        dbc.Col(id=f"{self.id}-temp-front"),
                        dbc.Col(id=f"{self.id}-temp-back"),
                    ],
                    align="start",
                ),
            ]
        )

    def get_temperature(self, key: str) -> Collection[html.Span]:
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
