from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
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
