# This Module has the Functions that Verify the Requirements of the Project

# Importing Required Modules

import mysql.connector as con
from mysql.connector.errors import ProgrammingError, Error
import core.InsertData as Insert

# Functions


def CheckDatabase():
    """
    CheckDatabase() -> Checks if the Database required Exists or not

    Parameters -> None
    """

    print("Checking Database Requirements..")

    db = con.connect(host="localhost", user="root",
                     database="", password="8059LoVe")
    cur = db.cursor()
    result = None

    try:
        cur.execute("use library;")
    except ProgrammingError:
        print("Database does not Exist!")
        result = False
    else:
        result = True

    if result is True:
        print("Database exists!")
    else:
        print("Creating Database with the Required Tables..")
        print("Please be Patient!")
        cur.execute("create database library;")
        cur.execute("use library;")
        CreateTables()
        print("Database and Tables Created!")

    cur.close()
    db.close()


def CreateTables():
    """
    CreateTables() -> Creates all the Required Tables

    Parameters -> None
    """

    db = con.connect(host="localhost", user="root",
                     database="library", password="8059LoVe")
    cur = db.cursor()

    cur.execute(
        "create table book_info (Book_ID varchar(10) NOT NULL, Title varchar(300) NOT NULL, Authors varchar(1000) NOT NULL, Average_rating varchar(4) NOT NULL, isbn varchar(10) NOT NULL, isbn13 varchar(13) NOT NULL, Language_code varchar(10) NOT NULL, Num_pages varchar(5) NOT NULL, Rating_count varchar(10) NOT NULL, Text_reviews_count varchar(10) NOT NULL, Pub_date varchar(10) NOT NULL, Publisher varchar(300) NOT NULL);")

    cur.execute("create table book_reserv (Book_ID varchar(10) NOT NULL, Title varchar(100) NOT NULL, User_Name varchar(50) NOT NULL, Mobile_No varchar(10) NOT NULL, ID_card_No varchar(13) NOT NULL, Date_Of_Booking varchar(20) NOT NULL, Booking_ID int NOT NULL);")

    Insert.InsertDataBook()

    cur.close()
    db.close()


def CheckConnection():
    """
    CheckConnection() -> Tests the Connection with the Mysql Server

    Parameter -> None
    """

    try:
        print("Checking the Connection to the MySQL Server..")
        connection = con.connect(host='localhost',
                                 database='',
                                 user="root",
                                 password="8059LoVe")
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server Version", db_Info)

    except Error:

        print("Error connecting to MySQL Server, Make sure the MySQL Server is running and then try again!")
        print("Exiting!")
        return False

    else:
        return True
