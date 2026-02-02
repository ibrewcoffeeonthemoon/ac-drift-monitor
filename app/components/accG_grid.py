import ac

from app.components.lib.chart import Chart
from app.components.lib.gl.shape import square
from app.data import telemetry
from app.window import window


class AccG_Grid:
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
        dot_size: int,
        max_value: float = 1.5,
        bg_opacity: float = 0.2,
    ) -> None:
        self._max_value = max_value
        self._bg_opacity = bg_opacity
        self._x_old = 0.0
        self._z_old = 0.0
        self._chart = Chart(
            x_pos,
            y_pos,
            width,
            height,
            dot_size=dot_size,
            marker_count=3,
            x_axis_marker_length=height,
            y_axis_marker_length=width,
        )

    def render(self) -> None:
        # set layouts, styles
        ac.setBackgroundOpacity(window, self._bg_opacity)

        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        x_raw, _, z_raw = telemetry.accG

        # normalize
        x_normalized = x_raw/self._max_value
        z_normalized = z_raw/self._max_value

        # clipping
        x_clipped = min(max(x_normalized, -1.0), +1.0)
        z_clipped = min(max(z_normalized, -1.0), +1.0)

        # smoothing
        weight = 0.8
        x = weight * x_clipped + (1-weight) * self._x_old
        z = weight * z_clipped + (1-weight) * self._z_old
        self._x_old = x_clipped
        self._z_old = z_clipped

        # plot the G-force value on chart
        self._chart.plot(x=x, y=z)
