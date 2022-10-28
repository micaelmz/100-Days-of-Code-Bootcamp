from extracted_colors import rgb_colors
from random import choice
from turtle_configurations import *


def random_color():
    return choice(rgb_colors)


def dot_line(coordinates):
    mt.goto(coordinates)
    for c in range(10):
        mt.dot(20, random_color())
        mt.forward(50)



for c in range(10):
    dot_line(coordinates)
    coordinates = (coordinates[0], coordinates[1]+50)


screen.exitonclick()