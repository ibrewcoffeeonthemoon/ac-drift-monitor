from app.components.lib.chart import Chart
from app.components.lib.gl.shape import square
from app.components.lib.indicator import Indicator


class SquareDot(Indicator):
    def __init__(
        self,
        chart: Chart,
        dot_size: int = 30,
        color4f: tuple = (1, 0, 0, 1),
        inverted_x_scale: bool = False,
        inverted_y_scale: bool = False,
        centered_x_scale: bool = True,
        centered_y_scale: bool = True,
    ) -> None:
        super().__init__(chart)
        self._dot_size = dot_size
        self._color4f = color4f
        self._inverted_x_scale = inverted_x_scale
        self._inverted_y_scale = inverted_y_scale
        self._centered_x_scale = centered_x_scale
        self._centered_y_scale = centered_y_scale

    def plot(
        self,
        x: float,
        y: float,
    ) -> None:
        def coordinate(val: float, root: int, offset: int, inverted: bool, centered: bool) -> float:
            begin = root+offset//2 if centered else root+offset if inverted else root
            length = val*offset//2 if centered else val*offset
            direction = -1 if inverted else 1
            position = begin + direction*length
            return position

        square(
            (
                coordinate(x, self._x_pos, self._width, self._inverted_x_scale, self._centered_x_scale),
                coordinate(y, self._y_pos, self._height, self._inverted_y_scale, self._centered_y_scale),
            ),
            length=self._dot_size,
            color4f=self._color4f
        )
