import accounts
import sql_query
import main_menu
from main_menu import *

def unique_search(sql, search):
    for unique in mysql_select(sql, search,):
        yield unique                   

def add_article(article_title, article_year, author_name_list,author_surname_list, journal):
    author_id_list = []
    article_id = ""
    journal_id=""
    for unique in unique_search(sql_query.search_unique_article, (article_title,)):
        if unique['article_title'] is not None:
            print("This article has been published by another journal.")
            return main()
    for author_name, author_surname in list(zip(author_name_list, author_surname_list)):
        mysql_insert(sql_query.author_insert_sql, (author_name, author_surname,author_name, author_surname))
        for i in mysql_select("SELECT id FROM authors WHERE author_name = %s and author_surname= %s", (author_name,author_surname)):
            author_id_list.append(i['id'])           
    mysql_insert(sql_query.journal_insert_sql, (journal, journal))
    for i in mysql_select("SELECT id FROM journals WHERE journal_name = %s", (journal,)):
        journal_id = i['id']

    mysql_insert("INSERT INTO articles (article_title, article_year,  journal_id) VALUES (%s, %s, %s)",(article_title, article_year, journal_id))
        if list(unique_search(sql_query.search_unique_article, (article_title,))):
            print("alread created")
    for i in mysql_select("SELECT id FROM articles WHERE article_title = %s", (article_title,)):
        article_id = i['id']
    for author_id in author_id_list:
        mysql_insert("INSERT INTO author_order (article_id, author_id, author_order) VALUES (%s, %s, %s)",(article_id, author_id, author_id_list.index(author_id)+1))
    print("Article has created successfully.")
    return main()

def article_search(search):
    if len(list(mysql_select(sql_query.article_find_sql,('%'+search+'%','%'+search+'%','%'+search+'%')))) == 0:
        print("No articles have been found.")
        return
    for result in mysql_select(sql_query.article_find_sql,('%'+search+'%','%'+search+'%','%'+ search+'%')):
        yield result



def main():
    from main_menu import get_a_string
    print("SELECT AN OPERATION TO CONTINUE: ")
    print("\t1 : Search an article by its title or author or journal")
    print("\t2 : Add an article")
    print("\t3 : Return to Main Menu")
    print("\te : Exit")

    choose = get_a_string("Choose: ", "Wrong Input! Choose: ")

    if choose == "1":
        search = get_a_string("Search: ", "Search: ")
        print("{:<3} | {:<100} | {:<4} | {:<100} | {:<50} ".format('ID', 'Title', 'Year', 'Author Name/Surname', 'Journal'))
        for result in article_search(search):
            print("{:<3} | {:<100} | {:<4} | {:<100} | {:<50} ".format(result['id'], result['title'][:50], result['year'],
                                                                        result['author'][:50],result['journal'][:20]))
        main()
    elif choose == "2":
        print("Enter 0 to return main menu.")
        title = get_a_string("Article Title: ", "Wrong Input! Article Title: ")
        if title == "0":
            main()
        year = get_an_integer("Article Year: ", "Wrong Input! Article Year: ")
        if str(year) == "0":
            main()
        orders_done=False
        author_name_list=[]
        author_surname_list=[]
        print("Enter Authors in order")
        while not orders_done:
            author_name_list.append(get_a_string("Author Name: ","Wrong Input! Author name: "))
            if author_name_list == "0":
                main()
            author_surname_list.append(get_a_string("Author Surname: ","Wrong Input! Author surname: " ))
            if author_surname_list == "0":
                main()
            d=input("All authors are written?y/n")
            if d=="y":
                orders_done=True
            elif d=="n":
                orders_done=False
        journal = get_a_string("Journal Name: ", "Wrong Input! Journal Name: ")
        if journal == "0":
            main()
        add_article(title, year,author_name_list,author_surname_list, journal)

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
