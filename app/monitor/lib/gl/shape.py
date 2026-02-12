import ac
import acsys

from ....lib.color import *
from ....lib.geometry import Vertex


def rectangle(
    vertex_center: Vertex,
    width: float,
    height: float,
    color: Color = white.full,
) -> None:
    x_pos, y_pos = vertex_center.i
    ac.glColor4f(*color)
    ac.glQuad(
        x_pos - width/2,
        y_pos - height/2,
        width,
        height,
    )


def square(
    vertex_center: Vertex,
    length: float,
    color: Color = white.full,
) -> None:
    rectangle(vertex_center, length, length, color)


def quadrilateral(
    vertex1: Vertex,
    vertex2: Vertex,
    vertex3: Vertex,
    vertex4: Vertex,
    color: Color = white.full,
) -> None:
    ac.glColor4f(*color)
    ac.glBegin(acsys.GL.Quads)
    ac.glVertex2f(*vertex1.f)
    ac.glVertex2f(*vertex2.f)
    ac.glVertex2f(*vertex3.f)
    ac.glVertex2f(*vertex4.f)
    ac.glEnd()
