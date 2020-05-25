import os
import math
if __name__ == "__main__":
    import doctest
    doctest.testmod()


def cls():
    """
    Check which OS, and clear last screen
    """
    # TODO: Check if this covers all systems
    os.system('cls' if os.name == 'nt' else 'clear')


def get_in(x):
    """
    Obtain, and return, required user input
    """
    try:
        if x == "1":
            x = float(input("Enter number: "))
            return x
        elif x == "2":
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            return x, y
    except Exception as e:
        expt(e.args)


def expt(e):
    """
    Handle exceptions by type
    """
    # print(e)
    print("An error has occurred")
    if 'float division by zero' in e:
        print("Unable to divide by zero")
        cls()
        menu()
    elif 'factorial() argument should not exceed 2147483647' in e:
        print('That number is too large, sorry')
        cls()
        menu()
    elif 'generic' in e:
        print("Please try again")
        cls()
        menu()
    elif 'could not convert string' or "'NoneType' object is not subscriptable" in e:
        print('Incorrect input, please try again')
        cls()
        menu()


def add(x, y):
    """
    Take two numbers, and print the sum
    :param x: 1
    :param y: 2
    :return: 3
    """
    try:
        print(x, '+', y, '=', x + y)
        menu()
    except Exception as e:
        expt(e.args)


def subtract(x, y):
    """
    Take two numbers, and print the difference
    :param x: 2
    :param y: 1
    :return: 1
    """
    try:
        print(x, '-', y, '=', x - y)
        menu()
    except Exception as e:
        expt(e.args)


def multiply(x, y):
    """
    Take two numbers, and print the product
    :param x: 1
    :param y: 2
    :return: 2
    """
    try:
        print(x, 'x', y, '=', x * y)
        menu()
    except Exception as e:
        expt(e.args)


def divide(x, y):
    """
    Take two numbers, and print the quotient
    :param x: 2
    :param y: 2
    :return: 1
    """
    # TODO: Find out if there is a way to work around divide by zero error
    try:
        if x or y == 0:
            print("0")
        print(x, '/', y, '=', x / y)
        menu()
    except Exception as e:
        expt(e.args)


def exponent(x, y):
    """
    Take two numbers, and print exponentiation
    :param x: 2
    :param y: 2
    :return: 4
    """
    try:
        print(x, '^', y, '=', x ** y)
        menu()
    except Exception as e:
        expt(e.args)


def fact(x):
    """
    Take one number, and print the factorial
    :param x: 2
    :return: 2
    """
    try:
        print(x, "factorial =", math.factorial(x))
        menu()
    except ValueError:
        print("Must be a positive whole number")
        fact(get_in("1"))
    except Exception as e:
        expt(e.args)


def menu():
    while True:
        """
        Obtain user operation selection
        """
        # TODO: Learn how to turn this in to a GUI
        print("\nWhich operation do you wish to perform?")
        print("1. Addition '+'? \n2. Subtraction '-'? \n3. Multiplication '*'? \n4. Division '/'?")
        print("5. Exponentiation '^'? \n6. Factorial '!'? ")
        print("Enter 'quit' to quit the program")
        user_input = input(":  ")
        ui_low = user_input.lower()
        if ui_low in ['quit', 'q', 'exit']:
            """
            Quit program at user selection
            """
            cls()
            print("You've tried the best, now try the rest")
            break
        else:
            """
            Obtain user input and, call selected function/operation, and output return
            """
            # TODO: Add more operations
            """
            Call for user input, and relevant operation
            """
            try:
                if ui_low in ['addition', '+', 'add', '1']:
                    n = get_in("2")
                    add(n[0], n[1])
                elif ui_low in ['subtraction', '-', 'subtract', '2']:
                    n = get_in("2")
                    subtract(n[0], n[1])
                elif ui_low in ['multiplication', '*', 'multiply', '3', 'x']:
                    n = get_in("2")
                    multiply(n[0], n[1])
                elif ui_low in ['division', '/', 'divide', '4']:
                    n = get_in("2")
                    divide(n[0], n[1])
                elif ui_low in ['exponents', '^', 'power', '5']:
                    n = get_in("2")
                    exponent(n[0], n[1])
                elif ui_low in ['fact', '!', 'factorial', '6']:
                    n = get_in("1")
                    fact(n)
                else:
                    e = 'generic'
                    expt(e)
            except Exception as e:
                expt(e.args)


menu()
