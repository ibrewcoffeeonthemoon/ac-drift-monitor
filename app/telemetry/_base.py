from abc import ABCMeta, abstractmethod


class DataSource(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._data = ()  # type: tuple[float, ...]

    @abstractmethod
    def fetch(self, car_id: int) -> None:
        ...

    def __iter__(self):
        yield from self._data

    def __getitem__(self, index: int) -> float:
        return self._data[index]
