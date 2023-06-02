# This Module has the Functions to Insert the Data in the MySQL Tables

# Importing Required Modules

import csv
import mysql.connector as con

# Functions


def InsertDataBook():
    """
    InsertDataBook() -> Inserts all the Book details in the book_info Table

    Parameters -> None
    """

    mn = con.connect(host="localhost",
                     user="root",
                     password="8059LoVe",
                     database="library")

    cur = mn.cursor()

    # Iterating through all the values and insert's them in the table
    # Replace the path below with the absolute path of the file on your computer
    try:
        with open("C:/Users/Admin/OneDrive/Desktop/Final project/Library/Assets/books.csv", errors="ignore") as csv_data:
            csv_reader = csv.reader(csv_data, delimiter=",")
            for row in csv_reader:
                row = row[0:12]
                cur.execute(
                    'INSERT INTO book_info VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', row)
    except FileNotFoundError:
        print("Please check whether the file is in the Assets Folder or not and try changing the Location in InsertData.py")
    finally:
        mn.commit()  # Important: Committing the Changes
        cur.close()
        mn.close()
