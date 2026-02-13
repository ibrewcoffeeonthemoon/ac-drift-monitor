import ac
import acsys

from ....lib.color import *
from ....lib.geometry import Vertex


def rectangle(
    center: Vertex,
    width: float,
    height: float,
    color: Color = white.full,
) -> None:
    ac.glColor4f(color.r, color.g, color.b, color.a)
    ac.glQuad(
        center.x - width/2,
        center.y - height/2,
        width,
        height,
    )


def square(
    center: Vertex,
    length: float,
    color: Color = white.full,
) -> None:
    rectangle(center, length, length, color)


def quadrilateral(
    vertex1: Vertex,
    vertex2: Vertex,
    vertex3: Vertex,
    vertex4: Vertex,
    color: Color = white.full,
) -> None:
    ac.glColor4f(color.r, color.g, color.b, color.a)
    ac.glBegin(acsys.GL.Quads)
    ac.glVertex2f(vertex1.x, vertex1.y)
    ac.glVertex2f(vertex2.x, vertex2.y)
    ac.glVertex2f(vertex3.x, vertex3.y)
    ac.glVertex2f(vertex4.x, vertex4.y)
    ac.glEnd()
