import ac

import config

from ....lib.color import *
from ....lib.geometry import Vertex
from ....window import window
from ..gl.line import horizontal_line, vertical_line
from ..text import BigText
from .region import Region


class Chart:
    def __init__(
        self,
        region: Region,
        x_axis_color: Color = white.transparent,
        y_axis_color: Color = white.transparent,
        x_axis_marker_color: Color = white.a1,
        y_axis_marker_color: Color = white.a1,
        x_axis_segment_count: int = 8,
        y_axis_segment_count: int = 8,
        x_axis_marker_length_ratio: float = 0.05,
        y_axis_marker_length_ratio: float = 0.05,
        bg_char: str = '',
    ) -> None:
        self._region = region
        self._x_axis_color = x_axis_color
        self._y_axis_color = y_axis_color
        self._x_axis_marker_color = x_axis_marker_color
        self._y_axis_marker_color = y_axis_marker_color
        self._x_axis_segmnt_count = x_axis_segment_count
        self._y_axis_segmnt_count = y_axis_segment_count
        self._x_axis_marker_length_ratio = x_axis_marker_length_ratio
        self._y_axis_marker_length_ratio = y_axis_marker_length_ratio
        self._bg_opacity = config.App.bg_opacity
        self._bg_char = bg_char

        if len(bg_char) > 0:
            BigText(
                self._region,
                text=self._bg_char,
                font_color=white.alpha(self._bg_opacity),
                expected_text_len=1,
            )

    def draw_axes(self) -> None:
        # set layouts, styles
        ac.setBackgroundOpacity(window, self._bg_opacity)

        # unpack
        x_pos, y_pos, width, height = self._region.bounds

        # x-axis
        horizontal_line(self._region.midpoint_left, width, self._x_axis_color)
        # y-axis
        vertical_line(self._region.midpoint_top, height, self._y_axis_color)

        # draw markers
        for i in range(self._x_axis_segmnt_count+1):
            # x-axis markers
            vertical_line(
                Vertex(
                    x_pos+i*width/self._x_axis_segmnt_count,
                    y_pos+height/2-self._x_axis_marker_length_ratio*height/2,
                ),
                round(self._x_axis_marker_length_ratio*height),
                self._x_axis_marker_color,
            )
        for i in range(self._y_axis_segmnt_count+1):
            # y-axis markers
            horizontal_line(
                Vertex(
                    x_pos+width/2-self._y_axis_marker_length_ratio*width/2,
                    y_pos+i*height/self._y_axis_segmnt_count,
                ),
                round(self._y_axis_marker_length_ratio*width),
                self._y_axis_marker_color
            )
