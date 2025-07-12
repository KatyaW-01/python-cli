from task import Task

class Project:
  all_projects = []

  def __init__(self,title,description,due_date):
    self.title = title
    self.description = description
    self.due_date = due_date
    Project.all_projects.append(self)

  def add_project(self):
    pass
    #add project to a specific user

  def display_projects(self):
    pass
    #display projects associated with a specific user

  def project_tasks(self): #return all tasks associated with the project
    tasks = []
    for task in Task.all_tasks:
      pass

