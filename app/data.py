from abc import ABCMeta, abstractmethod

import ac
import acsys


class _Data(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._data = ()  # type: tuple[float, ...]

    @abstractmethod
    def fetch(self, car_id: int) -> None:
        ...

    def __iter__(self):
        yield from self._data

    def __getitem__(self, index: int) -> float:
        return self._data[index]


class _AccG(_Data):
    def __init__(self) -> None:
        super().__init__()
        self._data = (0.0, 0.0, 0.0)

    def fetch(self, car_id: int) -> None:
        self._data = ac.getCarState(car_id, acsys.CS.AccG)

    @property
    def x(self) -> float: return self._data[0]

    @property
    def y(self) -> float: return self._data[1]

    @property
    def z(self) -> float: return self._data[2]


class _SlipRatio(_Data):
    def __init__(self) -> None:
        super().__init__()
        self._data = (0.0, 0.0, 0.0, 0.0)

    def fetch(self, car_id: int) -> None:
        self._data = ac.getCarState(car_id, acsys.CS.SlipRatio)

    @property
    def fl(self) -> float: return self._data[0]

    @property
    def fr(self) -> float: return self._data[1]

    @property
    def rl(self) -> float: return self._data[2]

    @property
    def rr(self) -> float: return self._data[3]


class _Telemetry:

    def __init__(self) -> None:
        # data
        self.accG = _AccG()
        self.slipRatio = _SlipRatio()

        # init
        self._car_id = ac.getFocusedCar()

    def fetch(self) -> None:
        self.accG.fetch(self._car_id)
        self.slipRatio.fetch(self._car_id)


# export
telemetry = _Telemetry()
