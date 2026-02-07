from acsys import CS

import config

from ..lib.stats import MovingAverage
from ..lib.value import Float
from ..telemetry import telemetry
from ._base import Monitor
from .lib.chart import Chart
from .lib.indicator import QuadBar


class _TyreSlipRatioMonitor:
    def __init__(
        self,
        i_slipRatio: int,
        x_pos: int,
        y_pos: int,
        width: int,
        height: int,
    ) -> None:
        self._i_slipRatio = i_slipRatio
        self._slipRatio = MovingAverage(scale=3.0)

        self._chart = Chart(
            x_pos,
            y_pos,
            width,
            height,
            x_axis_marker_color4f=(0, 0, 0, 0.0),
            axis_segment_count=4,
            x_axis_marker_length_ratio=1.0,
            y_axis_marker_length_ratio=1.0,
            bg_opacity=0.2,
            bg_char='S',
        )
        self._quad_bar = QuadBar(
            chart=self._chart,
            color4f=(1, 0, 0, 0.4),
            centered_y_scale=True,
        )

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        # slipRatio = telemetry.slipRatio[self._i_slipRatio]
        # slipRatio = telemetry[CS.SlipRatio][self._i_slipRatio]
        slipRatio = telemetry[CS.SlipRatio].wma()[self._i_slipRatio]

        # updadte buffer
        # self._slipRatio.update(slipRatio)

        # plot the indicators
        # self._quad_bar.plot(self._slipRatio.weighted_average)
        self._quad_bar.plot(
            Float(slipRatio).normalize(3.0).clip(-1, 1).value
        )


class SlipRatioMonitor(Monitor):
    data_keys = (CS.SlipRatio, )
    enabled = config.SlipRatioMonitor.enabled
    col_index = config.SlipRatioMonitor.col_index

    def __init__(
        self,
        x_pos: int,
        y_pos: int,
    ) -> None:
        super().__init__(x_pos, y_pos)

        self._width = width = config.App.span_len*config.SlipRatioMonitor.col_span
        self._height = height = config.App.height

        self._tyres_slip_ratio_monitors = [
            _TyreSlipRatioMonitor(
                i_slipRatio=i,
                x_pos=_x_pos,
                y_pos=_y_pos,
                width=width//2,
                height=height//2,
            )
            for i, (_x_pos, _y_pos) in enumerate((
                (x_pos, y_pos),
                (x_pos+width//2, y_pos),
                (x_pos, y_pos+height//2),
                (x_pos+width//2, y_pos+height//2),
            ))
        ]

    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def render(self) -> None:
        for monitor in self._tyres_slip_ratio_monitors:
            monitor.render()
