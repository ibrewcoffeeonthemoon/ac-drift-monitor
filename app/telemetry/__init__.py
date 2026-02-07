import ac

from .history import History


class _Telemetry:
    def __init__(self) -> None:
        # requested data keys
        self._data_keys = set()  # type: set[int]

        # data history
        self._data = dict()  # type: dict[int, History]

        # init
        self._car_id = ac.getFocusedCar()

    def __getitem__(self, key: int) -> History:
        return self._data[key]

    def register(self, *keys: int) -> None:
        for key in keys:
            self._data_keys.add(key)
            if key not in self._data:
                self._data[key] = History(100)

    def fetch(self) -> None:
        for key in self._data_keys:
            # val could be a scalar, 3d or 4d vector
            val = ac.getCarState(self._car_id, key)
            if not isinstance(val, tuple):
                val = (val, )
            self._data[key].append(val)


# export
telemetry = _Telemetry()
