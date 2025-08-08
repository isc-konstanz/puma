# -*- coding: utf-8 -*-
"""
twinline.application.view.machines.firing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from dash import html
from typing import Sequence

from lori.application.view.pages import ComponentGroup, PageLayout, register_component_page
from twinline.components.machines.firing import FiringFurnace, FiringTube


# noinspection PyProtectedMember
@register_component_page(FiringFurnace)
class FiringFurnacePage(ComponentGroup[FiringFurnace]):
    @property
    def tubes(self) -> Sequence[FiringTube]:
        return self._component.tubes

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
