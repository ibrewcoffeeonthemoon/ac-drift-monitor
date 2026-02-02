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
        dot_width = dot_height = self._dot_size
        x_pos = self._x_pos - dot_width//2 + self._width//2 * (1+x)
        y_pos = self._y_pos - dot_height//2 + self._height//2 * (1+z)
        ac.glQuad(x_pos, y_pos, dot_width, dot_height)
