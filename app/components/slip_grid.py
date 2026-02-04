from app.components.lib.chart import Chart
from app.components.lib.indicator.square_dot import SquareDot
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
        dot_size: int,
        max_value: float,
        bg_opacity: float = 0.2,
    ) -> None:
        self._i_slipRatio = i_slipRatio
        self._slipRatio = MovingAverage(max_value)

        self._chart = Chart(
            x_pos,
            y_pos,
            width,
            height,
            dot_size=dot_size,
            color4f_primary=(0, 0, 0, 0),
            color4f_secondary=(1, 1, 1, 0.1),
            marker_count=3,
            x_axis_marker_length=height,
            y_axis_marker_length=width,
            bg_opacity=bg_opacity,
            bg_char='',
            bg_char_font_size=120,
            inverted_y_scale=True,
            centered_y_scale=False,
        )
        self._square_dot = SquareDot(
            chart=self._chart,
            dot_size=dot_size,
            inverted_y_scale=True,
            centered_y_scale=False,
        )

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        slipRatio = telemetry.slipRatio[self._i_slipRatio]

        # updadte buffer
        self._slipRatio.update(slipRatio)

        # plot the indicators
        self._square_dot.plot(
            x=0.0,
            y=self._slipRatio.weighted_average,
        )
