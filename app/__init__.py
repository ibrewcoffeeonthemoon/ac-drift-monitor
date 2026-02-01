import ac

from app.components.accG_bar import AccG_Bar
from app.window import HEIGHT, WIDTH, window


class _App:
    def __init__(
        self,
        width: int,
        height: int,
    ) -> None:
        # set layouts, styles
        ac.setSize(window, width, height)
        ac.drawBorder(window, False)
        # ac.setBackgroundOpacity(window, 0)

        # create components
        self.accG_Bar = AccG_Bar()

        # init
        self._car_id = ac.getFocusedCar()

    def render(self) -> None:
        # set indicator values
        self.accG_Bar.render()


# export
app = _App(
    width=WIDTH,
    height=HEIGHT,
)
