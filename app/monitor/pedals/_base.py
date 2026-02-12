from ...lib.color import *
from ...lib.number import num
from ...telemetry import ac_api
from .._base import Component
from ..lib.chart import Chart
from ..lib.indicator import QuadBar


class Pedal(Component):
    color = white.transparent
    data_key = 0

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
    ) -> None:
        self._chart = Chart(
            x_pos,
            y_pos,
            width,
            height,
            x_axis_marker_color=white.transparent,
            axis_segment_count=8,
            y_axis_marker_length_ratio=1.0,
            bg_char='',
        )
        self._bar = QuadBar(
            chart=self._chart,
            color=self.color,
        )

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        val = ac_api[self.data_key].last[0]

        # plot the indicators
        self._bar.plot(
            num(val).clip(0, 1).f
        )
