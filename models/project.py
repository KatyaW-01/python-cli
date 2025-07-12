from task import Task

class Project:
  all_projects = []
  next_id = 1

  def __init__(self,project_id,title,description,due_date):
    self.id = project_id
    self.title = title
    self.description = description
    self.due_date = due_date

  def add_task(self):
    pass
    #add tasks to a project

  def project_tasks(self): #return all tasks associated with the project
    tasks = []
    for task in Task.all_tasks:
      pass

  @classmethod
  def create(cls,title,description,due_date):
    for project in cls.all_projects:
      if project.title.lower() == title.lower():
        print("Project with that title already exists")
        return None
    project_id = cls.next_id
    cls.next_id += 1
    new_project = cls(project_id,title,description,due_date)
    cls.all_projects.append(new_project)
    return new_project

