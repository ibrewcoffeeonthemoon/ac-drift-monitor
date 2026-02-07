import ac
import acsys

from ....lib.color import *


def line(
    vertex1: 'tuple[int, int]',
    vertex2: 'tuple[int, int]',
    color4f: 'tuple[float, float, float, float]' = white.full,
) -> None:
    ac.glColor4f(*color4f)
    ac.glBegin(acsys.GL.Lines)
    ac.glVertex2f(*vertex1)
    ac.glVertex2f(*vertex2)
    ac.glEnd()


def horizontal_line(
    vertex1: 'tuple[int, int]',
    length: int,
    color4f: 'tuple[float, float, float, float]' = white.full,
) -> None:
    x_pos, y_pos = vertex1
    line((x_pos, y_pos), (x_pos+length, y_pos), color4f)


def vertical_line(
    vertex1: 'tuple[int, int]',
    length: int,
    color4f: 'tuple[float, float, float, float]' = white.full,
) -> None:
    x_pos, y_pos = vertex1
    line((x_pos, y_pos), (x_pos, y_pos+length), color4f)
