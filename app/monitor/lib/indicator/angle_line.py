import math

from ....lib.color import *
from ....lib.geometry import Vertex
from ....lib.number import num
from ..chart import Chart
from ..gl.line import line
from ._base import Indicator


class AngleLine(Indicator):
    def __init__(
        self,
        chart: Chart,
        color: Color = yellow.full,
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

    def _vertices(self, angle_degree: float) -> 'tuple[Vertex, Vertex]':
        radian_angle = math.pi * angle_degree/180
        x_center, y_center = self._chart.center
        radius = math.sqrt(self._width**2 + self._height**2)/2
        x_coord = radius * math.cos(radian_angle)
        y_coord = radius * math.sin(radian_angle)
        return (
            Vertex(
                num(x_center+x_coord).clip(self._x_pos, self._x_pos+self._width).f,
                num(y_center-y_coord).clip(self._y_pos, self._y_pos+self._height).f,
            ),
            Vertex(
                num(x_center-x_coord).clip(self._x_pos, self._x_pos+self._width).f,
                num(y_center+y_coord).clip(self._y_pos, self._y_pos+self._width).f,
            ),
        )

    def plot(self, val: float, color: 'Color | None' = None) -> None:
        line(
            *self._vertices(val),
            color=color or self._color
        )
