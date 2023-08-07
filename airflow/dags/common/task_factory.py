from airflow.operators.bash import BashOperator

class TaskFactory:
    
    def __init__(self):
        pass

    def create_bash_task(self, pipeline, command):
        return BashOperator(
            task_id='{}_task'.format(pipeline),
            bash_command=command
        )
