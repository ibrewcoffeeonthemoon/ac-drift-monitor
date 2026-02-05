import ac

import config
from app.components import Component
from app.components.gforce_monitor import GForceMonitor
from app.components.slip_ratio_monitor import SlipRatioMonitor
from app.window import window


class _App:
    def __init__(self) -> None:
        # create components
        self._components = []  # type: list[Component]
        self._components.append(SlipRatioMonitor(x_pos=self._x_current, y_pos=self._y_current))
        self._components.append(GForceMonitor(x_pos=self._x_current, y_pos=self._y_current))

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

    def render(self) -> None:
        for component in self._components:
            component.render()


# export
app = _App()
