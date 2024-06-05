def add(a, b):
    result = a + b
    return f"The result of {a} + {b} is {result}"


def divide(a, b):
    try:
        result = a / b
        return f"The result of {a} / {b} is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero"


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


if __name__ == "__main__":
    result = add(5, 3)
    print(result)
