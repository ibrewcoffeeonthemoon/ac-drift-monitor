from app.lib.color import *
from app.lib.number import num
from app.monitor._base import Component
from app.monitor.lib.canvas import Chart, Region
from app.monitor.lib.indicator import QuadBar
from app.telemetry import ac_api


class Pedal(Component):
    color = white.transparent
    data_key = 0

    def __init__(
        self,
        x_pos: float,
        y_pos: float,
        width: float,
        height: float,
    ) -> None:
        self._region = Region(x_pos, y_pos, width, height)
        self._chart = Chart(
            self._region,
            x_axis_segment_count=1,
            y_axis_segment_count=1,
            x_axis_marker_length_ratio=1.0,
            y_axis_marker_length_ratio=1.0,
            bg_char='',
        )
        self._bar = QuadBar(
            region=self._region,
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
