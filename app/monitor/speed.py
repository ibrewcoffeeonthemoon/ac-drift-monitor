from acsys import CS

import config

from ..lib.color import *
from ..lib.number import num
from ..telemetry import ac_api
from ._base import Monitor
from .lib.canvas import Chart, Region
from .lib.indicator import QuadBar
from .lib.text.big_text import BigText


class SpeedMonitor(Monitor):
    data_keys = (CS.SpeedKMH,)
    enabled = config.SpeedMonitor.enabled
    col_index = config.SpeedMonitor.col_index

    def __init__(
        self,
        x_pos: float,
        y_pos: float,
    ) -> None:
        super().__init__(x_pos, y_pos)

        self._width = width = config.App.span_len*config.SpeedMonitor.col_span
        self._height = height = config.App.height
        self._region = Region(x_pos, y_pos, width, height)
        self._chart = Chart(
            self._region,
            x_axis_segment_count=1,
            y_axis_segment_count=8,
            x_axis_marker_length_ratio=1.0,
            y_axis_marker_length_ratio=1.0,
            bg_char='',
        )
        self._speed_bar_low = QuadBar(
            region=self._region,
            color=green.a2,
        )
        self._speed_bar_high = QuadBar(
            region=self._region,
            color=red.a4,
        )
        self._speed_meter = BigText(
            self._region,
            text='',
            font_color=white.full,
            expected_text_len=3
        )

    @property
    def width(self) -> float: return self._width
    @property
    def height(self) -> float: return self._height

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        speed_kmh = ac_api[CS.SpeedKMH].wma()[0]

        # plot the indicators
        if speed_kmh <= 100:
            self._speed_bar_low.plot(
                num(speed_kmh).normalize(100).clip(0, 1).f,
                color=yellow.a4 if speed_kmh > 50 else green.a4,
            )
        else:
            self._speed_bar_high.plot(
                num(speed_kmh).shift(-100).normalize(200).clip(0, 1).f
            )
        speed_kmh_text = str(round(speed_kmh))
        self._speed_meter.expected_text_len = len(speed_kmh_text)
        self._speed_meter.text = speed_kmh_text
