from models.task import Task
from utils.file_io import save_projects

class Project:
  all_projects = []
  next_id = 1

  def __init__(self,project_id,title,description,due_date):
    self.id = project_id
    self.title = title
    self.description = description
    self.due_date = due_date
    self.tasks = []

  def add_task(self,task_id):
    for task in self.tasks:
      if task.id == task_id:
        print("Task has already been added")
        return None
    for task in Task.all_tasks:
      if task.id == task_id:
        self.tasks.append(task)
        return
    print("Task not found")

  def project_tasks(self):
    return self.tasks
  
  #turn object data into dictionary for writing to json file
  def to_dict(self):
    return {
      "id": self.id,
      "title": self.title,
      "description": self.description,
      "due_date": self.due_date
    }
  
  #for loading data from json file, creates the objects again
  @classmethod
  def from_dict(cls,data):
    project = cls(data["id"], data["title"], data["description"], data["due_data"])
    project.tasks = []
    return project

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
    save_projects()
    return new_project

