number1 = int(input("enter number : "))
number2 = int(input("enter number : "))
math = input("Enter Operation : ")

if math == "+":
    result = number1 + number2
elif math == "-":
    result = number1 - number2
elif math == "*":
    result = number1 * number2
elif math == "/":
    if number2 == 0:
        print("Division by zero is not allowed. ")
    else:
        result = number1 / number2
else:
    print("invalid math")
        
if math in("+", "-", "*", "/"):
    print("The result is:", result)