operator = input("Enter operator (+,-,*,/):")
    
num1 = input("Enter the first number: ")     
    
num2 = input("Enter the second number: ")

num1 = int(num1)
num2 = int(num2)

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2

print(result)