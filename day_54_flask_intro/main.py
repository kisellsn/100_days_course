import time

from flask import Flask

app = Flask(__name__)


def delay_decorator(function):
    def wrapper():
        time.sleep(2)
        function()

    return wrapper


@delay_decorator
def hello_world():
    print("Hello World!")


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    hello_world()
    app.run(debug=True)
