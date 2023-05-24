from flask import Flask
from random import randint


app = Flask(__name__)


def check_right_number(function):
    def wrapper(*args):
        num = function(args)
        guess = args[0]
        if num == guess:
            return '<h1 style="color: #00FF00">You found me!</h1>'\
                   '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
        elif guess > num:
            return '<h1 style="color: #FF00FF">Too high, try again!</h1>' \
                   '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
        else:
            return '<h1 sty' \
                   'le="color: #FF0000">Too low, try again!</h1>' \
                   '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    return wrapper


@check_right_number
def pick_a_number(guess):
    return randint(0, 9)


@app.route('/')
def home():
    return "<h1>Guess a number between 0 and 9</h1>" \
           "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


@app.route('/<int:guess>')
def game(guess):
    return pick_a_number(guess)


if __name__ == "__main__":
    app.run(debug=True)