from ....lib.color import *
from ....lib.geometry import Vertex
from ..chart import Chart
from ..gl.shape import quadrilateral
from ._base import Indicator


class QuadBar(Indicator):
    def __init__(
        self,
        chart: Chart,
        color: Color = red.full,
        inverted_x_scale: bool = False,
        inverted_y_scale: bool = False,
        centered_x_scale: bool = False,
        centered_y_scale: bool = False,
    ) -> None:
        super().__init__(
            chart=chart,
            inverted_x_scale=inverted_x_scale,
            inverted_y_scale=inverted_y_scale,
            centered_x_scale=centered_x_scale,
            centered_y_scale=centered_y_scale,
        )
        self._color = color

    def _vertices(self, val: float) -> 'tuple[Vertex, Vertex, Vertex, Vertex]':
        x_begin, y_begin = self._begin
        x_mag, y_mag = self._magnitude
        x_dir, y_dir = self._direction
        return (
            Vertex(self._x_pos, y_begin + val*y_mag*y_dir),
            Vertex(self._x_pos+self._width, y_begin + val*y_mag*y_dir),
            Vertex(self._x_pos+self._width, y_begin),
            Vertex(self._x_pos, y_begin),
        )

    def plot(self, val: float, color: 'Color | None' = None) -> None:
        quadrilateral(
            *self._vertices(val),
            color=color or self._color
        )
