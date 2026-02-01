import ac

from app.components.accG_bar import AccG_Bar


class _App:
    name = 'AC Drift Monitor'
    width = 333
    height = 173

    def __init__(self) -> None:
        # create app window
        self._window = win = ac.newApp(self.name)

        # set layouts, styles
        ac.setSize(win, self.width, self.height)
        ac.drawBorder(win, False)
        ac.setBackgroundOpacity(win, 0)

        # create components
        self.accG_Bar = AccG_Bar(win)

        # init
        self._car_id = ac.getFocusedCar()

    @property
    def window(self) -> int:
        return self._window

    def render(self) -> None:
        # set indicator values
        self.accG_Bar.render()


# export
app = _App()
