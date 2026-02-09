import ac
import acsys

from ....lib.color import *
from ....lib.geometry import Vertex


def line(
    vertex1: Vertex,
    vertex2: Vertex,
    color: Color = white.full,
) -> None:
    ac.glColor4f(*color)
    ac.glBegin(acsys.GL.Lines)
    ac.glVertex2f(*vertex1)
    ac.glVertex2f(*vertex2)
    ac.glEnd()


def horizontal_line(
    vertex1: Vertex,
    length: int,
    color: Color = white.full,
) -> None:
    x_pos, y_pos = vertex1
    line(Vertex(x_pos, y_pos), Vertex(x_pos+length, y_pos), color)


def vertical_line(
    vertex1: Vertex,
    length: int,
    color: Color = white.full,
) -> None:
    x_pos, y_pos = vertex1
    line(Vertex(x_pos, y_pos), Vertex(x_pos, y_pos+length), color)
