from collections import deque


class MovingAverage:
    def __init__(
        self,
        scale: float = 1.0,
        weights: 'tuple[float, ...]' = (.2, .2, .2, .1, .1, .1, .1),
        initial_value: float = 0.0,
        min: float = -1.0,
        max: float = +1.0,
    ) -> None:
        self._scale = scale
        self._len = n = len(weights)
        self._weights = weights
        self._min = min
        self._max = max
        self._deque = deque([initial_value for _ in range(n)], maxlen=n)

    def update(self, val: float) -> None:
        # normalize
        val = val / self._scale

        # clipping
        val = min(max(val, self._min), self._max)

        # append
        self._deque.append(val)

    @property
    def last(self) -> float:
        return self._deque[-1]

    @property
    def simple_average(self) -> float:
        avg = sum(self._deque) / self._len
        return avg

    @property
    def weighted_average(self) -> float:
        pairs = zip(self._weights, self._deque)
        weighted_sum = sum((w*v for w, v in pairs))
        return weighted_sum
