from abc import ABCMeta, abstractmethod

from ..telemetry import ac_api


class Component(metaclass=ABCMeta):
    @abstractmethod
    def render(self) -> None:
        ...


class Monitor(Component):
    data_keys = ()  # type: tuple[int, ...]
    enabled = True
    col_index = 0

    def __init__(
        self,
        x_pos: float,
        y_pos: float,
    ) -> None:
        ac_api.register(*self.data_keys)

    @property
    @abstractmethod
    def width(self) -> float:
        ...

    @property
    @abstractmethod
    def height(self) -> float:
        ...
