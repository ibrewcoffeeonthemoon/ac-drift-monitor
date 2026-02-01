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


class Telemetry:

    def __init__(self) -> None:
        # data
        self.accG = _AccG()

        # init
        self._car_id = ac.getFocusedCar()

    def fetch(self) -> None:
        self.accG.fetch(self._car_id)
