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

from app import App
from app.indicator import Indicator


# This function gets called by AC when the Plugin is initialised
# The function has to return a string with the plugin name
def acMain(ac_version: str) -> str:
    global app
    app = App()
    ac.addRenderCallback(app.win, onFormRender)
    return app.name


def onFormRender(deltaT: float) -> None:
    global app
    barLength = Indicator.barLength
    x, y, z = ac.getCarState(0, acsys.CS.AccG)
    app.longitudinalGIndicator.setCurrentValue(z)
    app.lateralGIndicator.setCurrentValue(x)

    app.lateralGIndicator.drawHTriangleIn(167 + (app.lateralGIndicator.indicatorPosition*(barLength/2)))
    app.longitudinalGIndicator.drawLTriangleIn(167 + (app.longitudinalGIndicator.indicatorPosition*(barLength/2)))


def drawBar() -> None:
    ac.glColor4f(1, 1, 1, 1)
    ac.glQuad(0, 55, 300, 7)
    ac.glColor4f(1, 1, 1, 1)
    ac.glQuad(148, 45, 4, 27)
