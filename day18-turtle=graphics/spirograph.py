from initialize import *
from random import randint, choice
rb.speed(0)


def random_color(b):
    r = 0
    g = 0
    random_color = (r, g, int(b // 1.4))
    return random_color

for circle in range(0, 360, 7):
    rb.color(random_color(circle))
    '''
    for angle in range(0, 360, 10):
        rb.setheading(angle+circle)
        rb.forward(20)
    '''
    rb.circle(100)
    rb.setheading(circle)

screen.exitonclick()