import ac


class _Ext:
    def __init__(self) -> None:
        # init
        self._car_id = ac.getFocusedCar()

    @property
    def handbrake(self) -> float:
        return ac.ext_getHandbrake(self._car_id)


# export
ext = _Ext()
