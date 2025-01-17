# -*- coding: utf-8 -*-
"""
puma.application.view.machines.depositors.tube
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from typing import Collection, List

import dash_bootstrap_components as dbc
from dash import Input, Output, callback, html

from lori.application.view.pages import ComponentGroup, PageLayout
from puma.application.view.machines.depositors.zone import ThermalZonePage
from puma.components.machines.depositors import ThermalZone, VacuumTube


class VacuumTubePage(ComponentGroup[VacuumTube]):
    # noinspection PyProtectedMember
    def __init__(self, component: VacuumTube, **kwargs) -> None:
        super().__init__(component, children={"zones": ThermalZonePage}, **kwargs)
        for zone in self:
            zone.order += zone._component.index

    @property
    def zones(self) -> List[ThermalZone]:
        return self._component.zones

    def create_layout(self, layout: PageLayout) -> None:
        super().create_layout(layout)
        layout.card.append(self._build_overview())

    def _build_overview(self) -> html.Div:
        @callback(
            Output(f"{self.id}-paddle-temp-mean", "children"),
            Input("view-update", "n_intervals"),
        )
        def _update_overview(*_) -> Collection[dbc.Span]:
            return self._build_mean_temperature()

        return html.Div(
            [
                dbc.Row(dbc.Col(html.H5("Temperature"))),
                dbc.Row(dbc.Col(html.H6("Paddle Mean"))),
                dbc.Row(dbc.Col(id=f"{self.id}-paddle-temp-mean")),
            ],
        )

    def _build_mean_temperature(self) -> Collection[html.Span] | html.Span:
        if all(z.paddle_temp.is_valid() for z in self.zones):
            style = {
                "color": "#ff746c",
                "fontSize": "4rem",
            }
            return [
                html.Span(round(sum(z.paddle_temp.value for z in self.zones) / len(self.zones), 0), style=style),
                html.Span("°C", style=style),
            ]
        else:
            style = {
                "color": "#a9a9a9",
                "fontSize": "3rem",
            }
            return html.Span("IDLE", style=style)
