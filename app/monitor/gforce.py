from acsys import CS

import config

from ..lib.color import *
from ..telemetry import ac_api
from ._base import Monitor
from .lib.canvas import Chart
from .lib.indicator import QuadBar, SquareDot


class GForceMonitor(Monitor):
    data_keys = (CS.AccG, CS.NdSlip, )
    enabled = config.GForceMonitor.enabled
    col_index = config.GForceMonitor.col_index

    def __init__(
        self,
        x_pos: float,
        y_pos: float,
    ) -> None:
        super().__init__(x_pos, y_pos)

        self._width = width = config.App.span_len*config.GForceMonitor.col_span
        self._height = height = config.App.height

        self._chart = Chart(
            x_pos,
            y_pos,
            width,
            height,
            x_axis_color=white.a7,
            y_axis_color=white.a7,
            axis_segment_count=8,
            x_axis_marker_length_ratio=1.0,
            y_axis_marker_length_ratio=1.0,
            bg_char='G',
        )
        self._gforce_square_dot = SquareDot(
            region=self._chart,
            dot_size=round(config.GForceMonitor.box_size*self.height),
            scale=config.GForceMonitor.gforce_scale,
            inverted_y_scale=True,
        )
        self._slip_ratio_quad_bars = tuple(
            QuadBar(
                region=region,
                color=red.a4,
                scale=config.GForceMonitor.slip_ratio_scale,
            )
            for region in (
                self._chart.top_left,
                self._chart.top_right,
                self._chart.bottom_left,
                self._chart.bottom_right,
            )
        ) if config.GForceMonitor.slip_ratio_enabled else None

    @property
    def width(self) -> float: return self._width
    @property
    def height(self) -> float: return self._height

    def _render_gforce_square_dot(self) -> None:
        x_accG, _, z_accG = ac_api[CS.AccG].wma()
        self._gforce_square_dot.plot(x=x_accG, y=z_accG,)

    def _render_slip_ratio_quad_bar(self) -> None:
        fl, fr, rl, rr = ac_api[CS.NdSlip].wma()
        if self._slip_ratio_quad_bars is not None:
            self._slip_ratio_quad_bars[0].plot(fl)
            self._slip_ratio_quad_bars[1].plot(fr)
            self._slip_ratio_quad_bars[2].plot(rl)
            self._slip_ratio_quad_bars[3].plot(rr)

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry and plot the indicators
        self._render_gforce_square_dot()
        self._render_slip_ratio_quad_bar()
