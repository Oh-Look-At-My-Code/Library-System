# This Module has the Functions that allow a User to do Certain Task's

# Importing Required Modules

import mysql.connector
import os
import datetime
import time
from mysql.connector import DataError
import random

# Functions

def RecommendBook():
    """
    RecommendBook() -> Recommend books base on average rating, trending, authors, title, and randomization.

    Parameters -> None
    """

    mn = mysql.connector.connect(host="localhost", user="root",
                                 password="8059LoVe", database="library")
    cur = mn.cursor()

    print('Welcome to the book recommendation menu.')
    print('Please choosing a type of recommendation')
    print('1. Recommend books base on score.')
    print('2. Recommend books base on trending.')
    print('3. Recommend books base on authors.')
    print('4. Recommend books base on title of the book.')
    print('5. Randomly recommend books .')
    
    while True:
        try:
            choice = int(input('Your type of recommendation : '))
        except ValueError:
            print('To describe your type of recommendation, your input must be a number which is appeared in the menu.')
        else:
            if choice < 1 or choice > 5:
                print('Your input is an invalid number. Be reminded that your input must be a number which is appeared in the menu.')
            else:
                break
    
    if choice == 1:
        print('Your recommended books are : ')
        print('(Book ID, Title, Authors, Score)')
        cur.execute('select book_info.Book_ID,book_info.Title,Authors,Average_rating from book_info left join book_reserv on book_reserv.Book_ID = book_info.Book_ID where book_reserv.Booking_ID is null and Rating_count > 100 order by Average_rating desc limit 20')
        result = cur.fetchall()
        for i in result:
            print(i)
        print('Hope you enjoy your books.')
    elif choice == 2:
        print('Your recommended books are : ')
        print('(Book ID, Title, Authors, Score)')
        cur.execute('select book_info.Book_ID,book_info.Title,Authors,Average_rating from book_info left join book_reserv on book_reserv.Book_ID = book_info.Book_ID where book_reserv.Booking_ID is null order by Rating_count desc limit 20')
        result = cur.fetchall()
        for i in result:
            print(i)
        print('Hope you enjoy your books.')
    elif choice == 3:
        name = input('Enter your authors name : ')
        print('(Book ID, Title, Authors, Score)')
        cur.execute('select book_info.Book_ID,book_info.Title,Authors,Average_rating from book_info left join book_reserv on book_reserv.Book_ID = book_info.Book_ID where book_reserv.Booking_ID is null and Authors like ("%{}%") order by Average_rating desc limit 20'.format(name))
        result = cur.fetchall()
        for i in result:
            print(i)
        print('Hope you enjoy your books.')
    elif choice == 4:
        name = input('Enter your book name : ')
        print('(Book ID, Title, Score)')
        cur.execute('select book_info.Book_ID,book_info.Title,Average_rating from book_info left join book_reserv on book_reserv.Book_ID = book_info.Book_ID where book_reserv.Booking_ID is null and book_info.Title like ("%{}%") order by Average_rating desc limit 20'.format(name))
        result = cur.fetchall()
        for i in result:
            print(i)
        print('Hope you enjoy your books.')
    elif choice == 5:
        print('Your recommended books are : ')
        print('(Book ID, Title, Authors, Score)')
        cur.execute('select book_info.Book_ID,book_info.Title,book_info.Authors,Average_rating from book_info left join book_reserv on book_reserv.Book_ID = book_info.Book_ID where book_reserv.Booking_ID is null order by rand() desc limit 20')
        result = cur.fetchall()
        for i in result:
            print(i)
        print('Hope you enjoy your books.')
    mn.commit()
    cur.close()
    mn.close()


def BorrowBook():
    """
    BorrowBook() -> Let's a User Borrow a Book

    Parameters -> None
    """

    mn = mysql.connector.connect(host="localhost", user="root",
                                 password="8059LoVe", database="library")
    cur = mn.cursor()
    
    while True:
        try:
            book_id = str(input("Book ID: "))
            cur.execute('SELECT * FROM book_info where Book_ID="{}"'.format(book_id))
            result = cur.fetchall()
            if len(result) == 0:
                print('No books found or invalid book ID.')
                continue
            else:
                title = result[0]
                title = title[1]
            cur.execute('SELECT * FROM book_reserv where Book_ID="{}"'.format(book_id))
            result = cur.fetchall()
            if len(result) != 0:
                print('This book is being borrowed.')
                continue
            else:
                break
        except ValueError:
            print("Please Enter a Valid Book Number!")
            continue
        else:
            break
            
    while True:
        Name = input("Enter your User Name: ")
        if len(Name) == 0:
            print("Please Enter a Name!")
        elif len(Name) > 30:
            print("Name too Long!")
        else:
            break
            
    while True:
        try:
            Mobile = input("Enter your Mobile Number: ")
            for i in Mobile:
                if i in ['1','2','3','4','5','6','7','8','9','0']:
                    logic = 1
                else:
                    logic =0
        except ValueError:
            print("Please Enter a Valid Mobile Number!")
            continue
        else:
            if len(str(Mobile)) == 10 and Mobile != '0000000000' and logic != 0:
                break
            elif len(str(Mobile)) > 10 or len(str(Mobile)) < 10 and logic != 0:
                print("Please Enter a Valid 10 Digit Mobile Number!")
            else:
                print("Please Enter a Valid Phone Number!")
                
    while True:
        try:
            card_id = input("Enter you ID Card Number: ")
            for i in card_id:
                if i in ['1','2','3','4','5','6','7','8','9','0']:
                    logic = 1
                else:
                    logic = 0
        except ValueError:
            print("Please Enter a Valid ID Card Number!")
            continue
        else:
            if len(card_id) == 13 and card_id != 0000000000000 and logic == 1:
                break
            elif len(card_id) > 13 or len(card_id) < 13 and logic == 1:
                print("Please Enter a Valid 13 ID Card Number!")
            else:
                print("Please Enter a Valid ID Card Number!")
                
    Time_of_Booking = datetime.datetime.now()
    date = Time_of_Booking.date()
    date = date.strftime("%d-%m-%y")
    
    booking_id = random.randint(1, 10000)
    cur.execute("SELECT Booking_ID FROM book_reserv")
    result = cur.fetchall()
    Used_ID = []
    for x in result:
        for y in x:
            Used_ID.append(y)
    while True:
        if booking_id in Used_ID:
            booking_id = random.randint(1, 10000)
        else:
            break
    
    while True:
        print('The book you want to borrow is '+title+'.')
        ask = input("Are you Sure you want to borrow(Y/N): ")
        if ask in ["Y", "y"]:
            print("Booking...")
            try:
                query = "INSERT INTO book_reserv values('{}', '{}', '{}', '{}', '{}', '{}', {})".format(
                    book_id, title, Name, Mobile, card_id, date, booking_id)
                cur.execute(query)
            except DataError:
                print("Error in Booking!")
            else:
                print("Successfully Booked!")
                mn.commit()
                cur.close()
                mn.close()
                break
        elif ask in ["N", "n"]:
            print("Stopping Booking...")
            time.sleep(0.5)
            os.system("cls")
            break
        else:
            print("Please Enter Y (Yes) or N (No)!")


def ReturnBook():
    """
    ReturnBook() -> Allows a User to return a book.

    Parameters -> None
    """

    mn = mysql.connector.connect(host="localhost", user="root",
                                 password="8059LoVe", database="library")
    cur = mn.cursor()
    
    while True:
        Name = input("Enter your User Name: ")
        if len(Name) == 0:
            print("Please Enter a Name!")
        elif len(Name) > 30:
            print("Name too Long!")
        else:
            break
            
    while True:
        try:
            card_id = input("Enter you ID Card Number: ")
            for i in card_id:
                if i in ['1','2','3','4','5','6','7','8','9','0']:
                    logic = 1
                else:
                    logic = 0
                    break
        except ValueError:
            print("Please Enter a Valid ID Card Number!")
            continue
        else:
            if len(card_id) == 13 and card_id != '0000000000000' and logic == 1:
                break
            elif len(card_id) > 13 or len(card_id) < 13 and logic == 1:
                print("Please Enter a Valid 13 ID Card Number!")
            else:
                print("Please Enter a Valid ID Card Number!")
                
    cur.execute('SELECT Book_ID, Title, Booking_ID FROM book_reserv WHERE User_Name = "{}" and ID_card_No = "{}"'.format(Name,card_id))
    result = cur.fetchall()
    if len(result) == 0:
        print('You are not borrowing any book, or the given User Name or ID Card Number is incorrect.')
        return
    else:
        print('You are borrowing '+str(len(result))+' book(s).')
        print('(Book_ID, Title, Booking_ID)')
        for i in result:
            print(i)
    while True:
        try:
            return_book = int(input('Booking ID of the book you want to return : '))
        except ValueError:
            print('Please Enter a Valid Booking ID.')
            continue
        else:
            cur.execute('SELECT * FROM book_reserv WHERE Booking_ID = {}'.format(return_book))
            result = cur.fetchall()
            if len(result) == 0:
                print('Invalid Booking ID')
            else:
                break
    result1 = result[0]
    info = result1[5].split('-')
    day1, month1, year1 = [int(info[0]),int(info[1]),int(info[2])+2000]
    date1 = datetime.date(year1,month1,day1)
    while True:
        try:
            date_component = input('Please Enter a Returning Date(DD-MM-YYYY) : ').split('-')
            day2, month2, year2 = [int(i) for i in date_component]
            date2 = datetime.date(year2,month2,day2)
        except ValueError:
            print('Please Enter the Date in this Form : DD-MM-YYYY')
            continue
        else:
            if date2<date1:
                print('Please Enter a Valid Returning Date.')
            else:
                print('The book named '+ result1[1] + '\nBooking ID : '+ str(result1[6]) + '\nhas been successfully returned.')
                date_dif = date2-date1
                date_dif = date_dif.days
                if date_dif > 7:
                    fee = (date_dif-7)*200
                    print('You need to pay for '+str(fee)+' THB for our service.\nThank you.')
                else:
                    print('Thank you.')
            cur.execute('DELETE FROM book_reserv WHERE Booking_ID = {}'.format(return_book))
            mn.commit()
            cur.close()
            mn.close()
            break