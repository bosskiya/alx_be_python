#/usr/bin/env python3

def perform_operation(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            print("Division by zero (0) is not allowed")
            return
        return num1 / num2
    else:
        print("Only add, subtract, multiply, and divide operations are allowed")