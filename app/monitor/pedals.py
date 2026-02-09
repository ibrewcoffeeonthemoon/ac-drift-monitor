from acsys import CS

import config

from ..lib.color import *
from ..lib.number import num
from ..telemetry import ac_api
from ._base import Monitor
from .lib.chart import Chart
from .lib.indicator import QuadBar


class PedalsMonitor(Monitor):
    data_keys = (CS.Gas,)
    enabled = config.PedalsMonitor.enabled
    col_index = config.PedalsMonitor.col_index

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
    ) -> None:
        super().__init__(x_pos, y_pos)

        self._width = width = config.App.span_len*config.PedalsMonitor.col_span
        self._height = height = config.App.height

        self._chart = Chart(
            x_pos,
            y_pos,
            width,
            height,
            x_axis_marker_color=white.transparent,
            axis_segment_count=8,
            y_axis_marker_length_ratio=1.0,
            bg_opacity=0.4,
            bg_char='',
        )
        self._gas_bar = QuadBar(
            chart=self._chart,
            color=green.a4,
        )

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        gas = ac_api[CS.Gas].last[0]

        # plot the indicators
        self._gas_bar.plot(
            num(gas).clip(0, 1).f
        )
