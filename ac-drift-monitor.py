import ac

from app import App


# This function gets called by AC when the Plugin is initialised
# The function has to return a string with the plugin name
def acMain(ac_version: str) -> str:
    # create App
    global app
    app = App()

    # register render callback
    ac.addRenderCallback(app.window, on_render)

    # return App name
    return app.name


def on_render(deltaT: float) -> None:
    # render
    global app
    app.render()
