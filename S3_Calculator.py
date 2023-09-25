from _tkinter import *

import math


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero"

def square_root(x):
    return math.sqrt(x)

def power(x, y):
    return math.pow(x, y)

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

# Main calculator loop
while True:
    print("Scientific Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Square Root")
    print("6. Power")
    print("7. Sine")
    print("8. Cosine")
    print("9. Tangent")
    print("0. Exit")

    choice = input("Enter your choice: ")

    if choice == '0':
        print("Exiting the calculator...")
        break

    if choice in ['1', '2', '3', '4', '6']:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

    elif choice in ['5', '7', '8', '9']:
        num1 = float(input("Enter the number: "))

    if choice == '1':
        print("Result: ", add(num1, num2))

    elif choice == '2':
        print("Result: ", subtract(num1, num2))

    elif choice == '3':
        print("Result: ", multiply(num1, num2))

    elif choice == '4':
        print("Result: ", divide(num1, num2))

    elif choice == '5':
        print("Result: ", square_root(num1))

    elif choice == '6':
        print("Result: ", power(num1, num2))

    elif choice == '7':
        print("Result: ", sin(num1))

    elif choice == '8':
        print("Result: ", cos(num1))

    elif choice == '9':
        print("Result: ", tan(num1))

    else:
        print("Invalid input. Please try again.")

        
