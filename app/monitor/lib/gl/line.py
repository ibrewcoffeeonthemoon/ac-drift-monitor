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
    ac.glVertex2f(*vertex1.f)
    ac.glVertex2f(*vertex2.f)
    ac.glEnd()


def horizontal_line(
    vertex1: Vertex,
    length: float,
    color: Color = white.full,
) -> None:
    x_pos, y_pos = vertex1.f
    line(Vertex(x_pos, y_pos), Vertex(x_pos+length, y_pos), color)


def vertical_line(
    vertex1: Vertex,
    length: float,
    color: Color = white.full,
) -> None:
    x_pos, y_pos = vertex1.f
    line(Vertex(x_pos, y_pos), Vertex(x_pos, y_pos+length), color)
