import ac

from app.settings.window import window


class _Settings:
    def __init__(
        self,
        width: int,
        height: int,
    ) -> None:
        # state
        self._visible = False

        # set layouts, styles
        ac.setSize(window, width, height)

        # init
        self.visible = False

    @property
    def visible(self) -> bool:
        return self._visible

    @visible.setter
    def visible(self, val: bool) -> None:
        self._visible = val
        ac.setVisible(window, self._visible)

    def toggle_visible(self) -> None:
        self.visible = not self.visible


settings = _Settings(
    width=500,
    height=500,
)
