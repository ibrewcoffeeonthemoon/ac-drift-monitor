from .....lib.color import *
from .....lib.geometry import Vertex
from ...gl.shape import quadrilateral
from ._base import AngleIndicator


class AngleQuad(AngleIndicator):
    def _vertices(self, angle_degree: float) -> 'tuple[Vertex, Vertex, Vertex, Vertex]':
        vertex0, vertex1 = self._edge_intercepts(angle_degree)
        vertex2, vertex3 = self._nearest_corners(angle_degree)[-2:]
        return (vertex0, vertex1, vertex2, vertex3)

    def plot(self, val: float, color: 'Color | None' = None) -> None:
        val = val * self._sensitivity
        val = -val if self._reversed else val
        quadrilateral(
            *self._vertices(val),
            color=color or self._color
        )
