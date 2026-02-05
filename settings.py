import configparser
import os


class _Config:
    project_dir = os.path.dirname(__file__)
    config_ini_path = os.path.join(project_dir, 'config.ini')

    def __init__(self) -> None:
        self._parser = configparser.ConfigParser()
        self._parser.read(self.config_ini_path)

    @property
    def height(self) -> int:
        return self._parser.getint('APP', 'height')


config = _Config()
