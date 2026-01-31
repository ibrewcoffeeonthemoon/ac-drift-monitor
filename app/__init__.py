import ac

from app.indicator import Indicator


class App:
    name = 'AC Drift Monitor'
    width = 333
    height = 173
    bg_path = 'apps/python/ac-drift-monitor/bg.png'

    def __init__(self) -> None:
        self.win = ac.newApp(self.name)
        ac.setSize(self.win, self.width, self.height)
        ac.drawBorder(self.win, False)
        ac.setBackgroundOpacity(self.win, 0)
        ac.setBackgroundTexture(self.win, self.bg_path)

        self.lateralGIndicator = Indicator(self.win, 22, 62, "Lat.")
        self.longitudinalGIndicator = Indicator(self.win, 22, 136, "Lon.")
