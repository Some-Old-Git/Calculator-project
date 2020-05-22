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
    elif x == 'val' or 'typ':
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
        return float(x) + float(y)
    except ValueError:
        error('val')
    except OverflowError:
        error('over')
    except TypeError:
        error('typ')


def subtract(x, y):
    # Return the difference between the two inputs
    # Output any relevant error by type
    try:
        return float(x)-float(y)
    except ValueError:
        error('val')
    except OverflowError:
        error('over')
    except TypeError:
        error('typ')


def multiply(x, y):
    # Return the product of the two inputs
    # Output any relevant error by type
    try:
        return float(x) * float(y)
    except ValueError:
        error('val')
    except OverflowError:
        error('over')
    except TypeError:
        error('typ')


def divide(x, y):
    # Return the quotient of the two inputs
    # Output any relevant error by type
    try:
        return float(x) / float(y)
    except ZeroDivisionError:
        error('zero')
    except ValueError:
        error('val')
    except OverflowError:
        error('over')
    except TypeError:
        error('typ')


def menu():
    while True:
        # Obtain user operation selection
        print("Which operation do you wish to perform?")
        print("1. Addition '+'? \n2. Subtraction '-'? \n3. Multiplication '*'? \n4. Division '/'?")
        print("Enter 'quit' to quit the program")
        user_input = input(":  ")
        if user_input == 'quit':
            # Quit program
            cls()
            break
        else:
            # Obtain user input to then perform desired operation and output
            x = float(input("First number?:"))
            y = float(input("Second number?:"))
            if user_input == 'addition' or '+' or 'add' or '1':
                print(add(x,y))
            elif user_input == 'subtraction' or '-' or 'subtract' or '2':
                print(subtract(x, y))
                continue
            elif user_input == 'multiplication' or '*' or 'multiply' or '3' or 'x':
                print(multiply(x, y))
                continue
            elif user_input == 'division' or '/' or 'divide' or '4':
                print(divide(x, y))
                continue
            else:
                error('val')


menu()
