import main_menu
import sql_query
import main_menu
from main_menu import * 


def add_account(user_name, user_surname, user_email):
    for result in account_search(sql_query.account_find_sql, user_email):
        if result['user_email'] is not None:
            print("This e-mail is in used.")
            return main()
    mysql_insert("INSERT INTO accounts (user_name, user_surname, user_email) VALUES (%s, %s, %s)",(user_name, user_surname, user_email))
    print("Account Created Successfully.")
    return main()

def account_search(sql, search):
    for result in mysql_select(sql, ('%'+search+'%','%'+search+'%','%'+search+'%')):
        yield result

def account_search_id(sql, search):
    for result in mysql_select(sql, (search, )):
        yield result



def main():
    print("SELECT AN OPERATION TO CONTINUE: ")
    print("\t1 : Search User/Account")
    print("\t2 : Add an User/Account")
    print("\t3 : Return to Main Menu")
    print("\te : Exit")

    choose = get_a_string("Choose: ", "Wrong Input! Choose Again: ")

    if choose == "1":
        search = get_a_string("Search: ", "Wrong Input! Search Again: ")
        if search == "0":
            main()
        print("{:<3} | {:<50} | {:<50} | {:<50}".format('ID', 'Name', 'Surname', 'e-mail'))
        for result in account_search(sql_query.account_find_sql, search):
            print("{:<3} | {:<50} | {:<50} | {:<50}".format(result['id'],result['user_name'],result['user_surname'],result['user_email']))
        main()

    elif choose == "2":
        print("Enter 0 for cancel.")
        name = get_a_string("Name: ", "Wrong Input! Name: ")
        if name == "0":
            main()
        surname = get_a_string("Surname: ", "Wrong Input! Surname: ")
        if surname == "0":
            main()
        email = email_check("Email: ", "Wrong Input! Please use a correct Email: ")
        if email == "0":
            main()
        add_account(name, surname, email)

    elif choose == "3":
        clear()
        main_menu.main()

    elif choose == "e":
        print("CLOSED SUCCESSFULLY!")
        exit()

    else:
        clear()
        main()


if __name__ == "__main__":
    main()
