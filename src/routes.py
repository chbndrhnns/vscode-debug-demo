from flask import Blueprint, render_template, request

from src.core import add, divide, add_if_even_index_subtract_if_odd_position

main = Blueprint('main', __name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/add/<int:a>/<int:b>')
def add_endpoint(a, b):
    return add(a, b)


@main.route('/divide/<int:a>/<int:b>')
def divide_endpoint(a, b):
    return divide(a, b)


@main.route('/complex')
def complex_logic_endpoint():
    data = request.args.get('data')
    try:
        result = add_if_even_index_subtract_if_odd_position(data)
        return f"Result: {result}"
    except ValueError as e:
        return f"An error occurred: {str(e)}"
