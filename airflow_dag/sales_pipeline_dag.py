from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


def run_etl():

    df = extract_data()

    daily_sales, top_products, customer_sales = transform_data(df)

    load_data(daily_sales)


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024,1,1)
}

dag = DAG(
    'sales_pipeline',
    default_args=default_args,
    schedule_interval='@daily'
)

etl_task = PythonOperator(
    task_id='run_etl',
    python_callable=run_etl,
    dag=dag
)
