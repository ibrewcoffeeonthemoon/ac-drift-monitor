from acsys import CS

import config
from app.monitor.lib.text.big_text import big_text

from ..lib.value import Float
from ..telemetry import telemetry
from ._base import Monitor
from .lib.chart import Chart
from .lib.indicator import QuadBar


class SpeedMonitor(Monitor):
    data_keys = (CS.SpeedKMH,)
    enabled = config.SpeedMonitor.enabled
    col_index = config.SpeedMonitor.col_index

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
    ) -> None:
        super().__init__(x_pos, y_pos)

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
            color4f=(0, 1, 0, 0.4),
        )
        self._speed_meter = big_text(
            '',
            x_pos, y_pos, width, height,
            font_color=(1, 1, 1, 1),
            expected_text_len=3
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
        speed_kmh = telemetry[CS.SpeedKMH].wma()[0]

        # plot the indicators
        self._speed_meter.text = str(round(speed_kmh))
        self._quad_bar.plot(
            Float(speed_kmh).normalize(100).clip(0, 1).value
        )
