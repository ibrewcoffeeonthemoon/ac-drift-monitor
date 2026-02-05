import ac

from app.components.lib.gl.line import horizontal_line, vertical_line
from app.window import window


class Chart:
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
        color4f_primary: 'tuple[float, float, float, float]' = (1, 1, 1, 0.7),
        color4f_secondary: 'tuple[float, float, float, float]' = (1, 1, 1, 0.1),
        marker_count: int = 4,
        x_axis_marker_length: int = 10,
        y_axis_marker_length: int = 10,
        bg_opacity: float = 0.2,
        bg_char: str = '',
    ) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self._color4f_primary = color4f_primary
        self._color4f_secondary = color4f_secondary
        self._marker_count = marker_count
        self._x_axis_marker_length = x_axis_marker_length
        self._y_axis_marker_length = y_axis_marker_length
        self._bg_opacity = bg_opacity
        self._bg_char = bg_char

        self._draw_label()

    def _draw_label(self) -> None:
        # estimate dynamic font size
        font_size = min(self.width, self.height)
        font_size_vertical_offset = self.height//2-font_size*3//4
        # draw big label
        label = ac.addLabel(window, self._bg_char)
        ac.setFont(label, 'arial')
        ac.setFontSize(label, font_size)
        ac.setFontColor(label, 1, 1, 1, 0.1)
        ac.setFontAlignment(label, 'center')
        ac.setSize(label, self.width, self.height)
        ac.setPosition(
            label,
            self.x_pos,
            self.y_pos+font_size_vertical_offset,
        )

    def draw_axes(self) -> None:
        # set layouts, styles
        ac.setBackgroundOpacity(window, self._bg_opacity)

        # x-axis
        horizontal_line((self.x_pos, self.y_pos+self.height//2), self.width, self._color4f_primary)
        # y-axis
        vertical_line((self.x_pos+self.width//2, self.y_pos), self.height, self._color4f_primary)

        # draw markers
        for i in range(self._marker_count*2+1):
            # x-axis markers
            vertical_line(
                (self.x_pos+i*self.width//2//self._marker_count, self.y_pos+self.height//2-self._x_axis_marker_length//2),
                self._y_axis_marker_length,
                self._color4f_secondary
            )
            # y-axis markers
            horizontal_line(
                (self.x_pos+self.width//2-self._y_axis_marker_length //
                 2, self.y_pos+i*self.height//2//self._marker_count),
                self._y_axis_marker_length,
                self._color4f_secondary
            )
