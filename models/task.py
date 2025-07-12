class Task:
  all_tasks = []

  def __init__(self,title,status,assigned_to):
    self.title = title
    self.status = status
    self.assigned_to = assigned_to
    Task.all_tasks.append(self)

  def assign_task(self):
    pass
    #assign tasks to projects

  def complete(self):
    pass
    #mark tasks as complete

  def display_tasks(self):
    pass
    #display tasks assigned to specific users
