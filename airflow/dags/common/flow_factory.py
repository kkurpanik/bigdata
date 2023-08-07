from .sensor_factory import SensorFactory
from .task_factory import TaskFactory

class FlowFactory:

    def __init__(self):
        self.task_factory = TaskFactory()
        self.sensor_factory = SensorFactory()

    def create_single_sensor_flow(self, pipeline, external_id):
        s = self.sensor_factory.create_external_sensor(pipeline, external_id)
        return s
    
    def create_single_bash_flow(self, pipeline, command):
        b = self.task_factory.create_bash_task(pipeline, command)
        return b
