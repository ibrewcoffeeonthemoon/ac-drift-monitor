from abc import ABCMeta, abstractmethod

from app.components.lib.chart import Chart


class Indicator(metaclass=ABCMeta):
    def __init__(
        self,
        chart: Chart,
    ) -> None:
        self._chart = chart

    @abstractmethod
    def plot(self, *args, **kwargs) -> None:
        ...
