from initialize import *
from random import randint


def geometric(size):
    rb.pencolor(randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(size):
        rb.forward(100)
        rb.right(360/size)


for size in range(3, 11):
    geometric(size)


screen.exitonclick()