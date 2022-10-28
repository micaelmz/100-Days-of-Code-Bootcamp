from turtle import Turtle, Screen
from random import randint

# Settings
screen = Screen()
screen.colormode(255)
screen.setup(width=500, height=400)
screen.listen()
screen.title('Corrida de tartarugas.')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']


def hatch_an_egg(list):
    turtles = []
    pos = -90
    for color in list:
        new_turtle = Turtle(shape='turtle')
        new_turtle.penup()
        new_turtle.color(color)
        new_turtle.goto(x=-230, y=pos)
        pos += 30
        turtles.append(new_turtle)
    return turtles


turtles = hatch_an_egg(colors)

user_bet = screen.textinput(title='Façam suas apostas', prompt='Qual tartaruga irá ganhar a corrida? Digite a cor em inglês ')

if user_bet:
    game_is_running = True
else:
    print('Escolha uma cor!')
    game_is_running = False

while game_is_running:
    for turtle in turtles:
        if turtle.xcor() > 230:
            game_is_running = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f'Você ganhou! A tartaruga {winning_color} foi a campeã.')
            else:
                print(f'Você perdeu! A tartaruga {winning_color} foi a campeã.')
        turtle.forward(randint(0, 10))


screen.exitonclick()
