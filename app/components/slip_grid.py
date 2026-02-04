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
        self._slipRatio = MovingAverage(max_value=3.0)

        self._chart = Chart(
            x_pos,
            y_pos,
            width,
            height,
            color4f_primary=(0, 0, 0, 0),
            color4f_secondary=(1, 1, 1, 0.1),
            marker_count=3,
            x_axis_marker_length=height,
            y_axis_marker_length=width,
            bg_opacity=0.2,
            bg_char='',
            bg_char_font_size=120,
        )
        self._quad_bar = QuadBar(
            chart=self._chart,
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
