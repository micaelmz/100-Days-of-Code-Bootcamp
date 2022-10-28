import turtle

from turtle_settings import *


def move_fowards():
    turtle.forward(10)

def move_backwards():
    turtle.backward(10)

def turn_clockwise():
    turtle.right(10)

def turn_counter_clockwise():
    turtle.left(10)

def reset():
    turtle.reset()

screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='w', fun=move_fowards)
screen.onkey(key='d', fun=turn_clockwise)
screen.onkey(key='a', fun=turn_counter_clockwise)
screen.onkey(key='c', fun=reset)

screen.exitonclick()