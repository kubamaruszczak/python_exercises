from flask import Flask
from random import randint

num_to_guess = randint(0, 9)
print(num_to_guess)

app = Flask(__name__)


@app.route('/')
def main_page():
    return '<h1>Guess a number between 0 and 9</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:number>')
def guess_page(number):
    if number == num_to_guess:
        return '<h1 style="color: green;">You found me!</h1>' \
               '<img src="https://media3.giphy.com/media/BPJmthQ3YRwD6QqcVD/giphy.gif?cid=ecf05e47ayvqrc7n7hofio87f' \
               'q6qs69000eszx7y6p0gakk1&rid=giphy.gif&ct=g">'
    elif number > num_to_guess:
        return '<h1 style="color: purple;">Too high, try again!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1 style="color: red;">Too low, try again!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
