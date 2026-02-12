from acsys import CS

import config

from ..lib.color import *
from ..lib.number import num
from ..telemetry import ac_api, ac_mem
from ._base import Monitor
from .lib.canvas import Chart
from .lib.indicator import QuadBar
from .lib.text.big_text import big_text


class GearMonitor(Monitor):
    data_keys = (CS.Gear, CS.RPM, CS.IsEngineLimiterOn)
    enabled = config.GearMonitor.enabled
    col_index = config.GearMonitor.col_index

    def __init__(
        self,
        x_pos: float,
        y_pos: float,
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
            bg_char='',
        )
        self._gear_meter = big_text(
            x_pos, y_pos, width, height,
            text='',
            font_color=white.full,
            expected_text_len=1
        )
        self._rpm_bar = QuadBar(
            region=self._chart.region,
            color=white.a5,
        )

    @property
    def width(self) -> float: return self._width
    @property
    def height(self) -> float: return self._height

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        gear = ac_api[CS.Gear].last[0]
        rpm = ac_api[CS.RPM].last[0]
        engine_limited = bool(ac_api[CS.IsEngineLimiterOn].last[0])

        # plot the indicators
        gear_text = (
            str(gear-1) if gear > 1 else
            'N' if gear == 1 else
            'R'
        )
        self._gear_meter.text = gear_text
        maxRpm = ac_mem.static.maxRpm  # type: float
        rpm_bar_color = (
            white.a5 if rpm <= maxRpm*0.9 else
            red.a5 if not engine_limited else
            red.a8
        )
        self._rpm_bar.plot(
            num(rpm).normalize(maxRpm).clip(0, 1).f,
            color=rpm_bar_color,
        )
