a = float(input("Enter 1st number :"))
operator = input("Enter(+,-,*,/,%,**) :")
b = float(input("Enter 2nd number :"))

if operator == "+":
    print("The result is :", a + b)

elif operator == "-":
    print("The result is :", a - b)

elif operator == "*":
    print("The result is :", a * b)

elif operator == "/":
    print("The result is :", a / b)

elif operator == "%":
    print("The result is :", a % b)

elif operator == "**":
    print("The result is :", a ** b)

else:
    print("Invalid operation")