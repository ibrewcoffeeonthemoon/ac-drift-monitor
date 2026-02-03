import ac
import acsys


class _AccG:
    def __init__(self) -> None:
        self.x = 0.0
        self.y = 0.0
        self.z = 0.0

    def fetch(self, car_id: int) -> None:
        self.x, self.y, self.z = ac.getCarState(car_id, acsys.CS.AccG)

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z


class _SlipRatio:
    def __init__(self) -> None:
        self._data = (0.0, 0.0, 0.0, 0.0)

    def fetch(self, car_id: int) -> None:
        self._data = ac.getCarState(car_id, acsys.CS.SlipRatio)

    def __iter__(self):
        yield from self._data

    def __getitem__(self, index: int) -> float:
        return self._data[index]

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
