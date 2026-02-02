import ac

from app.data import telemetry


class AccG_Grid:
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
        dot_size: int,
    ) -> None:
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
        self._height = height
        self._dot_size = dot_size

    def render(self) -> None:
        ac.glColor4f(1, 0, 0, 1)
        x, _, z = telemetry.accG
        x_pos = self._x_pos + self._width//2 * (1+x)
        y_pos = self._y_pos + self._height//2 * (1+z)
        dot_width = dot_height = self._dot_size
        ac.glQuad(x_pos, y_pos, dot_width, dot_height)
