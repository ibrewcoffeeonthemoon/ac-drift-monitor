from acsys import CS

import config

from ..lib.color import *
from ..lib.number import num
from ..telemetry import ac_api, ac_mem
from ._base import Component, Monitor
from .lib.canvas import Chart, Region
from .lib.indicator import QuadBar
from .lib.text import BigText


class _TyreSlipRatioMonitor(Component):
    def __init__(
        self,
        i_slipRatio: int,
        x_pos: float,
        y_pos: float,
        width: float,
        height: float,
    ) -> None:
        self._i_slipRatio = i_slipRatio

        self._region = Region(x_pos, y_pos, width, height)
        self._chart = Chart(
            self._region,
            x_axis_marker_color=white.transparent,
            axis_segment_count=4,
            x_axis_marker_length_ratio=1.0,
            y_axis_marker_length_ratio=1.0,
        )
        self._quad_bar = QuadBar(
            region=self._region,
            color=red.a4,
            centered_y_scale=True,
        )
        self._temperature_text = BigText(
            region=self._region.top_half,
            text='',
            font_color=white.full,
            expected_text_len=3,
        )
        self._pressure_text = BigText(
            region=self._region.bottom_half,
            text='',
            font_color=white.full,
            expected_text_len=3,
        )

    def render(self) -> None:
        # draw axes
        self._chart.draw_axes()

        # fetch telemetry
        slipRatio = ac_api[CS.SlipRatio].wma()[self._i_slipRatio]
        temperature = ac_mem.physics.tyreCoreTemperature[self._i_slipRatio]  # type: float
        pressure = ac_mem.physics.wheelsPressure[self._i_slipRatio]  # type: float

        # plot the indicators
        self._quad_bar.plot(
            num(slipRatio).normalize(3.0).clip(-1, 1).f
        )
        self._temperature_text.text = str(round(temperature, 1))
        self._pressure_text.text = str(round(pressure, 1))


class SlipRatioMonitor(Monitor):
    data_keys = (CS.SlipRatio, )
    enabled = config.TyreInfoMonitor.enabled
    col_index = config.TyreInfoMonitor.col_index

    def __init__(
        self,
        x_pos: float,
        y_pos: float,
    ) -> None:
        super().__init__(x_pos, y_pos)

        self._width = width = config.App.span_len*config.TyreInfoMonitor.col_span
        self._height = height = config.App.height

        self._tyres_slip_ratio_monitors = [
            _TyreSlipRatioMonitor(
                i_slipRatio=i,
                x_pos=_x_pos,
                y_pos=_y_pos,
                width=width/2,
                height=height/2,
            )
            for i, (_x_pos, _y_pos) in enumerate((
                (x_pos, y_pos),
                (x_pos+width/2, y_pos),
                (x_pos, y_pos+height/2),
                (x_pos+width/2, y_pos+height/2),
            ))
        ]

    @property
    def width(self) -> float: return self._width
    @property
    def height(self) -> float: return self._height

    def render(self) -> None:
        for monitor in self._tyres_slip_ratio_monitors:
            monitor.render()
