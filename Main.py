9# This is the Main File that loads all the Other Modules

# Importing Required Modules

import core.User_Functions as User
import core.Other as Other
import core.Checks as Check
from time import sleep

# Initial Checks

# Checking the Connection to the MySQL Server
connection_status = Check.CheckConnection()
if connection_status is False:
    quit()
else:
    Check.CheckDatabase()  # Checking for the Requirements of the Project

#Other.ClearScreen()  # Clear the Terminal Window

# Final Imports

# Ask for the Input and Process it

Other.Menu()

while True:
    ans = input("Choose an Option Number: ")
    if ans == "1":
        User.BorrowBook()
    elif ans == "2":
        User.ReturnBook()
    elif ans == "3":
        User.RecommendBook()
    elif ans == "4":
        Other.ClearScreen()
        Other.Menu()
    elif ans == "5":
        Other.Menu()
    elif ans == "6":
        Other.ClearScreen()
        Other.About()
        while True:
            ask = input("Do you want to Display Menu(Y/N): ")
            if ask in ["Y", "y"]:
                Other.Menu()
                break
            elif ask in ["N", "n"]:
                break
            else:
                print("Please Enter either Y (Yes) or N (No)!")
    elif ans == "7":
        print("Closing all Connections..")
        sleep(0.5)
        print("Thank You!")
        quit()
    else:
        print("Please Enter a Valid Option Number!")
