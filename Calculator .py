import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def error(x):
    # Handle input and computation errors by type
    print("An error has occurred")
    if x == 'zero':
        print("Unable to divide by zero")
        cls()
        menu()
    elif x == 'over':
        print("Number too large")
        cls()
        menu()
    elif x == 'generic':
        print("Please try again")
        cls()
        menu()
    else:
        cls()
        menu()


def add(x, y):
    # Return the sum of the two inputs
    # Output any relevant error by type
    try:
        return x + y
    except (ValueError, TypeError):
        error('generic')
    except OverflowError:
        error('over')


def subtract(x, y):
    # Return the difference between the two inputs
    # Output any relevant error by type
    try:
        return x - y
    except (ValueError, TypeError):
        error('gen')
    except OverflowError:
        error('over')


def multiply(x, y):
    # Return the product of the two inputs
    # Output any relevant error by type
    try:
        return x * y
    except (ValueError, TypeError):
        error('generic')
    except OverflowError:
        error('over')


def divide(x, y):
    # Return the quotient of the two inputs
    # Output any relevant error by type
    try:
        return x / y
    except ZeroDivisionError:
        error('zero')
    except (ValueError, TypeError):
        error('generic')
    except OverflowError:
        error('over')


def menu():
    while True:
        # Obtain user operation selection
        print("Which operation do you wish to perform?")
        print("1. Addition '+'? \n2. Subtraction '-'? \n3. Multiplication '*'? \n4. Division '/'?")
        print("Enter 'quit' to quit the program")
        user_input = input(":  ")
        ui_low = user_input.lower()
        if 'quit' in ui_low:
            # Quit program
            cls()
            break
        else:
            # Obtain user input to then perform desired operation and output
            x = float(input("First number?:"))
            y = float(input("Second number?:"))
            if ui_low in ['addition', '+', 'add', '1']:
                print(x, '+', y, '=', add(x, y))
            elif ui_low in ['subtraction', '-', 'subtract', '2']:
                print(x, '-', y, '=', subtract(x, y))
                continue
            elif ui_low in ['multiplication', '*', 'multiply', '3', 'x']:
                print(x, 'x', y, '=', multiply(x, y))
                continue
            elif ui_low in ['division', '/', 'divide', '4']:
                print(x, '/', y, '=', divide(x, y))
                continue
            else:
                error('generic')


menu()
