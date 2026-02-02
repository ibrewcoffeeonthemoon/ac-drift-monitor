from app.components.lib.gl.line import horizontal_line, vertical_line
from app.components.lib.gl.shape import square


class Chart:
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
        dot_size: int = 30,
        color4f_primary: tuple = (1, 1, 1, 0.7),
        color4f_secondary: tuple = (1, 1, 1, 0.1),
        marker_count: int = 4,
        x_axis_marker_length: int = 10,
        y_axis_marker_length: int = 10,
    ) -> None:
        self._x_pos = x_pos
        self._y_pos = y_pos
        self._width = width
        self._height = height
        self._dot_size = dot_size
        self._color4f_primary = color4f_primary
        self._color4f_secondary = color4f_secondary
        self._marker_count = marker_count
        self._x_axis_marker_length = x_axis_marker_length
        self._y_axis_marker_length = y_axis_marker_length

    def draw_axes(self) -> None:
        # x-axis
        horizontal_line((self._x_pos, self._y_pos+self._height//2), self._width, self._color4f_primary)
        # y-axis
        vertical_line((self._x_pos+self._width//2, self._y_pos), self._height, self._color4f_primary)

        # draw markers
        for i in range(self._marker_count*2+1):
            # x-axis markers
            vertical_line(
                (self._x_pos+i*self._width//2//self._marker_count, self._y_pos+self._height//2-self._x_axis_marker_length//2),
                self._y_axis_marker_length,
                self._color4f_secondary
            )
            # y-axis markers
            horizontal_line(
                (self._x_pos+self._width//2-self._y_axis_marker_length //
                 2, self._y_pos+i*self._height//2//self._marker_count),
                self._y_axis_marker_length,
                self._color4f_secondary
            )

    def plot(self, x, y) -> None:
        square(
            (
                self._x_pos + self._width//2 + x*self._width//2,
                self._y_pos + self._height//2 + y*self._height//2
            ),
            length=self._dot_size,
            color4f=(1, 0, 0, 1)
        )
