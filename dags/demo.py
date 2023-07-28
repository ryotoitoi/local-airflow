from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from airflow.decorators import task
import logging

logging.basicConfig(level=logging.INFO)
LOGGER= logging.getLogger(__name__)

@task(task_id="log_message")
def log_message():
    LOGGER.info("This task is running!")

# DAGの定義とタスクの作成を 'with' 文を使用して行います。
with DAG(
    'demo',
    default_args={'owner': 'airflow'},
    description='A simple tutorial DAG',
    schedule_interval='0 12 * * *',
    start_date=days_ago(1),
    tags=['example']
) as dag:
    log_task = log_message()

    log_task
