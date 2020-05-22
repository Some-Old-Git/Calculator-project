import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def add(x, y):
    return float(x) + float(y)


def subtract(x, y):
    return float(x) - float(y)


def multiply(x, y):
    return float(x) * float(y)


def divide(x, y):
    return float(x) / float(y)


def menu():
    while True:
        print("Which operation do you wish to perform?")
        print("Äddition + '?' \nSubtraction '-' ? \nMultiplication '*' ? \nor Division '/' ?")
        print("Enter 'quit' to quit the program")
        user_input = input(": ")
        if user_input == "quit":
            cls()
            exit()
        else:
            x = float(input("First number?:"))
            y = float(input("Second number?:"))
            if user_input == "add" or "+":
                print(add(x, y))
            elif user_input == "subtract" or "-":
                print(subtract(x, y))
            elif user_input == "multiply" or "*":
                print(multiply(x, y))
            elif user_input == "divide" or "/":
                print(divide(x, y))
            else:
                print("Unknown input")
                cls()
                menu()


menu()
