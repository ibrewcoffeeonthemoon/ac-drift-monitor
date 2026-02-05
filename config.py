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


class App:
    height = _int('App', 'height')
    span_len = height//2


class GForceMonitor:
    col_span = _int('GForceMonitor', 'col_span')


class SlipRatioMonitor:
    col_span = _int('SlipRatioMonitor', 'col_span')
