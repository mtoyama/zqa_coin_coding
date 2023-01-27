def calculate():
    operation = input("Enter an operation (+, -, *, /): ")
    if operation not in ['+', '-', '*', '/']:
        print("Invalid operator")
        return
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2
    print(f"Result: {result}")

calculate()
