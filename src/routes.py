from flask import Blueprint, render_template, request

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
    

@main.route('/complex')
def complex_logic():
    data = request.args.get('data')
    try:
        result = process_complex_logic(data)
        return f"Result: {result}"
    except Exception as e:
        return f"An error occurred: {str(e)}"

def process_complex_logic(data):
    # Simulate complex logic
    if not data:
        raise ValueError("No data provided")
    
    result = 0
    for i in range(1, len(data) + 1):
        if i % 2 == 0:
            result += int(data[i - 1])
        else:
            result -= int(data[i - 1])
    
    return result