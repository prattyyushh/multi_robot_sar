from task_manager import TaskManager


class Coordinator:

    def __init__(self):

        self.task_manager = TaskManager()

    def create_detection_task(self, detection):

        location = detection["location"]

        task = self.task_manager.create_task(
            location
        )

        return task

    def dispatch_scout(self, task):

        task.assign("SCOUT_1")

        task.update_status(
            "IN_PROGRESS"
        )

    def dispatch_verifier(self, task):

        task.assign("VERIFIER_2")

        task.update_status(
            "VERIFICATION"
        )

    def complete_task(self, task):

        task.update_status(
            "COMPLETED"
        )
