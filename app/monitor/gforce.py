from acsys import CS

import config

from ..lib.value import Float
from ..telemetry import telemetry
from ._base import Monitor
from .lib.chart import Chart
from .lib.indicator import QuadBar, SquareDot


class GForceMonitor(Monitor):
    data_keys = (CS.AccG, CS.SlipRatio, )
    enabled = config.GForceMonitor.enabled
    col_index = config.GForceMonitor.col_index

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
    ) -> None:
        super().__init__(x_pos, y_pos)

        self._width = width = config.App.span_len*config.GForceMonitor.col_span
        self._height = height = config.App.height

        self._chart = Chart(
            x_pos,
            y_pos,
            width,
            height,
            x_axis_color4f=(1, 1, 1, 0.7),
            y_axis_color4f=(1, 1, 1, 0.7),
            axis_segment_count=8,
            x_axis_marker_length_ratio=1.0,
            y_axis_marker_length_ratio=1.0,
            bg_opacity=0.2,
            bg_char='G',
        )
        self._quad_bar = QuadBar(
            chart=self._chart,
            color4f=(1, 0, 0, 0.4),
        )
        self._square_dot = SquareDot(
            chart=self._chart,
            dot_size=round(config.GForceMonitor.box_size*self.height),
            inverted_y_scale=True,
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
        avg_rear_slipRatio = sum(telemetry[CS.SlipRatio].wma()[-2:])/2
        x_accG, _, z_accG = telemetry[CS.AccG].wma()

        # plot the indicators
        self._quad_bar.plot(
            Float(avg_rear_slipRatio).normalize(3.0).clip(0, 1).value
        )
        self._square_dot.plot(
            x=Float(x_accG).normalize(1.2).clip(-1, 1).value,
            y=Float(z_accG).normalize(1.2).clip(-1, 1).value,
        )
