import math

from ....lib.color import *
from ....lib.geometry import Vertex
from .line import line


def angle_line(
    x_pos: int,
    y_pos: int,
    width: int,
    height: int,
    angle_degree: float,
    color: Color,
) -> None:
    radian_angle = math.pi * angle_degree/180
    x_start = x_pos+width/2
    y_start = y_pos+height/2
    radius = math.sqrt(width**2 + height**2)/2
    x_coord = radius * math.cos(radian_angle)
    y_coord = radius * math.sin(radian_angle)
    line(
        Vertex(x_start+x_coord, y_start-y_coord),
        Vertex(x_start-x_coord, y_start+y_coord),
        color=color,
    )
