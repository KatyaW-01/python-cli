class Task:
  all_tasks = []
  next_id = 1

  def __init__(self,task_id,title,status,assigned_to):
    self.id = task_id
    self.title = title
    self.status = status
    self.assigned_to = assigned_to

  def complete(self):
    pass
    #mark tasks as complete

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
    return new_task
