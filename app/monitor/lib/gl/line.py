import ac
import acsys

from ....lib.color import *
from ....lib.geometry import Vertex


def line(
    vertex1: Vertex,
    vertex2: Vertex,
    color: Color = white.full,
) -> None:
    ac.glColor4f(color.r, color.g, color.b, color.a)
    ac.glBegin(acsys.GL.Lines)
    ac.glVertex2f(vertex1.x, vertex1.y)
    ac.glVertex2f(vertex2.x, vertex2.y)
    ac.glEnd()


def horizontal_line(
    vertex: Vertex,
    length: float,
    color: Color = white.full,
) -> None:
    line(vertex, Vertex(vertex.x+length, vertex.y), color)


def vertical_line(
    vertex: Vertex,
    length: float,
    color: Color = white.full,
) -> None:
    line(vertex, Vertex(vertex.x, vertex.y+length), color)
