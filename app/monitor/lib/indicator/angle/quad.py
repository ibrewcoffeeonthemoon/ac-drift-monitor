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
    ) -> None:
        super().__init__(chart=chart)
        self._color = color

    def _vertices(self, angle_degree: float) -> 'tuple[Vertex, Vertex, Vertex, Vertex]':
        vertex0, vertex1 = self._edge_intercepts(angle_degree)
        vertex2, vertex3 = self._nearest_corners(angle_degree)[-2:]
        return (vertex0, vertex1, vertex2, vertex3)

    def plot(self, val: float, color: 'Color | None' = None) -> None:
        quadrilateral(
            *self._vertices(val),
            color=color or self._color
        )
