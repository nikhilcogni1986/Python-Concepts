import os

from Projects.Calculator.art import logo


def add(first_number, second_number):
    return first_number + second_number


def sub(first_number, second_number):
    return first_number - second_number


def multiply(first_number, second_number):
    return first_number * second_number


def divide(first_number, second_number):
    return first_number / second_number


def calculator():
    print(logo)
    first_number = float(input("First Number?: "))
    while True:
        operation = input("+\n-\n*\n/\nOperation: ")
        second_number = float(input(f"{first_number} {operation} "))

        operations = {
            "+": add(first_number, second_number),
            "-": sub(first_number, second_number),
            "*": multiply(first_number, second_number),
            "/": divide(first_number, second_number)
        }
        print(f"{first_number} {operation} {second_number} = {operations[operation]}")
        first_number = operations[operation]
        print()
        if input(f"Type 'y' to continue with {first_number} or 'n' to start new calculation: ").lower() == "n":
            print()
            os.system("cls")
            calculator()


calculator()
