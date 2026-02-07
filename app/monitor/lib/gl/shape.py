import ac
import acsys

from ....lib.color import *


def rectangle(
    vertex_center: 'tuple[int, int]',
    width: int,
    height: int,
    color: Color = white.full,
) -> None:
    x_pos, y_pos = vertex_center
    ac.glColor4f(*color)
    ac.glQuad(
        x_pos - width//2,
        y_pos - height//2,
        width,
        height,
    )


def square(
    vertex_center: 'tuple[int, int]',
    length: int,
    color: Color = white.full,
) -> None:
    rectangle(vertex_center, length, length, color)


def quadrilateral(
    vertex1: 'tuple[int, int]',
    vertex2: 'tuple[int, int]',
    vertex3: 'tuple[int, int]',
    vertex4: 'tuple[int, int]',
    color: Color = white.full,
) -> None:
    ac.glColor4f(*color)
    ac.glBegin(acsys.GL.Quads)
    ac.glVertex2f(*vertex1)
    ac.glVertex2f(*vertex2)
    ac.glVertex2f(*vertex3)
    ac.glVertex2f(*vertex4)
    ac.glEnd()
