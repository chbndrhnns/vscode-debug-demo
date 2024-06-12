def add(a, b):
    result = a + b
    return f"The result of {a} + {b} is {result}"


def divide(a, b):
    try:
        result = a / b
        return f"The result of {a} / {b} is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"


def add_if_even_index_subtract_if_odd_position(data):
    # Simulate complex logic
    if not data:
        raise ValueError("No data provided")
    
    result = 0
    for i in range(len(data)):
        if i % 2 == 0:
            result += int(data[i]) 
        else:
            result -= int(data[i])
    
    return result



if __name__ == "__main__":
    result = add(5, 3)
    print(result)
