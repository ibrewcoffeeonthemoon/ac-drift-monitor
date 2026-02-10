from acsys import CS

import config

from ..lib.color import *
from ..telemetry import ac_api
from ._base import Monitor
from .lib.chart import Chart
from .lib.indicator.angle_line import AngleLine


class SlipAngleMonitor(Monitor):
    data_keys = (CS.SlipAngle, )
    enabled = config.SlipAngleMonitor.enabled
    col_index = config.SlipAngleMonitor.col_index

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
    ) -> None:
        super().__init__(x_pos, y_pos)

        self._width = width = config.App.span_len*config.SlipAngleMonitor.col_span
        self._height = height = config.App.height

        self._chart = Chart(
            x_pos,
            y_pos,
            width,
            height,
            x_axis_color=white.a7,
            y_axis_color=white.a7,
            axis_segment_count=8,
            x_axis_marker_length_ratio=1.0,
            y_axis_marker_length_ratio=1.0,
            bg_opacity=0.2,
            bg_char='A',
        )
        self._angle_line = AngleLine(
            chart=self._chart,
            color=cyan.a9,
        )

    @property
    def width(self) -> int: return self._width
    @property
    def height(self) -> int: return self._height

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        avg_rear_slipAngle = sum(ac_api[CS.SlipAngle].wma()[-2:])/2

        # plot the indicators
        self._angle_line.plot(avg_rear_slipAngle)
