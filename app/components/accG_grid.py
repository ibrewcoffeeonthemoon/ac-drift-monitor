from app.components.lib.chart import Chart
from app.components.lib.indicator.quad_bar import QuadBar
from app.components.lib.indicator.square_dot import SquareDot
from app.data import telemetry
from app.lib.stats import MovingAverage


class AccG_Grid:
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
    ) -> None:
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
            axis_segment_count=6,
            x_axis_marker_length=height,
            y_axis_marker_length=width,
            bg_opacity=0.2,
            bg_char='G',
        )
        self._quad_bar = QuadBar(
            chart=self._chart,
            color4f=(1, 0, 0, 0.4),
        )
        self._square_dot = SquareDot(
            chart=self._chart,
            dot_size=30,
            inverted_y_scale=True,
        )

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
