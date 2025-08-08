# -*- coding: utf-8 -*-
"""
twinline.application.view.machines.depositors.pecvd
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""

from __future__ import annotations

from dash import html
from typing import Sequence

from lori.application.view.pages import ComponentGroup, PageLayout, register_component_page
from twinline.components.machines.depositors import Pecvd, VacuumTube


# noinspection PyProtectedMember
@register_component_page(Pecvd)
class PecvdPage(ComponentGroup[Pecvd]):
    @property
    def tubes(self) -> Sequence[VacuumTube]:
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
