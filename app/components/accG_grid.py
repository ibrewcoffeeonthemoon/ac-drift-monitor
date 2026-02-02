import ac

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
        def box_pos(val: float, start: int, width: int, box_width: int) -> int:
            scale = width/2
            pos = start + scale + val*scale - box_width/2
            return round(pos)
        ac.glColor4f(1, 0, 0, 1)
        ac.glQuad(
            box_pos(x, self._x_pos, self._width, self._dot_size),
            box_pos(z, self._y_pos, self._height, self._dot_size),
            self._dot_size,
            self._dot_size,
        )
