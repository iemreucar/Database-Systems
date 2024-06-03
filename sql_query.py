search_unique_article= """
SELECT article_title,
       journal_id
FROM articles
WHERE article_title=%s
"""

author_insert_sql = """
INSERT INTO authors (author_name, author_surname)
SELECT %s, %s 
FROM DUAL
WHERE NOT EXISTS
    (SELECT author_name, author_surname
     FROM authors
     WHERE author_name=(%s) and author_surname = (%s) )
LIMIT 1                      
"""

journal_insert_sql = """
INSERT INTO journals (journal_name)
SELECT *
FROM
  (SELECT (%s)) AS tmp
WHERE NOT EXISTS
    (SELECT journal_name
     FROM journals
     WHERE journal_name = (%s) )
LIMIT 1 
"""

article_sold_find_by_email_sql = """
SELECT sales.id AS id,
       accounts.user_email AS email,
       sales.sale_date AS sale_date
FROM sales
JOIN accounts ON sales.user_id = accounts.id
WHERE accounts.user_email = %s
"""

article_sold_find_by_title_sql = """
SELECT articles.id AS id,
       articles.title AS title,
       articles.year AS year,
       GROUP_CONCAT(CONCAT(authors.author_name,' ',authors.author_surname) ORDER BY author_order.author_order) AS author,
       journals.journal_name AS journal,
       sales.id AS sale_id,
       accounts.user_email AS member,
       sales.sale_date AS sale_date,
FROM sales
JOIN articles ON articles.id = sales.article_id
JOIN author_order ON articles.id = author_order.article_id
JOIN authors ON authors.id = author_order.authorId
JOIN journals ON articles.journal_id = journals.id
JOIN accounts ON sales.user_id = accounts.id
GROUP BY articles.title
HAVING title LIKE %s OR author LIKE %s OR publisher LIKE %s
ORDER BY articles.id
"""


sale_find_by_id_sql = """
SELECT articles.id AS id,
       articles.article_title AS title,
       articles.article_year AS year,
       GROUP_CONCAT(CONCAT(authors.author_name,' ',authors.author_surname) ORDER BY author_order.author_order) AS author,
       journals.journal_name AS journal,
       sales.sale_date AS sale_date
FROM articles
JOIN author_order ON articles.id = author_order.article_id
JOIN authors ON author_order.author_id = authors.id
JOIN journals ON journals.id = articles.journal_id
LEFT JOIN sales ON sales.article_id = articles.id
WHERE sales.id = %s
"""

sale_article_sql = """
INSERT INTO sales(
    user_id,
    article_id,
    sale_date
)
VALUES(%s, %s, NOW())
"""

account_find_sql = """
SELECT id,
       user_name,
       user_surname,
       user_email
FROM accounts
WHERE user_name LIKE %s
  OR user_surname LIKE %s
  OR user_email LIKE %s
"""

email_find_id_sql = """
SELECT id,
       user_name,
       user_surname,
       user_email
FROM accounts
WHERE user_email = %s
"""

article_find_sql = """
SELECT articles.id AS id,
       articles.article_title AS title,
       articles.article_year AS year,
       GROUP_CONCAT(CONCAT(authors.author_name,' ',authors.author_surname) ORDER BY author_order.author_order) AS author,
       journals.journal_name AS journal
FROM articles
JOIN author_order ON articles.id = author_order.article_id
JOIN authors ON author_order.author_id = authors.id
JOIN journals ON journals.id = articles.journal_id
GROUP BY title
HAVING title LIKE %s OR author LIKE %s OR journal LIKE %s
ORDER BY articles.id
"""

article_sold_find_sql = """
SELECT article_id 
FROM articles
LEFT JOIN sales ON sales.article_id = articles.id
WHERE articles.id = %s
"""

article_find_id_sql = """
SELECT articles.id AS id,
       articles.article_title AS title,
       articles.article_year AS year,
       GROUP_CONCAT(CONCAT(authors.author_name,' ',authors.author_surname) ORDER BY author_order.author_order) AS author,
       journals.journal_name AS journal
FROM articles
JOIN author_order ON articles.id = author_order.article_id
JOIN authors ON author_order.author_id = authors.id
JOIN journals ON journals.id = articles.journal_id
GROUP BY title
HAVING articles.id = %s
ORDER BY articles.id
"""