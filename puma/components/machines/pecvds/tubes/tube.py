# -*- coding: utf-8 -*-
"""
puma.components.machines.pecvds.tubes.tube_temperature_overview
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


"""
from lori import Component, Configurations, Context
from puma.components.machines.pecvds.tubes import Temperatures


class Tube(Component):
    TYPE: str = "pecvd_tube"
    SECTION: str = "tube"

    temperatures: Temperatures

    def __init__(self, number: int, context: Context, configs: Configurations, *args, **kwargs) -> None:
        super().__init__(context, configs, key=f"tube{number}", name=f"Tube {number}", *args, **kwargs)
        self.temperatures = Temperatures(
            context,
            configs.get_section(
                Temperatures.SECTION,
                defaults={"data": configs.get_section("data")},
                ensure_exists=True
            ),
            key="temperatures",
            name="Temperatures"
        )

    def configure(self, configs: Configurations) -> None:
        super().configure(configs)
        self.temperatures.configure(
            configs.get_section(
                Temperatures.SECTION,
                defaults={"data": configs.get_section("data")},
                ensure_exists=True
            )
        )

    def activate(self) -> None:
        super().activate()
        self.temperatures.activate()

    def deactivate(self) -> None:
        super().deactivate()
        self.temperatures.deactivate()
