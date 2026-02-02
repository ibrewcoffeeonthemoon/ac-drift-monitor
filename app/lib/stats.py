from collections import deque


class MovingAverage:
    def __init__(
        self,
        weights: tuple = (0.4, 0.3, 0.2, 0.1),
        initial_value: float = 0.0,
    ) -> None:
        self._len = n = len(weights)
        self._weights = weights
        self._deque = deque([initial_value for _ in range(n)], maxlen=n)

    def update(self, val: float) -> None:
        self._deque.append(val)

    @property
    def simple_average(self) -> float:
        return sum(self._deque) / self._len
