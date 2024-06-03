import re
from os import system, name
import mysql.connector
from mysql.connector import Error

def mysql_connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', database='bte513b_article_sale_website', user='root',password='')
        if conn.is_connected():
            return conn
    except Error as e:
        print(e)

def mysql_select(sql, val):
    mydb = mysql_connect()
    mycursor = mydb.cursor(dictionary=True)
    try:
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        for x in myresult:
            yield x
    except Error as e:
        mydb.rollback()
        print(e)
        return e
    
def mysql_insert(sql, val):
    mydb = mysql_connect()
    mycursor = mydb.cursor()
    try:
        mycursor.execute(sql, val)
        mydb.commit()
    except Error as e:
        mydb.rollback()
        print(e)
        return e
    

def get_a_string(message, error):
    i = input(message)
    while len(i.strip()) == 0:
        i = input(error)
    return i

def get_an_integer(message, error):
    msg = message
    while True:
        try:
            i = int(input(msg))
            break
        except ValueError:
            msg = error
    return i

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def email_check(message, error):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    i = input(message)
    while True:
        if re.search(regex, i):
            return i
        else:
            i = input(error)        

import accounts
import articles_and_authors
import sales
def main():

    clear()
    print("ARTICLE AND SALES CONTROL CENTER")
    print("SELECT AN OPERATION TO CONTINUE: ")
    print("\t1 : Account Options")
    print("\t2 : Article Options")
    print("\t3 : Sale Options")
    print("\te : EXIT")

    user_input = get_a_string("Choose: ", "PLEASE SELECT A PROPER OPERATION! CHOOSE: ")

    if user_input == "1":
        clear()
        accounts.main()

    elif user_input == "2":
        clear()
        articles_and_authors.main()

    elif user_input == "3":
        clear()
        sales.main()

    elif user_input == "e":
        print("CLOSED SUCCESSFULLY!")
        exit()

    else:
        clear()
        main()
        
        
if __name__ == "__main__":
    main()


