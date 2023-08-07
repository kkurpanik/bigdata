from airflow.sensors.external_task import ExternalTaskSensor
from airflow.models.dagrun import DagRun

class SensorFactory:

    def __init__(self):
        pass

    def __last_execution_date(self, execution_date, **kwargs):
        lookup_str_before = "_wait_for_"
        lookup_str_after = "_sensor"
        task_instance = str(kwargs["task_instance"])
        parent_dag_name = task_instance.split(lookup_str_before, 1)[1].split(lookup_str_after, 1)[0]
        parent_dag_runs = DagRun.find(dag_id=parent_dag_name)
        parent_dag_runs.sort(key=lambda x: x.execution_date, reverse=True)
        if parent_dag_runs:
            last_execution_date = parent_dag_runs[0].execution_date
            return last_execution_date
        else:
            return execution_date
    
    def create_external_sensor(self, pipeline, external_id):
        return ExternalTaskSensor(
            task_id='{}_wait_for_{}_sensor'.format(pipeline, external_id),
            external_dag_id=external_id,
            execution_date_fn=self.__last_execution_date,
            mode='reschedule',
            timeout=360
        )
