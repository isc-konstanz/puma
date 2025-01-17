# -*- coding: utf-8 -*-
"""
puma.application.view.machines.depositors.zone
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from typing import Collection, Tuple

import dash_bootstrap_components as dbc
from dash import Input, Output, callback, html

from lori import Channel
from lori.application.view.pages import ComponentPage, PageLayout
from puma.components.machines.depositors import ThermalZone


class ThermalZonePage(ComponentPage[ThermalZone]):
    def create_layout(self, layout: PageLayout) -> None:
        super().create_layout(layout)
        layout.card.append(self._build_overview(), focus=True)
        layout.append(self._build_temperatures())

    def _build_overview(self) -> html.Div:
        @callback(
            Output(f"{self.id}-temp", "children"),
            Input("view-update", "n_intervals"),
        )
        def _update_overview(*_) -> Collection[dbc.Span]:
            return self._build_temperature(self.data[ThermalZone.PADDLE_TEMP])

        return html.Div(
            [
                dbc.Row(dbc.Col(html.H5("Temperature"))),
                dbc.Row(dbc.Col(html.H6("Paddle"))),
                dbc.Row(dbc.Col(id=f"{self.id}-temp")),
            ],
        )

    def _build_temperatures(self) -> html.Div:
        temperatures = self.data[
            [
                ThermalZone.PADDLE_TEMP,
                ThermalZone.PADDLE_TEMP_SETPOINT,
                ThermalZone.SPIKE_TEMP,
                ThermalZone.SPIKE_TEMP_SETPOINT,
            ]
        ]

        @callback(
            *[Output(f"{self.id}-{self._encode_id(t.key)}", "children") for t in temperatures],
            Input("view-update", "n_intervals"),
        )
        def _update_temperatures(*_) -> Tuple[Collection[html.Span], ...]:
            return tuple(self._build_temperature(t) for t in temperatures)

        return html.Div(
            [
                dbc.Row(dbc.Col(html.H5("Temperatures"))),
                dbc.Row(
                    [
                        dbc.Col(html.H5("Paddle"), width="auto", style={"min-width": "15rem"}),
                        dbc.Col(html.H5("Paddle Setpoint"), width="auto", style={"min-width": "15rem"}),
                        dbc.Col(html.H5("Spike"), width="auto", style={"min-width": "15rem"}),
                        dbc.Col(html.H5("Spike Setpoint"), width="auto", style={"min-width": "15rem"}),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            self._build_temperature(t),
                            id=f"{self.id}-{self._encode_id(t.key)}",
                            width="auto",
                            style={"min-width": "15rem"},
                        )
                        for t in temperatures
                    ]
                ),
            ]
        )

    @staticmethod
    def _build_temperature(temperature: Channel) -> Collection[html.Span]:
        value = round(temperature.value, 0) if temperature.is_valid() else dbc.Spinner()
        style = {
            "color": "#ff746c",
            "fontSize": "4rem",
        }
        return [
            html.Span(value, style=style),
            html.Span("°C", style=style),
        ]
