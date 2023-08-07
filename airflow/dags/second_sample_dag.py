from airflow import DAG
from common.constants import default_args
from common.flow_factory import FlowFactory
from datetime import datetime


flow_factory = FlowFactory()
with DAG(
    dag_id='second_sample_dag',
    default_args=default_args,
    description="Second sample DAG",
    schedule=None,
    start_date=datetime(2021, 1, 1),
    tags=["samples"]) as dag:

    first_external_sensor = flow_factory.create_single_sensor_flow('second', 'first_sample_dag')
    print_date_task = flow_factory.create_single_bash_flow('print_date', 'echo `date`')
    sleep_15 = flow_factory.create_single_bash_flow('sleep_15', 'sleep 15')

    first_external_sensor >> print_date_task >> sleep_15
