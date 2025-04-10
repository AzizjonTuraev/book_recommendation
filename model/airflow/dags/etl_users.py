from airflow import DAG
from airflow.operators.python import PythonOperator
# import os
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta

from users_data_cleaning import get_correct_location, get_correct_age
from io import StringIO
import csv
import pandas as pd

default_args = {
    "owner": "azizjon",
    "retries": 0,
    "retry_delay": timedelta(minutes=5)
}


def load_users_to_postgres(**context):
    hook = PostgresHook(postgres_conn_id='postgres_localhost')
    conn = hook.get_conn()
    cursor = conn.cursor()

    users_df = pd.read_csv('/opt/airflow/dags/dataset/users.csv')
    users_df = get_correct_location(users_df)
    users_df = get_correct_age(users_df)

    clean_data = StringIO()
    users_df.to_csv(clean_data, index=False, header=True, na_rep='NULL')

    clean_data.seek(0)
    cursor.copy_expert("""
        COPY users 
        FROM stdin WITH CSV HEADER DELIMITER ',' NULL 'NULL'
    """, clean_data)
    conn.commit()
    
    cursor.close()
    conn.close()
    clean_data.close()


with DAG(
    dag_id="import_users_to_database",
    default_args=default_args, 
    # start_date=datetime(2025, 3, 21),
    start_date=datetime.today(),
    schedule_interval='0 0 * * *',
) as dag:

    load_books = PythonOperator(
        task_id='load_users_to_sql',
        python_callable=load_users_to_postgres,
        provide_context=True,
        dag=dag
    )




