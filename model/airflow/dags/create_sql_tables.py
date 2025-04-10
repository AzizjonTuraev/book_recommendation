from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

default_args = {
    "owner": "azizjon",
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}


with DAG(
    dag_id="create_table_if_not_exist",
    default_args=default_args, 
    # start_date=datetime(2025, 3, 21),
    start_date=datetime.today(),
    schedule_interval='@once'
) as dag:

    create_books = SQLExecuteQueryOperator(
        task_id = "create_books_table",
        conn_id  = 'postgres_localhost',
        sql= """
            CREATE TABLE IF NOT EXISTS books (
                ISBN VARCHAR(13) PRIMARY KEY,
                book_title VARCHAR(1000) NOT NULL,
                book_author VARCHAR(255),
                year_of_publication INTEGER,
                publisher VARCHAR(255),
                image_url_s VARCHAR(255),
                image_url_m VARCHAR(255),
                image_url_l VARCHAR(255)
            );
        """
    )

    create_users = SQLExecuteQueryOperator(
        task_id = "create_users_table",
        conn_id  = 'postgres_localhost',
        sql= """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                location VARCHAR(255),
                age INTEGER
            );
        """
    )

    create_ratings = SQLExecuteQueryOperator(
        task_id = "create_ratings_table",
        conn_id  = 'postgres_localhost',
        sql= """
            CREATE TABLE IF NOT EXISTS ratings (
                user_id INTEGER,
                ISBN VARCHAR(20),
                book_rating INTEGER,
                PRIMARY KEY (user_id, ISBN)
        );
        """
    )


    [create_books, create_users] >> create_ratings



# SELECT count(isbn)
# FROM books b 
# WHERE b.book_author = 'Agatha Christie';


# SELECT 
#     r.user_id,
#     COUNT(r.ISBN) AS rating_count
# FROM 
#     ratings r
# GROUP BY 
#     r.user_id
# ORDER BY 
#     rating_count DESC
# LIMIT 10;



# SELECT 
#     b.book_title,
#     b.book_author,
#     CASE
#         WHEN u.age < 20 THEN 'Teens'
#         WHEN u.age < 30 THEN '20s'
#         WHEN u.age < 40 THEN '30s'
#         WHEN u.age < 50 THEN '40s'
#         ELSE '50+'
#     END AS age_group,
#     COUNT(*) AS rating_count,
#     ROUND(AVG(r.book_rating), 2) AS avg_rating
# FROM ratings r
# JOIN books b ON r.ISBN = b.ISBN
# JOIN users u ON r.user_id = u.user_id
# GROUP BY b.book_title, b.book_author, age_group
# HAVING COUNT(*) >= 50
# ORDER BY age_group, avg_rating DESC;

