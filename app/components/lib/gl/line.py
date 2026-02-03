import ac
import acsys


def line(
    vertex1: tuple,
    vertex2: tuple,
    color4f: tuple = (1, 1, 1, 1),
) -> None:
    ac.glColor4f(*color4f)
    ac.glBegin(acsys.GL.Lines)
    ac.glVertex2f(*vertex1)
    ac.glVertex2f(*vertex2)
    ac.glEnd()


def horizontal_line(
    vertex1: tuple,
    length: int,
    color4f: tuple = (1, 1, 1, 1),
) -> None:
    x_pos, y_pos = vertex1
    line((x_pos, y_pos), (x_pos+length, y_pos), color4f)


def vertical_line(
    vertex1: tuple,
    length: int,
    color4f: tuple = (1, 1, 1, 1),
) -> None:
    x_pos, y_pos = vertex1
    line((x_pos, y_pos), (x_pos, y_pos+length), color4f)
