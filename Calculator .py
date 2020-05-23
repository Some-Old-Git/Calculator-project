import os


def cls():
    # TODO: Check if this covers all systems
    os.system('cls' if os.name == 'nt' else 'clear')


def error(x):
    # Handle input and computation errors by type
    # TODO: Find out if there is a way to compress this
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
    elif x == 'debug':
        print('Failure to pass test \n Run debug')
        cls()
        exit()
    else:
        cls()
        menu()


def debug():
    # Test functions to ensure working correctly
    try:
        print('Testing addition')
        assert add(1, 2) == 3
        print('Testing subtraction')
        assert subtract(2, 1) == 1
        print('Testing multiplication')
        assert multiply(2, 2) == 4
        print('Testing division')
        assert divide(2, 1) == 2
        print('Testing exponentiation')
        assert exponent(2, 2) == 4
        print('Tests passed')
        menu()
    except AssertionError:
        error('debug')


def add(x, y):
    # Return the sum of the two inputs
    # Output any relevant error by type
    try:
        assert x + y >= x
        return x + y
    except (ValueError, TypeError):
        error('generic')
    except OverflowError:
        error('over')
    except AssertionError:
        error('debug')


def subtract(x, y):
    # Return the difference between the two inputs
    # Output any relevant error by type
    try:
        assert x - y <= x
        return x - y
    except (ValueError, TypeError):
        error('gen')
    except OverflowError:
        error('over')
    except AssertionError:
        error('debug')


def multiply(x, y):
    # Return the product of the two inputs
    # Output any relevant error by type
    try:
        assert x * y >= x
        return x * y
    except (ValueError, TypeError):
        error('generic')
    except OverflowError:
        error('over')
    except AssertionError:
        error('debug')


def divide(x, y):
    # Return the quotient of the two inputs
    # Output any relevant error by type
    # TODO: Find out if there is a way to remove divide by zero error
    try:
        assert x / y <= x
        return x / y
    except ZeroDivisionError:
        error('zero')
    except (ValueError, TypeError):
        error('generic')
    except OverflowError:
        error('over')
    except AssertionError:
        error('debug')


def exponent(x, y):
    # Return the exponent of the two inputs
    # Output any relevant error by type
    try:
        assert x ** y >= x
        return x ** y
    except (ValueError, TypeError):
        error('generic')
    except OverflowError:
        error('over')
    except AssertionError:
        error('debug')


def menu():
    while True:
        # Obtain user operation selection
        # TODO: Learn how to turn this in to a GUI
        print("Which operation do you wish to perform?")
        print("1. Addition '+'? \n2. Subtraction '-'? \n3. Multiplication '*'? \n4. Division '/'?")
        print("5. Exponentiation '^'?")
        print("Enter 'quit' to quit the program")
        user_input = input(":  ")
        ui_low = user_input.lower()
        if 'quit' in ui_low:
            # Quit program
            cls()
            break
        elif 'debug' in ui_low:
            debug()
        else:
            # Obtain user input to then perform desired operation and output
            # TODO: Add more operations
            try:
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
                elif ui_low in ['exponents', '^', 'power', '5']:
                    print(x, '^', y, '=', exponent(x, y))
                else:
                    error('generic')
            except ValueError:
                print("Sorry, I didn't learn algebra in school, please enter numbers only")
                menu()


menu()