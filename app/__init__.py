import ac

import config

from .components import *
from .window import window


class _App:
    def __init__(self) -> None:
        # attach components
        self._components = []  # type: list[Component]
        for monitor_class in sorted(MONITOR_CLASSES, key=lambda cls: cls.col_index):
            self._attach(monitor_class)  # type: ignore[type-abstract]

        # set layouts, styles
        ac.setSize(
            window,
            round(sum(c.width for c in self._components)),
            config.App.height,
        )
        ac.setTitle(window, '')
        ac.setIconPosition(window, 0, -10000)
        ac.drawBorder(window, False)

    @property
    def _x_current(self) -> int:
        return sum(c.width for c in self._components)

    @property
    def _y_current(self) -> int:
        return 0

    def _attach(self, cls: 'type[Component]') -> None:
        if cls.enabled:
            self._components.append(cls(
                x_pos=self._x_current,
                y_pos=self._y_current
            ))

    def render(self) -> None:
        for component in self._components:
            component.render()


# export
app = _App()
