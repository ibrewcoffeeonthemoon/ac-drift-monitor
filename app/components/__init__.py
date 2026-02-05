from abc import ABCMeta, abstractmethod


class Component(metaclass=ABCMeta):
    @abstractmethod
    def render(self) -> None:
        ...
