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
    
    csv_file_path = '/opt/airflow/dags/dataset/Books.csv'
    bad_rows = []  # To store malformed rows
    current_year = datetime.now().year
    
    # Create a temporary file-like object for clean data
    clean_data = StringIO()
    writer = csv.writer(clean_data)
    
    with open(csv_file_path, 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        writer.writerow(header)
        
        for i, row in enumerate(reader, 2):
            try:
                if len(row) > 3:  # Ensure row has enough columns
                    year_of_publication = int(row[3])
                    
                    if year_of_publication > current_year:
                        row[3] = 0
                    
                    writer.writerow(row)
                else:
                    raise ValueError("Not enough columns")
            except (ValueError, IndexError) as e:
                bad_rows.append(f"Line {i}: {row} | Error: {str(e)}")
    
    clean_data.seek(0)
    cursor.copy_expert("COPY books FROM stdin WITH CSV HEADER DELIMITER ','", clean_data)
    conn.commit()

    if bad_rows:
        print("\n=== MALFORMED ROWS SKIPPED ===")
        for row in bad_rows:
            print(row)
        print(f"\nTotal bad rows: {len(bad_rows)}")
    
    cursor.close()
    conn.close()
    clean_data.close()


with DAG(
    dag_id="import_books_to_database",
    default_args=default_args, 
    start_date=datetime.today(),
    schedule_interval='0 0 * * *',
) as dag:

    load_books = PythonOperator(
        task_id='load_books_to_sql',
        python_callable=load_csv_to_postgres_using_psycopg2,
        provide_context=True,
        dag=dag
    )


