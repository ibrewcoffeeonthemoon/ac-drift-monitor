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


class SlipRatioMonitor:
    enabled = _boolean('SlipRatioMonitor', 'enabled')
    col_index = _int('SlipRatioMonitor', 'col_index')
    col_span = _int('SlipRatioMonitor', 'col_span')


class GForceMonitor:
    enabled = _boolean('GForceMonitor', 'enabled')
    col_index = _int('GForceMonitor', 'col_index')
    col_span = _int('GForceMonitor', 'col_span')
    box_size = _float('GForceMonitor', 'box_size')


class SpeedMonitor:
    enabled = _boolean('SpeedMonitor', 'enabled')
    col_index = _int('SpeedMonitor', 'col_index')
    col_span = _int('SpeedMonitor', 'col_span')
