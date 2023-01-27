operator = input("Enter operator (+,-,*,/):")
    
if operator == "+":
    result = number_change + number_change2
elif operator == "-":
    result = number_change - number_change2
elif operator == "*":
    result = number_change * number_change2
elif operator == "/":
    result = number_change / number_change2


num1 = input("Enter the first number: ")
number_change = int(num1)
             
num2 = input("Enter the second number: ")
number_change2 = int(num2)
             
print(result)