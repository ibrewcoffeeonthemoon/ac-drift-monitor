from ....lib.color import *
from ..chart import Chart
from ..gl.shape import square
from ._base import Indicator


class SquareDot(Indicator):
    def __init__(
        self,
        chart: Chart,
        dot_size: int = 30,
        color4f: 'tuple[float, float, float, float]' = red.full,
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
        self._color4f = color4f

    def _coordinates(self, x: float, y: float) -> 'tuple[int, int]':
        x, y = tuple(
            round(begin + val*magnitude*direction)
            for val, begin, magnitude, direction
            in zip((x, y), self._begin, self._magnitude, self._direction)
        )
        return x, y

    def plot(self, x: float, y: float,) -> None:
        square(
            self._coordinates(x, y),
            length=self._dot_size,
            color4f=self._color4f
        )
