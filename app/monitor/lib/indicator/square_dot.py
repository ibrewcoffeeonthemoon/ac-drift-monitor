from ....lib.color import *
from ....lib.geometry import Vertex
from ....lib.number import num
from ..chart import Region
from ..gl.shape import square
from ._base import Indicator


class SquareDot(Indicator):
    def __init__(
        self,
        chart: Region,
        dot_size: float = 30,
        color: Color = red.full,
        scale: float = 1.0,
        inverted_x_scale: bool = False,
        inverted_y_scale: bool = False,
        centered_x_scale: bool = True,
        centered_y_scale: bool = True,
    ) -> None:
        super().__init__(
            chart=chart,
            inverted_x_scale=inverted_x_scale,
            inverted_y_scale=inverted_y_scale,
            centered_x_scale=centered_x_scale,
            centered_y_scale=centered_y_scale,
        )
        self._dot_size = dot_size
        self._color = color
        self._scale = scale

    def _vertices(self, x: float, y: float) -> Vertex:
        return Vertex(*(
            begin + val*magnitude*direction
            for val, begin, magnitude, direction
            in zip((x, y), self._begin, self._magnitude, self._direction)
        ))

    def plot(self, x: float, y: float,) -> None:
        square(
            self._vertices(
                x=num(x).normalize(self._scale).clip(-1, 1).f,
                y=num(y).normalize(self._scale).clip(-1, 1).f,
            ),
            length=self._dot_size,
            color=self._color
        )
