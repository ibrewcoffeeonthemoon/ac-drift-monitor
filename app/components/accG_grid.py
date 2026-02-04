from app.components.lib.chart import Chart
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
        self._x_accG = MovingAverage(max_value=1.2)
        self._z_accG = MovingAverage(max_value=1.2)

        self._chart = Chart(
            x_pos,
            y_pos,
            width,
            height,
            marker_count=3,
            x_axis_marker_length=height,
            y_axis_marker_length=width,
            bg_opacity=0.2,
            bg_char='G',
            bg_char_font_size=360,
        )
        self._square_dot = SquareDot(
            chart=self._chart,
            dot_size=30,
        )

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        x_accG, _, z_accG = telemetry.accG

        # updadte buffer
        self._x_accG.update(x_accG)
        self._z_accG.update(z_accG)

        # plot the indicators
        self._square_dot.plot(
            x=self._x_accG.weighted_average,
            y=self._z_accG.weighted_average,
        )
