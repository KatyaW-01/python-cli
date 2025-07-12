class Task:
  all_tasks = []

  def __init__(self,title,status,assigned_to):
    self.title = title
    self.status = status
    self.assigned_to = assigned_to
    Task.all_tasks.append(self)

  def complete(self):
    pass
    #mark tasks as complete

  @classmethod
  def create(cls,title,status,assigned_to):
    for task in cls.all_tasks:
      if task.title.lower() == title.lower():
        print("Task already exists")
        return None
    new_task = cls(title,status,assigned_to)
    cls.all_tasks.append(new_task)
    return new_task
