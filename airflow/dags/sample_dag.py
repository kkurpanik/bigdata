from airflow import DAG
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
    schedule=timedelta(days=1),
    start_date=datetime(2023,8,8),
    catchup=False,
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
