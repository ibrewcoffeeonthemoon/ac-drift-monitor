from acsys import CS

import config

from ..lib.color import *
from ..lib.number import num
from ..telemetry import telemetry
from ._base import Monitor
from .lib.chart import Chart
from .lib.indicator import QuadBar
from .lib.text.big_text import big_text


class GearMonitor(Monitor):
    data_keys = (CS.Gear, CS.RPM, CS.IsEngineLimiterOn)
    enabled = config.GearMonitor.enabled
    col_index = config.GearMonitor.col_index

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
    ) -> None:
        super().__init__(x_pos, y_pos)

        self._width = width = config.App.span_len*config.GearMonitor.col_span
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
        self._gear_meter = big_text(
            '',
            x_pos, y_pos, width, height,
            font_color=white.full,
            expected_text_len=1
        )
        self._rpm_bar = QuadBar(
            chart=self._chart,
            color=white.a5,
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
        gear = telemetry[CS.Gear].last[0]
        rpm = telemetry[CS.RPM].last[0]
        engine_limited = bool(telemetry[CS.IsEngineLimiterOn].last[0])

        # plot the indicators
        gear_text = str(gear-1) if gear > 1 else 'N' if gear == 1 else 'R'
        self._gear_meter.text = gear_text
        rpm_bar_color = white.a5 if rpm <= 7000 else red.a5 if not engine_limited else red.a8
        self._rpm_bar.plot(
            num(rpm).normalize(10000).clip(0, 1).f,
            color=rpm_bar_color,
        )
