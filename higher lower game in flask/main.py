from flask import Flask
import random

rand_num = random.randint(0,9)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1>Guess a number between 0 and 9</h1>'\
           '<img src="https://i.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.webp">'

@app.route("/<int:num>")
def check(num):
    if num > rand_num:
        return '<h1 style="color: purple;">Too High,try again!</h1>'\
               '<img src="https://i.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.webp">'
    elif num < rand_num:
        return '<h1 style="color: red;">Too Low,try again!</h1>'\
               '<img src="https://i.giphy.com/media/jD4DwBtqPXRXa/giphy.webp">'
    else:
        return '<h1 style="color: green;">You found me!</h1>'\
               '<img src="https://i.giphy.com/media/4T7e4DmcrP9du/giphy.webp">'

if __name__ == "__main__":
    app.run(debug=True)