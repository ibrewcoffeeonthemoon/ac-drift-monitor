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
        self.window = ac.newApp(self.name)

        # set layouts, styles
        ac.setSize(self.window, self.width, self.height)
        ac.drawBorder(self.window, False)
        ac.setBackgroundOpacity(self.window, 0)
        ac.setBackgroundTexture(self.window, self.bg_img_path)

        # create indicators
        self._ind_latG = Indicator(self.window, 22, 62, "Lat.", arrow_on_top=True)
        self._ind_longG = Indicator(self.window, 22, 136, "Lon.", arrow_on_top=False)

        # init
        self.car_id = ac.getFocusedCar()

    def render(self) -> None:
        # fetch car state values
        x, y, z = ac.getCarState(self.car_id, acsys.CS.AccG)

        # set indicator values
        self._ind_latG.value = x
        self._ind_longG.value = z
