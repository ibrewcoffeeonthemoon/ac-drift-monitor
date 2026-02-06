import config

from ..data import telemetry
from ..lib.stats import MovingAverage
from ._base import Component
from .lib.chart import Chart
from .lib.indicator import QuadBar


class SpeedMonitor(Component):
    enabled = config.SpeedMonitor.enabled
    col_index = config.SpeedMonitor.col_index

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
    ) -> None:
        self._width = width = config.App.span_len*config.SpeedMonitor.col_span
        self._height = height = config.App.height

        self._chart = Chart(
            x_pos,
            y_pos,
            width,
            height,
            x_axis_marker_color4f=(0, 0, 0, 0.0),
            axis_segment_count=8,
            y_axis_marker_length_ratio=1.0,
            bg_opacity=0.4,
            bg_char='V',
        )
        self._quad_bar = QuadBar(
            chart=self._chart,
            color4f=(1, 0, 0, 0.4),
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
