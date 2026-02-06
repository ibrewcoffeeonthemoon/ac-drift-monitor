import config

from ..data import telemetry
from ..lib.stats import MovingAverage
from .base import Component
from .lib.chart import Chart
from .lib.indicator.quad_bar import QuadBar
from .lib.indicator.square_dot import SquareDot


class GForceMonitor(Component):
    enabled = config.GForceMonitor.enabled
    col_index = config.GForceMonitor.col_index

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
    ) -> None:
        self._width = width = config.App.span_len*config.GForceMonitor.col_span
        self._height = height = config.App.height

        self._slipRatio = MovingAverage(scale=3.0, min=0)
        self._x_accG = MovingAverage(scale=1.2)
        self._z_accG = MovingAverage(scale=1.2)

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
        avg_rear_slipRatio = (telemetry.slipRatio.rl+telemetry.slipRatio.rr)/2
        x_accG, _, z_accG = telemetry.accG

        # updadte buffer
        self._slipRatio.update(avg_rear_slipRatio)
        self._x_accG.update(x_accG)
        self._z_accG.update(z_accG)

        # plot the indicators
        self._quad_bar.plot(self._slipRatio.weighted_average)
        self._square_dot.plot(
            x=self._x_accG.weighted_average,
            y=self._z_accG.weighted_average,
        )
