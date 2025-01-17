# -*- coding: utf-8 -*-
"""
puma.application.view.machines.firing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from dash import html

from lori.application.view.pages import ComponentGroup, PageLayout, register_component_page
from puma.application.view.machines.firing.tube import FiringTubePage
from puma.components.machines.firing import FiringFurnace


# noinspection PyProtectedMember
@register_component_page(FiringFurnace, children={"tubes": FiringTubePage})
class FiringFurnacePage(ComponentGroup[FiringFurnace]):
    def create_layout(self, layout: PageLayout) -> None:
        super().create_layout(layout)

        layout.card.append(self._build_tubes(), focus=True)

    def _build_tubes(self) -> html.Div:
        return html.Div(
            [
                html.H5("Tubes"),
                html.Span(len(self._component.tubes), style={"fontSize": "4rem"}),
            ],
        )
