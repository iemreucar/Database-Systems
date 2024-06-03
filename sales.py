import accounts
import sql_query
import main_menu
from main_menu import *         

def sale_article(article_id, email):
    print("Article Infos:")
    print("{:<3} | {:<100} | {:<4} | {:<100} | {:<20}".format('ID', 'Title', 'Year', 'Author', 'Journal'))
    for result in mysql_select(sql_query.article_find_id_sql, (article_id,)):
        print("{:<3} | {:<100} | {:<4} | {:<100} | {:<20}".format(result['id'], result['title'][:100], result['year'], result['author'][:100], result['journal'][:20]))
    print("Account Infos:")
    print("{:<3} | {:<50} | {:<50} | {:<50}".format('ID', 'Name', 'Surname', 'Email'))

    for result in accounts.account_search_id(sql_query.email_find_id_sql, email):
        print("{:<4} | {:<50} | {:<50} | {:<50}".format(result['id'], result['user_name'], result['user_surname'],result['user_email']))
    mysql_insert(sql_query.sale_article_sql, (result['id'], article_id))
    return main()

def search_sale_by_account(search, sql):
    for result in mysql_select(sql, (search,)):
        yield result

def search_sale_by_id(search, sql):
    for result in mysql_select(sql, (search,)):
        yield result

def search_account_by_title(search):
    for result in mysql_select(sql_query.article_sold_find_by_title_sql('%'+search+'%','%'+search+'%','%'+search+'%')):
        yield result



def main():
    print("SELECT AN OPERATION TO CONTINUE: ")
    print("\t1 : Search a sale by its customer e-mail")
    print("\t2 : Sale an article")
    print("\t3 : Return main")
    print("\te : Exit")

    choose = get_a_string("Choose: ", "Wrong Input! Choose: ")

    if choose == "1":
        email = email_check("e-mail: ", "Wrong Input! e-mail: ")
        print("{:<3} | {:<100} | {:<4} | {:<100} | {:<20} | {:<5} ".format('ID','Title','Year','Author','Journal','Date of Sale'))
        for i in search_sale_by_account(email, sql_query.article_sold_find_by_email_sql):
            for result in search_sale_by_id(i['id'], sql_query.sale_find_by_id_sql):                                                                                                        
                print("{:<3} | {:<100} | {:<4} | {:<100} | {:<20} | {:<50} ".format(result['id'], result['title'][:100],result['year'],
                                                                          result['author'][:100],result['journal'][:20],str(result['sale_date'])[:50]))
        main()

    elif choose == "2":
        print("Enter 0 to return main menu.")
        article_id = get_a_string("Article ID: ", "Wrong Input! Article ID: ")
        if article_id == "0":
            main()
        if len(list(mysql_select(sql_query.article_find_id_sql, (article_id,)))) == 0:
            print("No articles have been found.")
            return main()
        email_in = get_a_string("Account email: ", "Wrong Input! Account email: ")
        if email_in == "0":
            main()
        if len(list(mysql_select(sql_query.email_find_id_sql, (email_in,)))) == 0:
            print("No accounts have been found.")
            return main()
        sale_article(article_id, email_in)

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
