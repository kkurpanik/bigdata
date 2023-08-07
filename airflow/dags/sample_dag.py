from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    "depends_on_past": False,
    "email": ["airflow@example.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    "sample_dag",
    default_args = default_args,
    description = "A sample DAG",
    schedule=None,
    start_date=datetime(2021, 1, 1)
    tags=["example"]
) as dag:
    t1 = BashOperator(
        task_id = "print_date",
        bash_command = "date"
    )

    t2 = BashOperator(
        task_id = "sleep",
        depends_on_past = False,
        bash_command = "sleep 5",
        retries = 3
    )

    t1 >> t2
