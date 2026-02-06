import ac


class _Telemetry:
    def __init__(self) -> None:
        # requested data keys
        self._data_keys = set()  # type: set[int]

        # data dictionary
        self._data = {
            key: ()
            for key in self._data_keys
        }  # type: dict[int, tuple[float, ...]]

        # init
        self._car_id = ac.getFocusedCar()

    def __getitem__(self, key: int) -> 'tuple[float, ...]':
        return self._data[key]

    def register(self, *keys: int) -> None:
        for key in keys:
            self._data_keys.add(key)

    def fetch(self) -> None:
        for key in self._data_keys:
            # val could be a scalar, 3d or 4d vector
            val = ac.getCarState(self._car_id, key)
            if not isinstance(val, tuple):
                val = (val, )
            self._data[key] = val


# export
telemetry = _Telemetry()
