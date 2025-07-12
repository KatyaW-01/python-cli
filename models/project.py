from task import Task

class Project:
  all_projects = []

  def __init__(self,title,description,due_date):
    self.title = title
    self.description = description
    self.due_date = due_date
    Project.all_projects.append(self)

  def add_task(self):
    pass
    #add tasks to a project

  def project_tasks(self): #return all tasks associated with the project
    tasks = []
    for task in Task.all_tasks:
      pass

