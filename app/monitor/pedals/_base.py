from ...lib.color import *
from ...lib.number import num
from ...telemetry import ac_api
from .._base import Component
from ..lib.chart import Chart
from ..lib.indicator import QuadBar


class PedalMonitor(Component):
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
        color: Color,
        data_key: int,
        inverted: bool,
    ) -> None:
        self._color = color
        self._data_key = data_key
        self._inverted = inverted
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
        self._bar = QuadBar(
            chart=self._chart,
            color=self._color,
        )

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        val = ac_api[self._data_key].last[0]

        # plot the indicators
        val = 1-val if self._inverted else val
        self._bar.plot(
            num(val).clip(0, 1).f
        )
