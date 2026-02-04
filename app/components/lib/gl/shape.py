import ac
import acsys


def rectangle(
    vertex_center: tuple,
    width: int,
    height: int,
    color4f: tuple = (1, 1, 1, 1),
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
    vertex_center: tuple,
    length: int,
    color4f: tuple = (1, 1, 1, 1),
) -> None:
    rectangle(vertex_center, length, length, color4f)


def quadrilateral(
    vertex1: tuple,
    vertex2: tuple,
    vertex3: tuple,
    vertex4: tuple,
    color4f: tuple = (1, 1, 1, 1),
) -> None:
    ac.glColor4f(*color4f)
    ac.glBegin(acsys.GL.Quads)
    ac.glVertex2f(*vertex1)
    ac.glVertex2f(*vertex2)
    ac.glVertex2f(*vertex3)
    ac.glVertex2f(*vertex4)
    ac.glEnd()
