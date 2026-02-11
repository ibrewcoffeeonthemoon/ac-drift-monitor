import math

from ....lib.color import *
from ....lib.geometry import Vertex
from ....lib.number import num
from ..chart import Chart
from ..gl.shape import quadrilateral
from ._base import Indicator


class AngleQuad(Indicator):
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

    def _vertices(self, angle_degree: float) -> 'tuple[Vertex, Vertex, Vertex, Vertex]':
        radian_angle = math.pi * angle_degree/180
        x_center, y_center = self._chart.center
        radius = math.sqrt(self._width**2 + self._height**2)/2
        x_coord = radius * math.cos(radian_angle)
        y_coord = radius * math.sin(radian_angle)
        vertex1 = Vertex(
            num(x_center+x_coord).clip(self._x_pos, self._x_pos+self._width).f,
            num(y_center-y_coord).clip(self._y_pos, self._y_pos+self._height).f,
        )
        vertex2 = Vertex(
            num(x_center-x_coord).clip(self._x_pos, self._x_pos+self._width).f,
            num(y_center+y_coord).clip(self._y_pos, self._y_pos+self._width).f,
        )
        vertex3, vertex4 = (
            (self._chart.corner_bottom_left, self._chart.corner_bottom_right) if abs(angle_degree) <= 45 else
            (self._chart.corner_bottom_right, self._chart.corner_top_right) if angle_degree > 45 else
            (self._chart.corner_top_left, self._chart.corner_bottom_left)
        )
        # counter clockwise direction
        return (vertex1, vertex2, vertex3, vertex4)

    def plot(self, val: float, color: 'Color | None' = None) -> None:
        quadrilateral(
            *self._vertices(val),
            color=color or self._color
        )
