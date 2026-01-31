import ac


class Indicator:
    maxG = 2
    barLength = 322

    def __init__(
        self,
        appWindow: int,
        x: int,
        y: int,
        name: str,
    ) -> None:
        self.xPosition = x
        self.yPosition = y
        self.counter = 0
        self.secondsToFade = 3
        self.currentValue = 0
        self.oldValue = 0
        self.maxValue = 0

        ac.setPosition(ac.addLabel(appWindow, name), x, y)
        self.currentValueLabel = ac.addLabel(appWindow, "0.0g")
        ac.setPosition(self.currentValueLabel, x+50, y)
        self.indicatorWidth = 10
        self.indicatorPosition = 0

    def setCurrentValue(self, value: float) -> None:
        self.currentValue = min(max(value, -self.maxG), self.maxG)
        # filtering the values
        filter = 0.2
        self.currentValue = self.oldValue*(filter) + self.currentValue*(1-filter)
        self.currentValue = round(self.currentValue*100)/100
        ac.setText(self.currentValueLabel, "{0}g".format(abs(self.currentValue)))
        if (abs(self.currentValue) < 0.1):
            self.currentValue = 0
            ac.setText(self.currentValueLabel, "0.0g")

        self.indicatorPosition = self.currentValue/self.maxG
