from collections import deque
from itertools import islice


class History:
    def __init__(
        self,
        maxlen: int,
    ) -> None:
        self._maxlen = maxlen
        self._data = deque(maxlen=maxlen)  # type: deque[tuple[float, ...]]

    def append(self, val: 'tuple[float, ...]') -> None:
        self._data.append(val)

    @property
    def last(self) -> 'tuple[float, ...]':
        return self._data[-1]

    # def simple_average(self, n: int) -> 'tuple[float, ...]':
    #     window = islice(self._data, self._maxlen-n, self._maxlen)
    #     answer = tuple(sum(series)/n for series in zip(*window))
    #     return answer
