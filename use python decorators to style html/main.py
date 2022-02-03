from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wraper():
        x=f"<b>{func()}</b>"
        return x
    return wraper
def make_emphasis(func):
    def wraper():
        x=f"<em>{func()}</em>"
        return x
    return wraper
def make_underlined(func):
    def wraper():
        x=f"<u>{func()}</u>"
        return x
    return wraper


@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "Hello, World"

if __name__ == "__main__":
    app.run(debug=True)