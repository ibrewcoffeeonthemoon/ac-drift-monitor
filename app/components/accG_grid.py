import ac

from app.components.lib import chart
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
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
        self._height = height
        self._dot_size = dot_size
        self._max_value = max_value
        self._bg_opacity = bg_opacity
        self._x_old = 0.0
        self._z_old = 0.0

    def render(self) -> None:
        # set layouts, styles
        ac.setBackgroundOpacity(window, self._bg_opacity)

        # draw axes
        chart.draw_axes(
            self._x_pos,
            self._y_pos,
            self._width,
            self._height,
            marker_count=3,
            x_axis_marker_length=self._height,
            y_axis_marker_length=self._width,
        )

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

        # draw a centered box on a 2D grid, visualize the g-force
        square(
            (
                self._x_pos + self._width//2 + x*self._width//2,
                self._y_pos + self._height//2 + z*self._height//2
            ),
            length=self._dot_size,
            color4f=(1, 0, 0, 1)
        )
