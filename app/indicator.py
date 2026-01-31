import ac
import acsys


class Indicator:
    maxG = 2
    barLength = 322
    triangleWidth = 10

    def __init__(
        self,
        window: int,
        x: int,
        y: int,
        name: str,
        arrow_on_top: bool,
    ) -> None:
        self.xPosition = x
        self.yPosition = y
        self.counter = 0
        self.secondsToFade = 3
        self.value = 0
        self.oldValue = 0
        self.maxValue = 0
        self.arrow_on_top = arrow_on_top

        ac.setPosition(ac.addLabel(window, name), x, y)
        self.currentValueLabel = ac.addLabel(window, "0.0g")
        ac.setPosition(self.currentValueLabel, x+50, y)
        self.indicatorWidth = 10
        self.indicatorPosition = 0

    def set_value(self, value: float) -> None:
        # clip value
        self.value = min(max(value, -self.maxG), self.maxG)

        # smooth value
        weight = 0.2
        self.value = self.oldValue*weight + self.value*(1-weight)

        # round value
        self.value = round(self.value*100)/100

        # display
        ac.setText(self.currentValueLabel, "{0}g".format(abs(self.value)))
        if (abs(self.value) < 0.1):
            self.value = 0
            ac.setText(self.currentValueLabel, "0.0g")

        # calc indicator position
        self.indicatorPosition = self.value/self.maxG

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

    def drawBar(self) -> None:
        ac.glColor4f(1, 1, 1, 1)
        ac.glQuad(0, 55, 300, 7)
        ac.glColor4f(1, 1, 1, 1)
        ac.glQuad(148, 45, 4, 27)
