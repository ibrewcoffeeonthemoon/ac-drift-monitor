from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
    enabled = True

    @abstractmethod
    def __init__(
        self,
        x_pos: int,
        y_pos: int,
    ) -> None:
        ...

    @abstractmethod
    def render(self) -> None:
        ...

    @property
    @abstractmethod
    def width(self) -> int:
        ...

    @property
    @abstractmethod
    def height(self) -> int:
        ...
