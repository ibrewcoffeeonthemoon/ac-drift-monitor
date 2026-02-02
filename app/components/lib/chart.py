from app.components.lib import draw


def draw_axes(
    x_pos: int,
    y_pos: int,
    width: int,
    height: int,
    color4f_primary: tuple = (1, 1, 1, 1),
    color4f_secondary: tuple = (1, 1, 1, 0.5),
) -> None:
    draw.horizontal_line((x_pos, y_pos+height//2), width, color4f_primary)
    draw.vertical_line((x_pos+width//2, y_pos), height, color4f_primary)
