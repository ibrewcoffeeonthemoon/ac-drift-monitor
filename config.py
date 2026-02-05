import configparser
import os

project_root = os.path.dirname(__file__)
path = os.path.join(project_root, 'config.ini')
parser = configparser.ConfigParser()
parser.read(path)

_int = parser.getint
_float = parser.getfloat
_boolean = parser.getboolean
_str = parser.get


class APP:
    height = _int('APP', 'height')
