import ac

import config

from ..lib.color import *
from ..telemetry import ac_mem
from ..window import window
from ._base import Component, Monitor
from .lib.canvas import Chart, Region
from .lib.indicator.heat_tile import HeatTile
from .lib.text import BigText


class _TyreMonitor(Component):
    def __init__(
        self,
        i: int,
        region: Region,
    ) -> None:
        self._i = i
        self._region = region
        self._temperature_heat_tile = HeatTile(region.top, low=25, high=125)
        self._temperature_text = BigText(region=region.top, text='', font_color=white.full, expected_text_len=3)
        BigText(region.top.right.right, '°c', white.a7, 3, 'left')
        self._pressure_heat_tile = HeatTile(region.bottom, low=20, high=40)
        self._pressure_text = BigText(region=region.bottom, text='', font_color=white.full, expected_text_len=3)
        BigText(region.bottom.right.right, 'psi', white.a7, 3, 'left')

    def render(self) -> None:
        # fetch telemetry
        temperature = ac_mem.physics.tyreCoreTemperature[self._i]  # type: float
        pressure = ac_mem.physics.wheelsPressure[self._i]  # type: float

        # plot the indicators
        temperature_text = str(round(temperature, 1))
        self._temperature_text.expected_text_len = len(temperature_text)-1
        self._temperature_text.text = temperature_text
        self._temperature_heat_tile.plot(temperature)
        pressure_text = str(round(pressure, 1))
        self._pressure_text.expected_text_len = len(pressure_text)-1
        self._pressure_text.text = pressure_text
        self._pressure_heat_tile.plot(pressure)


class TyreInfoMonitor(Monitor):
    data_keys = ()
    enabled = config.TyreInfoMonitor.enabled
    col_index = config.TyreInfoMonitor.col_index

    def __init__(
        self,
        x_pos: float,
        y_pos: float,
    ) -> None:
        super().__init__(x_pos, y_pos)

        self.width = width = config.App.span_len*config.TyreInfoMonitor.col_span
        self.height = height = config.App.height
        self._region = Region(x_pos, y_pos, width, height)
        self._chart = Chart(
            self._region,
            x_axis_color=white.a7,
            y_axis_color=white.a7,
            y_axis_segment_count=4,
            y_axis_marker_color=white.a5,
            y_axis_marker_length_ratio=1.0,
            x_axis_marker_length_ratio=0.0,
        )
        self._tyre_monitors = [
            _TyreMonitor(i, region)
            for i, region in enumerate((
                self._region.top_left,
                self._region.top_right,
                self._region.bottom_left,
                self._region.bottom_right,
            ))
        ]

    def render(self) -> None:
        self._chart.draw_axes()
        for monitor in self._tyre_monitors:
            monitor.render()
