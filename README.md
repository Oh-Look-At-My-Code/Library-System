Library System

---------
:FOLDERS:
_________

/Assets : Contains the data that is to be inserted in the MySQL tables in csv format
         
         #Files: books.csv -> Contains all the data about the books in the format 
                                     #(Book ID, Title, Authors, Average rating, isbn, isbn13, Language code, Num pages, Rating_count, Text_reviews_count, Pub_date, Publisher)

/core : Contains all the files that are required by the project to work

        #Files: __init__.py -> Makes the folder to be recognized as a module
               #Checks.py -> This file contains the functions that verify the requirements of the Project
               #InsertData.py -> This file contains the functions to insert the data in the MySQL tables
               #User_Functions.py -> This file contains the function that allow a user to perform certain task
               #Other.py -> This file contains some commonly used functions

-------------------
:ROOT FOLDER FILES:
___________________

Main.py -> This is the main file that connects all the other modules and is used to run the project

requirements.txt -> It contains the required packages for this project to work that can be installed via the command
                    `pip3 install -r requirements.txt`


----------
:FEATURES:
__________

Overview: This is a library book management system in which a user can borrow a book, return a book, look for the recommended books.
          MySQL is used as the backend database in this project.

1. Borrow a book: Users can borrow a book
2. Return a book: Users can return a book
3. Recommend books: Users can look for the recommended book
4. Clear Screen: Clears the terminal screen
5. Menu: Shows the menu
6. About: Prints the content of this file to the screen
7. Exit: Exit the program

-------------------
:ENVIRONMENT SETUP:
___________________

1. Clone the Repository to your machine.
2. Create a Virtual Environment using virtualenv or pipenv.
3. `pip3 install -r Requirements.txt` to install the required packages automatically.
4. Make sure the MySQL Service is running and change the "8059LoVe" in the files with the password and the "root" with the username of your local SQL server.
5. `python3 Main.py` to see if the program is running correctly and is able to connect to MySQL Server. (Feel free to ask for help if you face any error)

### NOTE: Step 2 is optional but highly recommended to avoid conflicting packages.
### NOTE: After Cloning the Repo rename the README.md to README.txt in order for the About() Function in /core/Other.py to work.
