import ac


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
