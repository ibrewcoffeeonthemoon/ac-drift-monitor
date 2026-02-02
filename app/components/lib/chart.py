import ac

from app.components.lib.gl.line import horizontal_line, vertical_line
from app.components.lib.gl.shape import square
from app.window import window


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
        bg_opacity: float = 0.2,
        bg_char: str = '',
        bg_char_font_size: int = 120,
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
        self._bg_opacity = bg_opacity
        self._bg_char = bg_char
        self._bg_char_font_size = bg_char_font_size

        self._draw_label()

    def _draw_label(self) -> None:
        # draw big label
        label = ac.addLabel(window, self._bg_char)
        ac.setFont(label, 'arial')
        ac.setFontSize(label, self._bg_char_font_size)
        ac.setFontColor(label, 1, 1, 1, 0.1)
        ac.setPosition(
            label,
            self._x_pos+25,
            self._y_pos-110,
        )

    def draw_axes(self) -> None:
        # set layouts, styles
        ac.setBackgroundOpacity(window, self._bg_opacity)

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
