from abc import ABCMeta, abstractmethod

from app.components.lib.chart import Chart


class Indicator(metaclass=ABCMeta):
    def __init__(
        self,
        chart: Chart,
        inverted_x_scale: bool,
        inverted_y_scale: bool,
        centered_x_scale: bool,
        centered_y_scale: bool,
    ) -> None:
        self._chart = chart
        self._x_pos = self._chart.x_pos
        self._y_pos = self._chart.y_pos
        self._width = self._chart.width
        self._height = self._chart.height
        self._inverted_x_scale = inverted_x_scale
        self._inverted_y_scale = inverted_y_scale
        self._centered_x_scale = centered_x_scale
        self._centered_y_scale = centered_y_scale

    @abstractmethod
    def plot(self, *args, **kwargs) -> None:
        ...
