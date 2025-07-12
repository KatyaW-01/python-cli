class Task:
  all_tasks = []

  def __init__(self,title,status,assigned_to):
    self.title = title
    self.status = status
    self.assigned_to = assigned_to
    Task.all_tasks.append(self)