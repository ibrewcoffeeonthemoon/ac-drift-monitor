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
    gforce_scale = _float('GForceMonitor', 'gforce_scale')
    slip_ratio_enabled = _boolean('GForceMonitor', 'slip_ratio_enabled')


class SlipAngleMonitor:
    enabled = _boolean('SlipAngleMonitor', 'enabled')
    col_index = _int('SlipAngleMonitor', 'col_index')
    col_span = _int('SlipAngleMonitor', 'col_span')
    sensitivity = _float('SlipAngleMonitor', 'sensitivity')
    wheel_degree = _int('SlipAngleMonitor', 'wheel_degree')


class SpeedMonitor:
    enabled = _boolean('SpeedMonitor', 'enabled')
    col_index = _int('SpeedMonitor', 'col_index')
    col_span = _int('SpeedMonitor', 'col_span')


class GearMonitor:
    enabled = _boolean('GearMonitor', 'enabled')
    col_index = _int('GearMonitor', 'col_index')
    col_span = _int('GearMonitor', 'col_span')


class PedalsMonitor:
    enabled = _boolean('PedalsMonitor', 'enabled')
    col_index = _int('PedalsMonitor', 'col_index')
    col_span = _int('PedalsMonitor', 'col_span')
