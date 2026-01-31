##############################################################
# Kunos Simulazioni
# AC Python tutorial 04 : Get data from AC
#
# To activate create a folder with the same name as this file
# in apps/python. Ex apps/python/tutorial01
# Then copy this file inside it and launch AC
#############################################################

import ac

from app import App


# This function gets called by AC when the Plugin is initialised
# The function has to return a string with the plugin name
def acMain(ac_version: str) -> str:
    # create App
    global app
    app = App()

    # register render callback
    ac.addRenderCallback(app.window, onRender)

    # return App name
    return app.name


def onRender(deltaT: float) -> None:
    # render
    global app
    app.render()
