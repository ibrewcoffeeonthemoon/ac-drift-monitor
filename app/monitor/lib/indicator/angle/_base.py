import math

from .....lib.geometry import Vertex
from .....lib.number import num
from .._base import Indicator


class AngleIndicator(Indicator):
    def _edge_intercepts(self, angle_degree: float) -> 'tuple[Vertex, Vertex]':
        x_center, y_center = self._chart.center
        radius = self._chart.diagonal_len
        radian_angle = num(angle_degree).radian().f
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
        return (vertex1, vertex2)
