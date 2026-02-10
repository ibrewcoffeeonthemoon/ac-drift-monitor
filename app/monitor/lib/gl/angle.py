import math

from ....lib.color import *
from ....lib.geometry import Vertex
from ....lib.number import num
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
    x_center = x_pos+width/2
    y_center = y_pos+height/2
    radius = math.sqrt(width**2 + height**2)/2
    x_coord = radius * math.cos(radian_angle)
    y_coord = radius * math.sin(radian_angle)
    line(
        Vertex(
            num(x_center+x_coord).clip(x_pos, x_pos+width).f,
            num(y_center-y_coord).clip(y_pos, y_pos+height).f,
        ),
        Vertex(
            num(x_center-x_coord).clip(x_pos, x_pos+width).f,
            num(y_center+y_coord).clip(y_pos, y_pos+width).f
        ),
        color=color,
    )
