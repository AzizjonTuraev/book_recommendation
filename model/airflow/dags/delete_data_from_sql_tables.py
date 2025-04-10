from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator
from airflow.models.baseoperator import chain

default_args = {
    "owner": "azizjon",
    "retries": 1,
    "retry_delay": timedelta(minutes=1)
}


with DAG(
    dag_id="delete_table_data",
    default_args=default_args, 
    start_date=datetime.today(),
    schedule_interval=None,
    catchup=False
) as dag:


    delete_data_from_books = SQLExecuteQueryOperator(
        task_id='delete_data_task_books',
        conn_id='postgres_localhost',
        sql="""
            DELETE FROM books;
        """
    )


    delete_data_from_ratings = SQLExecuteQueryOperator(
        task_id='delete_data_task_ratings',
        conn_id='postgres_localhost',
        sql="""
            DELETE FROM ratings;
        """
    )

    delete_data_from_users = SQLExecuteQueryOperator(
        task_id='delete_data_task_users',
        conn_id='postgres_localhost',
        sql="""
            DELETE FROM users;
        """
    )

    chain(delete_data_from_ratings, [delete_data_from_users, delete_data_from_books])
