from app.components.lib.chart import Chart
from app.components.lib.indicator.quad_bar import QuadBar
from app.data import telemetry
from app.lib.stats import MovingAverage


class Slip_Grid:
    def __init__(
        self,
        i_slipRatio: int,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
    ) -> None:
        self._i_slipRatio = i_slipRatio
        self._slipRatio = MovingAverage(scale=3.0)

        self._chart = Chart(
            x_pos,
            y_pos,
            width,
            height,
            x_axis_marker_color4f=(0, 0, 0, 0.0),
            axis_segment_count=4,
            x_axis_marker_length_ratio=1.0,
            y_axis_marker_length_ratio=1.0,
            bg_opacity=0.2,
            bg_char='S',
        )
        self._quad_bar = QuadBar(
            chart=self._chart,
            color4f=(1, 0, 0, 0.4),
            centered_y_scale=True,
        )

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        slipRatio = telemetry.slipRatio[self._i_slipRatio]

        # updadte buffer
        self._slipRatio.update(slipRatio)

        # plot the indicators
        self._quad_bar.plot(self._slipRatio.weighted_average)
