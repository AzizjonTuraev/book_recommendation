from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.postgres.hooks.postgres import PostgresHook
from datetime import datetime, timedelta

from io import StringIO
import csv

default_args = {
    "owner": "azizjon",
    "retries": 0,
    "retry_delay": timedelta(minutes=5)
}


def load_csv_to_postgres_using_psycopg2(**context):
    hook = PostgresHook(postgres_conn_id='postgres_localhost')
    conn = hook.get_conn()
    cursor = conn.cursor()

    csv_file_path = '/opt/airflow/dags/dataset/Ratings.csv'
    clean_data = StringIO()
    writer = csv.writer(clean_data)
    
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        writer.writerow(header)
        
        for row in reader:
            writer.writerow(row)

    clean_data.seek(0)
    cursor.copy_expert("COPY ratings FROM stdin WITH CSV HEADER DELIMITER ','", clean_data)
    conn.commit()
        
    cursor.close()
    conn.close()
    clean_data.close()


with DAG(
    dag_id="import_ratings_to_database",
    default_args=default_args, 
    start_date=datetime.today(),
    schedule_interval='0 0 * * *',
) as dag:

    load_books = PythonOperator(
        task_id='load_ratings_to_sql',
        python_callable=load_csv_to_postgres_using_psycopg2,
        provide_context=True,
        dag=dag
    )




