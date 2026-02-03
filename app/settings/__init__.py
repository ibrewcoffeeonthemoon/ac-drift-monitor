import ac

from app.settings.window import window


class _Settings:
    def __init__(
        self,
        width: int,
        height: int,
    ) -> None:
        # set layouts, styles
        ac.setSize(window, width, height)
        ac.setVisible(window, True)


settings = _Settings(
    width=500,
    height=500,
)
