from initialize import *
from random import randint, choice

rb.speed(0)
rb.pensize(7)
rb.forward(100)

direction = [90, -90, 180]
#direction_setheading = [0, 90, 180, 270]


def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    random_color = (r,g,b)
    return random_color


for _ in range(200):
    rb.pencolor(random_color())
    random_direction = choice(direction)
    #random_heading = choice(direction_setheading)
    rb.forward(50)
    #rb.setheading(random_heading)
    rb.right(random_direction)


screen.exitonclick()