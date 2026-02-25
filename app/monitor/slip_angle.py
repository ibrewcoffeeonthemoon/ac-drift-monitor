from acsys import CS

import config
from app.lib.color import *
from app.lib.number import num
from app.telemetry import ac_api

from ._base import Monitor
from .lib.canvas import Chart, Region
from .lib.indicator import AngleQuad


class SlipAngleMonitor(Monitor):
    data_keys = (CS.SlipAngle, CS.Steer)
    enabled = config.SlipAngleMonitor.enabled
    col_index = config.SlipAngleMonitor.col_index

    def __init__(
        self,
        x_pos: float,
        y_pos: float,
    ) -> None:
        super().__init__(x_pos, y_pos)

        self.width = width = config.App.span_len*config.SlipAngleMonitor.col_span
        self.height = height = config.App.height
        self._region = Region(x_pos, y_pos, width, height)
        self._chart = Chart(
            self._region,
            x_axis_color=white.a7,
            y_axis_color=white.a7,
            x_axis_segment_count=4,
            y_axis_segment_count=4,
            x_axis_marker_length_ratio=1.0,
            y_axis_marker_length_ratio=1.0,
            bg_char='A',
        )
        self._slip_angle_quad = AngleQuad(
            region=self._region,
            sensitivity=config.SlipAngleMonitor.sensitivity,
            reversed=True,
            color=cyan.a5,
        )
        self._steering_angle_quad = AngleQuad(
            region=self._region,
            sensitivity=(
                num(config.SlipAngleMonitor.sensitivity)
                .normalize(config.SlipAngleMonitor.wheel_degree/180).f
            ),
            reversed=True,
            color=blue.a5,
        )

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        avg_rear_slipAngle_degree = sum(ac_api[CS.SlipAngle].wma()[-2:])/2
        steer_angle_degree = ac_api[CS.Steer].last[0]

        # plot the indicators
        self._slip_angle_quad.plot(avg_rear_slipAngle_degree)
        self._steering_angle_quad.plot(steer_angle_degree)
