import ac

from ...window import window
from .gl.line import horizontal_line, vertical_line


class Chart:
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
        x_axis_color4f: 'tuple[float, float, float, float]' = (1, 1, 1, 0.0),
        y_axis_color4f: 'tuple[float, float, float, float]' = (1, 1, 1, 0.0),
        x_axis_marker_color4f: 'tuple[float, float, float, float]' = (1, 1, 1, 0.1),
        y_axis_marker_color4f: 'tuple[float, float, float, float]' = (1, 1, 1, 0.1),
        axis_segment_count: int = 8,
        x_axis_marker_length_ratio: float = 0.05,
        y_axis_marker_length_ratio: float = 0.05,
        bg_opacity: float = 0.2,
        bg_char: str = '',
    ) -> None:
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height
        self._x_axis_color4f = x_axis_color4f
        self._y_axis_color4f = y_axis_color4f
        self._x_axis_marker_color4f = x_axis_marker_color4f
        self._y_axis_marker_color4f = y_axis_marker_color4f
        self._axis_segmnt_count = axis_segment_count
        self._x_axis_marker_length_ratio = x_axis_marker_length_ratio
        self._y_axis_marker_length_ratio = y_axis_marker_length_ratio
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
        horizontal_line((self.x_pos, self.y_pos+self.height//2), self.width, self._x_axis_color4f)
        # y-axis
        vertical_line((self.x_pos+self.width//2, self.y_pos), self.height, self._y_axis_color4f)

        # draw markers
        for i in range(self._axis_segmnt_count+1):
            # x-axis markers
            vertical_line(
                (
                    round(self.x_pos+i*self.width/self._axis_segmnt_count),
                    round(self.y_pos+self.height/2-self._x_axis_marker_length_ratio*self.height/2),
                ),
                round(self._x_axis_marker_length_ratio*self.height),
                self._x_axis_marker_color4f,
            )
            # y-axis markers
            horizontal_line(
                (
                    round(self.x_pos+self.width/2-self._y_axis_marker_length_ratio*self.width/2),
                    round(self.y_pos+i*self.height/self._axis_segmnt_count)
                ),
                round(self._y_axis_marker_length_ratio*self.width),
                self._y_axis_marker_color4f
            )
