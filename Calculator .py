import time
import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def add():
    a_1 = float(input("First number?: "))
    a_2 = float(input("Second number?: "))
    print(int(a_1) + int(a_2))
    while True:
        a_3 = input("Press enter for menu, or x to exit program: ")
        if "x" in a_3:
            exit()
        elif not a_3:
            cls()
            menu()


def subtract():
    s_1 = float(input("First number?: "))
    s_2 = float(input("Second number?: "))
    print(int(s_1) - int(s_2))
    while True:
        s_3 = input("Press enter for menu, or x to exit program: ")
        if "x" in s_3:
            exit()
        elif not s_3:
            cls()
            menu()


def multiply():
    m_1 = float(input("First number?: "))
    m_2 = float(input("Second number?: "))
    print(int(m_1) * int(m_2))
    while True:
        m_3 = input("Press enter for menu, or x to exit program: ")
        if "x" in m_3:
            exit()
        elif not m_3:
            cls()
            menu()


def divide():
    d_1 = float(input("First number?: "))
    d_2 = float(input("Second number?: "))
    print(int(d_1) / int(d_2))
    while True:
        d_3 = input("Press enter for menu, or x to exit program: ")
        if "x" in d_3:
            exit()
        elif not d_3:
            cls()
            menu()


def menu():
    while True:
        print("Options")
        print("Enter 'add' to add two numbers")
        print("Enter 'subtract' to subtract two numbers")
        print("Enter 'multiply' to multiply two numbers")
        print("Enter 'divide' to divide two numbers")
        print("Enter 'quit' to quit the program")
        user_input = input(": ")
        if user_input == "quit":
            exit()
        elif user_input == "add":
            add()
        elif user_input == "subtract":
            subtract()
        elif user_input == "multiply":
            multiply()
        elif user_input == "divide":
            divide()
        else:
            print("Unknown input")
            time.sleep(2)
            cls()
            menu()


menu()
