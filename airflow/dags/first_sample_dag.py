from airflow import DAG
from common.constants import default_args
from common.flow_factory import FlowFactory
from datetime import datetime


flow_factory = FlowFactory()
with DAG(
    dag_id='first_sample_dag',
    default_args=default_args,
    description="First sample DAG",
    schedule=None,
    start_date=datetime(2021, 1, 1),
    tags=["samples"]) as dag:

    print_date_task = flow_factory.create_single_bash_flow('print_date', 'echo `date`')
    sleep_60 = flow_factory.create_single_bash_flow('sleep_60', 'sleep 60')

    print_date_task >> sleep_60
