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
        # fetch telemetry
        x, _, z = telemetry.accG

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
