from utils.file_io import save_tasks

class Task:
  all_tasks = []
  next_id = 1

  def __init__(self,task_id,title,status,assigned_to):
    self.id = task_id
    self.title = title
    self.status = status
    self.assigned_to = assigned_to #id or the project object

  def complete(self,task_id):
    for task in self.all_tasks:
      if task.id == task_id and task.status == "completed":
        print("Task has already been completed")
        return None
      elif task.id == task_id  and task.status != "completed":
        task.status = "completed"
        return
    print("Task not found")

  def to_dict(self):
    return {
      "id": self.id,
      "title": self.title,
      "status": self.status,
      "assigned_to": self.assigned_to
    }

  @classmethod
  def create(cls,title,status,assigned_to):
    for task in cls.all_tasks:
      if task.title.lower() == title.lower():
        print("Task already exists")
        return None
    task_id = cls.next_id
    cls.next_id += 1
    new_task = cls(task_id,title,status,assigned_to)
    cls.all_tasks.append(new_task)
    save_tasks()
    return new_task
