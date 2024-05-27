from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/add/<int:a>/<int:b>')
def add(a, b):
    result = a + b
    return f"The result of {a} + {b} is {result}"

@main.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    try:
        result = a / b
        return f"The result of {a} / {b} is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"