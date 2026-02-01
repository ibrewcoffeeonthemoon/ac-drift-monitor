import ac

from app import app
from app.data import telemetry


# This function gets called by AC when the Plugin is initialised
# The function has to return a string with the plugin name
def acMain(ac_version: str) -> str:
    # register render callback
    ac.addRenderCallback(app.window, on_render)

    # return App name
    return app.name


def acUpdate(deltaT: float) -> None:
    # fetch car state values
    telemetry.fetch()


def on_render(deltaT: float) -> None:
    # render
    app.render()
