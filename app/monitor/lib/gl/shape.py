import ac
import acsys

from ....lib.color import *
from ....lib.geometry import Vertex


def rectangle(
    vertex: Vertex,
    width: float,
    height: float,
    color: Color = white.full,
) -> None:
    ac.glColor4f(color.r, color.g, color.b, color.a)
    ac.glQuad(vertex.x, vertex.y, width, height)


def centered_square(
    center: Vertex,
    length: float,
    color: Color = white.full,
) -> None:
    ac.glColor4f(color.r, color.g, color.b, color.a)
    ac.glQuad(center.x - length/2, center.y - length/2, length, length)


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
