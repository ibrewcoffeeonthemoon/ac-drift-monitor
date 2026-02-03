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
        self.fl = 0.0
        self.fr = 0.0
        self.rl = 0.0
        self.rr = 0.0

    def fetch(self, car_id: int) -> None:
        self.fl, self.fr, self.rl, self.rr = ac.getCarState(car_id, acsys.CS.SlipRatio)

    def __iter__(self):
        yield self.fl
        yield self.fr
        yield self.rl
        yield self.rr

    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self.fl
        elif index == 1:
            return self.fr
        elif index == 2:
            return self.rl
        elif index == 3:
            return self.rr
        else:
            raise IndexError


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
