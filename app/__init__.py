import ac

from app.components.accG_bar import AccG_Bar
from app.data import Telemetry


class App:
    name = 'AC Drift Monitor'
    width = 333
    height = 173
    bg_img_path = 'apps/python/ac-drift-monitor/assets/bg.png'

    def __init__(self) -> None:
        # telemetry data
        self.telemetry = Telemetry()

        # create app window
        self._window = win = ac.newApp(self.name)

        # set layouts, styles
        ac.setSize(win, self.width, self.height)
        ac.drawBorder(win, False)
        ac.setBackgroundOpacity(win, 0)
        ac.setBackgroundTexture(win, self.bg_img_path)

        # create components
        self.accG_Bar = AccG_Bar(win, self.telemetry)

        # init
        self._car_id = ac.getFocusedCar()

    @property
    def window(self) -> int:
        return self._window

    def render(self) -> None:
        # set indicator values
        self.accG_Bar.render()
