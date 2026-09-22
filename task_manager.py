class Task:

    def __init__(self, task_id, location, priority="HIGH"):

        self.task_id = task_id
        self.location = location
        self.priority = priority
        self.status = "CREATED"
        self.assigned_robot = None

    def assign(self, robot):

        self.assigned_robot = robot
        self.status = "ASSIGNED"

        print(
            f"\n[GATEWAY] Task {self.task_id} "
            f"assigned to {robot}"
        )

    def update_status(self, status):

        self.status = status

        print(
            f"[GATEWAY] Task {self.task_id} "
            f"status: {status}"
        )


class TaskManager:

    def __init__(self):

        self.task_counter = 0
        self.tasks = []

    def create_task(self, location):

        self.task_counter += 1

        task = Task(
            task_id=f"T{self.task_counter:03}",
            location=location
        )

        self.tasks.append(task)

        print("\n[GATEWAY] New task created")
        print(f"Task ID: {task.task_id}")
        print(f"Location: {task.location}")
        print(f"Priority: {task.priority}")

        return task
