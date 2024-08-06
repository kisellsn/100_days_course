import time

from flask import Flask

app = Flask(__name__)
NUMBER = 4


@app.route('/')
def hello_world():
    return 'Guess a number between 0 and 9'


# def make_bold(function):
#     def wrapper(*args, **kwargs):
#         return f'<b>{function(kwargs[0])}</b>'
#     return wrapper


@app.route('/<int:number>')
def number_manager(number):
    if number > NUMBER:
        return ("<h3>Too high</h3>"
                "<img src='https://media0.giphy.com/media/v1"
                ".Y2lkPTc5MGI3NjExbms1cnNyNDB5Z25wMTRqMTNsZnRrNHhyMm5tbXZpZmYwYjc2cnNvNiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Tfi5w35wly0x2/200.webp' />")
    elif number < NUMBER:
        return ("<h3>Too low</h3>"
                "<img src='https://media2.giphy.com/media/v1"
                ".Y2lkPTc5MGI3NjExYjVjZWF2ano4bm5tdmNqNnRiM3p5b3lhOHhjMjczbThhemhyajg3eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/lpOMzrjrSKYOA/giphy.webp' />")
    else:
        return ("<h1>You won!</h1>"
                "<img src='https://media3.giphy.com/media/v1"
                ".Y2lkPTc5MGI3NjExbWxjMnh0eTZpMHRrNzFzYnlhaXduN205NGhyc2Q3ajg1enVqNmp6ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hzBc3HCFc0icM/giphy.webp' />")


if __name__ == '__main__':
    app.run(debug=True)
