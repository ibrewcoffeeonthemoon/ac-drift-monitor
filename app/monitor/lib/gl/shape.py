import ac
import acsys

from ....lib.color import *


def rectangle(
    vertex_center: 'tuple[int, int]',
    width: int,
    height: int,
    color4f: 'tuple[float, float, float, float]' = white.full,
) -> None:
    x_pos, y_pos = vertex_center
    ac.glColor4f(*color4f)
    ac.glQuad(
        x_pos - width//2,
        y_pos - height//2,
        width,
        height,
    )


def square(
    vertex_center: 'tuple[int, int]',
    length: int,
    color4f: 'tuple[float, float, float, float]' = white.full,
) -> None:
    rectangle(vertex_center, length, length, color4f)


def quadrilateral(
    vertex1: 'tuple[int, int]',
    vertex2: 'tuple[int, int]',
    vertex3: 'tuple[int, int]',
    vertex4: 'tuple[int, int]',
    color4f: 'tuple[float, float, float, float]' = white.full,
) -> None:
    ac.glColor4f(*color4f)
    ac.glBegin(acsys.GL.Quads)
    ac.glVertex2f(*vertex1)
    ac.glVertex2f(*vertex2)
    ac.glVertex2f(*vertex3)
    ac.glVertex2f(*vertex4)
    ac.glEnd()
