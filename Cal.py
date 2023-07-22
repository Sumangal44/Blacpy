import sys
from termcolor import colored

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b

def get_operator():
    while True:
        operator = input("Enter the operation (+, -, *, /): ")
        if operator in ('+', '-', '*', '/'):
            return operator
        print(colored("Invalid operator! Please enter a valid operator.", "red"))

def get_numbers():
    while True:
        try:
            a = float(input("Enter the first number: "))
            b = float(input("Enter the second number: "))
            return a, b
        except ValueError:
            print(colored("Invalid input! Please enter valid numbers.", "red"))

def calculator():
    print(colored("Welcome to the Colorful Calculator!", "blue"))
    while True:
        try:
            a, b = get_numbers()
            operator = get_operator()
            if operator == '+':
                result = add(a, b)
            elif operator == '-':
                result = subtract(a, b)
            elif operator == '*':
                result = multiply(a, b)
            elif operator == '/':
                result = divide(a, b)

            print(colored(f"Result: {result}", "cyan"))
        except Exception as e:
            print(colored(f"Error: {e}", "red"))

        choice = input("Do you want to continue (y/n)?: ")
        if choice.lower() != 'y':
            break

    print(colored("Goodbye! Thanks for using the Colorful Calculator.", "magenta"))

if __name__ == "__main__":
    calculator()
  
