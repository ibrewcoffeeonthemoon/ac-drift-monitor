import math

from .....lib.color import *
from .....lib.geometry import Vertex
from .....lib.number import num
from ...chart import Chart
from .._base import Indicator


class AngleIndicator(Indicator):
    def __init__(
        self,
        chart: Chart,
        sensitivity: float = 1.0,
        reversed: bool = False,
        color: Color = yellow.full,
    ) -> None:
        super().__init__(chart=chart)
        self._sensitivity = sensitivity
        self._reversed = reversed
        self._color = color
        theta = math.degrees(math.atan2(chart.height, chart.width))
        self._quadrant_boundries = (theta, 180-theta, 180+theta, 360-theta)

    def _quadrant(self, angle_degree: float) -> int:
        r'''
        quardant id:
         \ 1 /
         2 X 0
         / 3 \
        '''
        b0, b1, b2, b3 = self._quadrant_boundries
        remainder = angle_degree % 360
        return (
            0 if b3 <= remainder or remainder < b0 else
            1 if b0 <= remainder < b1 else
            2 if b1 <= remainder < b2 else
            3
        )

    def _nearest_corners(self, angle_degree: float) -> 'tuple[Vertex, Vertex, Vertex, Vertex]':
        id = self._quadrant(angle_degree)
        c0, c1, c2, c3 = self._chart.corners[id:] + self._chart.corners[:id]
        return c0, c1, c2, c3

    def _edge_intercepts(self, angle_degree: float) -> 'tuple[Vertex, Vertex]':
        x_center, y_center = self._chart.center.f
        radius = self._chart.diagonal_len/2
        radian_angle = num(angle_degree).radian().f
        x_coord = radius * math.cos(radian_angle)
        y_coord = radius * math.sin(radian_angle)
        vertex1 = Vertex(
            num(x_center+x_coord).clip(self._x_pos, self._x_pos+self._width).f,
            num(y_center-y_coord).clip(self._y_pos, self._y_pos+self._height).f,
        )
        vertex2 = Vertex(
            num(x_center-x_coord).clip(self._x_pos, self._x_pos+self._width).f,
            num(y_center+y_coord).clip(self._y_pos, self._y_pos+self._height).f,
        )
        return (vertex1, vertex2)
