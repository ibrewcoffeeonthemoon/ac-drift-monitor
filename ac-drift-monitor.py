##############################################################
# Kunos Simulazioni
# AC Python tutorial 04 : Get data from AC
#
# To activate create a folder with the same name as this file
# in apps/python. Ex apps/python/tutorial01
# Then copy this file inside it and launch AC
#############################################################

import ac
import acsys

from app.indicator import Indicator

longitudinalGIndicator = 0
lateralGIndicator = 0
barLength = 322


# This function gets called by AC when the Plugin is initialised
# The function has to return a string with the plugin name
def acMain(ac_version: str) -> str:
    global longitudinalGIndicator, lateralGIndicator
    appWindow = ac.newApp("AC Drift Monitor")
    ac.setSize(appWindow, 333, 173)
    ac.drawBorder(appWindow, False)
    ac.setBackgroundOpacity(appWindow, 0)
    ac.setBackgroundTexture(appWindow, "apps/python/ac-drift-monitor/bg.png")
    lateralGIndicator = Indicator(appWindow, 22, 62, "Lat.")
    longitudinalGIndicator = Indicator(appWindow, 22, 136, "Lon.")
    ac.addRenderCallback(appWindow, onFormRender)
    return "AC Drift Monitor"


def onFormRender(deltaT: float) -> None:
    global longitudinalGIndicator, lateralGIndicator, barLength
    drawHTriangleIn(167 + (lateralGIndicator.indicatorPosition*(barLength/2)))
    drawLTriangleIn(167 + (longitudinalGIndicator.indicatorPosition*(barLength/2)))
    x, y, z = ac.getCarState(0, acsys.CS.AccG)
    longitudinalGIndicator.setCurrentValue(z)
    lateralGIndicator.setCurrentValue(x)


def drawBar() -> None:
    ac.glColor4f(1, 1, 1, 1)
    ac.glQuad(0, 55, 300, 7)
    ac.glColor4f(1, 1, 1, 1)
    ac.glQuad(148, 45, 4, 27)


def drawLTriangleIn(x: float) -> None:
    triangleWidth = 10
    ac.glColor4f(1, 0, 0, 1)
    ac.glBegin(acsys.GL.Triangles)
    ac.glVertex2f(x, 109)
    ac.glVertex2f(x-(triangleWidth/2), 109+triangleWidth)
    ac.glVertex2f(x+(triangleWidth/2), 109+triangleWidth)
    ac.glEnd()
    ac.glQuad(x-(triangleWidth/2), 109+triangleWidth, triangleWidth, triangleWidth/2)


def drawHTriangleIn(x: float) -> None:
    triangleWidth = 10
    ac.glColor4f(1, 0, 0, 1)
    ac.glBegin(acsys.GL.Triangles)
    ac.glVertex2f(x, 104)
    ac.glVertex2f(x-(triangleWidth/2), 104-triangleWidth)
    ac.glVertex2f(x+(triangleWidth/2), 104-triangleWidth)
    ac.glEnd()
    ac.glQuad(x-(triangleWidth/2), 104-(triangleWidth + triangleWidth/2), triangleWidth, triangleWidth/2)
