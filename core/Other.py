# This Module has some Other Commonly used Functions

# Importing Required Modules

import os
import time


# Functions

def About():
    """
    About() -> Prints the About Information on the Terminal

    Parameters -> None
    """
    # Change the path given here to the absolute path of the README file
    with open('C:/Users/Admin/OneDrive/Desktop/Final project/Library/README.md') as file:
        data = file.read()
        print(data)


def ClearScreen():
    """
    ClearScreen() -> Clears the Terminal Screen

    Parameters -> None
    """

    print("Clearing..")
    time.sleep(2)
    os.system("cls")


def Menu(answer="Yes"):
    """
    Menu() -> Displays the Menu

    Parameters -> Answer (User's Choice on Displaying the Menu, by default it is set to True)
    """

    if answer in ["Yes", "Y"]:
        print("  WELCOME TO LIBRARY SYSTEM")
        print("1. Borrow a book")
        print("2. Return a book")
        print("3. Recommend books")
        print("4. Clear Screen")
        print("5. Menu")
        print("6. About")
        print("7. Exit")
    else:
        pass
