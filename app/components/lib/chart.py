from app.components.lib.gl.line import horizontal_line, vertical_line


def draw_axes(
    x_pos: int,
    y_pos: int,
    width: int,
    height: int,
    color4f_primary: tuple = (1, 1, 1, 0.7),
    color4f_secondary: tuple = (1, 1, 1, 0.1),
    marker_count: int = 4,
    x_axis_marker_length: int = 10,
    y_axis_marker_length: int = 10,
) -> None:
    # x-axis
    horizontal_line((x_pos, y_pos+height//2), width, color4f_primary)
    # y-axis
    vertical_line((x_pos+width//2, y_pos), height, color4f_primary)

    # draw markers
    for i in range(marker_count*2+1):
        # x-axis markers
        vertical_line(
            (x_pos+i*width//2//marker_count, y_pos+height//2-x_axis_marker_length//2),
            y_axis_marker_length,
            color4f_secondary
        )
        # y-axis markers
        horizontal_line(
            (x_pos+width//2-y_axis_marker_length//2, y_pos+i*height//2//marker_count),
            y_axis_marker_length,
            color4f_secondary
        )
