# -*- coding: utf-8 -*-
"""
twinline.application.view.machines.wetbench
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from typing import Collection

import dash_bootstrap_components as dbc
from dash import Input, Output, callback, html

from lori.application.view.pages import ComponentPage, PageLayout, register_component_page
from twinline.components.machines.wetbenches import WetBench


@register_component_page(WetBench)
class WetBenchPage(ComponentPage[WetBench]):
    def create_layout(self, layout: PageLayout) -> None:
        super().create_layout(layout)

        overview = self._build_overview()
        layout.card.append(overview, focus=True)
        layout.append(dbc.Row(dbc.Col(overview, width="auto")))

    def _build_overview(self) -> html.Div:
        @callback(
            Output(f"{self.id}-overview", "children"),
            Input("view-update", "n_intervals"),
        )
        def _update_overview(*_) -> Collection[html.Span]:
            return self._get_acidity()

        return html.Div(
            [
                html.H5("Bath acidity"),
                html.Div(
                    _update_overview(),
                    id=f"{self.id}-overview",
                ),
            ]
        )

    def _get_acidity(self) -> Collection[html.Span]:
        acidity = self.data.acidity
        value = round(acidity.value, 1) if acidity.is_valid() else dbc.Spinner()
        style = {
            "color": "#f6ac69",
            "fontSize": "4rem",
        }
        return [
            html.Span(value, style=style),
            html.Span("pH", style=style),
        ]
