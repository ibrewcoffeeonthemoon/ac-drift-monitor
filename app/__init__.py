import ac
import acsys

from app.indicator import Indicator


class App:
    name = 'AC Drift Monitor'
    width = 333
    height = 173
    bg_img_path = 'apps/python/ac-drift-monitor/assets/bg.png'

    def __init__(self) -> None:
        # create app window
        self._window = ac.newApp(self.name)

        # set layouts, styles
        ac.setSize(self._window, self.width, self.height)
        ac.drawBorder(self._window, False)
        ac.setBackgroundOpacity(self._window, 0)
        ac.setBackgroundTexture(self._window, self.bg_img_path)

        # create indicators
        self._ind_latG = Indicator(self._window, 22, 62, "Lat.", arrow_on_top=True)
        self._ind_longG = Indicator(self._window, 22, 136, "Lon.", arrow_on_top=False)

        # init
        self._car_id = ac.getFocusedCar()

    @property
    def window(self) -> int:
        return self._window

    def render(self) -> None:
        # fetch car state values
        x, y, z = ac.getCarState(self._car_id, acsys.CS.AccG)

        # set indicator values
        self._ind_latG.value = x
        self._ind_longG.value = z
