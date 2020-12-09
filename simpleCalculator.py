# Program: a simple calculator that add, subtracts, multiply, and divides user values.

# function add: adds two numbers
def add(a,b):
    return a+b

# function subtract: subtract two numbers
def subtract(a,b):
    return a-b

# function divide: divide two numbers
def divide(a,b):
    return a/b

# function multiply: multiply two numbers
def multiply(a,b):
    return a*b

print("MENU: ")
print("Please select a operation ")
print("1.Add (+)")
print("2.Subtract (-)")
print("3.Divide (/)")
print("4.Multiply (x)")


while True:
    value = input("please enter operation:")

    if value in ('1', '2', '3', '4'):
        number1 = int(input("Enter first number: "))
        number2 = int(input("Enter second number: "))
        print("Answer:")
        if value == '1':
            print(number1, "+", number2, "=", add(number1, number2))
        if value == '2':
            print(number1, "-", number2, "=", subtract(number1, number2))
        if value == '3':
            print(number1, "/", number2, "=", divide(number1, number2))
        if value == '4':
            print(number1, "*", number2, "=", multiply(number1, number2))
        break
    else:
            print("Invalid please try again")
