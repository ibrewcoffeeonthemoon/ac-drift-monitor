import ac
import acsys


class Indicator:
    maxG = 2
    barLength = 322
    triangleWidth = 10

    def __init__(
        self,
        appWindow: int,
        x: int,
        y: int,
        name: str,
        arrow_on_top: bool,
    ) -> None:
        self.xPosition = x
        self.yPosition = y
        self.counter = 0
        self.secondsToFade = 3
        self.currentValue = 0
        self.oldValue = 0
        self.maxValue = 0
        self.arrow_on_top = arrow_on_top

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

        # draw triangle
        if self.arrow_on_top:
            self.drawHTriangleIn(167 + (self.indicatorPosition*(self.barLength/2)))
        else:
            self.drawLTriangleIn(167 + (self.indicatorPosition*(self.barLength/2)))

    def drawLTriangleIn(self, x: float) -> None:
        w = self.triangleWidth
        ac.glColor4f(1, 0, 0, 1)
        ac.glBegin(acsys.GL.Triangles)
        ac.glVertex2f(x, 109)
        ac.glVertex2f(x-(w/2), 109+w)
        ac.glVertex2f(x+(w/2), 109+w)
        ac.glEnd()
        ac.glQuad(x-(w/2), 109+w, w, w/2)

    def drawHTriangleIn(self, x: float) -> None:
        w = self.triangleWidth
        ac.glColor4f(1, 0, 0, 1)
        ac.glBegin(acsys.GL.Triangles)
        ac.glVertex2f(x, 104)
        ac.glVertex2f(x-(w/2), 104-w)
        ac.glVertex2f(x+(w/2), 104-w)
        ac.glEnd()
        ac.glQuad(x-(w/2), 104-(w + w/2), w, w/2)
