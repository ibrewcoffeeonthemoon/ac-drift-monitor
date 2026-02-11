from .....lib.color import *
from .....lib.geometry import Vertex
from ...chart import Chart
from ...gl.shape import quadrilateral
from ._base import AngleIndicator


class AngleQuad(AngleIndicator):
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
        vertex1, vertex2 = self._edge_intercepts(angle_degree)
        vertex3, vertex4 = (
            (self._chart.corner_bottom_left, self._chart.corner_bottom_right) if abs(angle_degree) <= 45 else
            (self._chart.corner_bottom_right, self._chart.corner_top_right) if angle_degree > 45 else
            (self._chart.corner_top_left, self._chart.corner_bottom_left)
        ) if not self._inverted_x_scale else (
            (self._chart.corner_top_left, self._chart.corner_top_right) if abs(angle_degree) <= 45 else
            (self._chart.corner_bottom_left, self._chart.corner_top_left) if angle_degree > 45 else
            (self._chart.corner_top_right, self._chart.corner_bottom_right)
        )
        # counter clockwise direction
        return (vertex1, vertex2, vertex3, vertex4)

    def plot(self, val: float, color: 'Color | None' = None) -> None:
        quadrilateral(
            *self._vertices(val),
            color=color or self._color
        )
