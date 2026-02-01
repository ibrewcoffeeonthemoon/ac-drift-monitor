import ac

from app.components.accG_bar import AccG_Bar
from app.window import window


class _App:
    width = 333
    height = 173

    def __init__(self) -> None:
        # set layouts, styles
        ac.setSize(window, self.width, self.height)
        ac.drawBorder(window, False)
        ac.setBackgroundOpacity(window, 0)

        # create components
        self.accG_Bar = AccG_Bar(window)

        # init
        self._car_id = ac.getFocusedCar()

    def render(self) -> None:
        # set indicator values
        self.accG_Bar.render()


# export
app = _App()
