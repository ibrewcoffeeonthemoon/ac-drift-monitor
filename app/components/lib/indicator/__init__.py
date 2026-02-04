from abc import ABCMeta, abstractmethod

from app.components.lib.chart import Chart


class Indicator(metaclass=ABCMeta):
    def __init__(
        self,
        chart: Chart,
    ) -> None:
        self._chart = chart
        self._x_pos = self._chart.x_pos
        self._y_pos = self._chart.y_pos
        self._width = self._chart.width
        self._height = self._chart.height

    @abstractmethod
    def plot(self, *args, **kwargs) -> None:
        ...
