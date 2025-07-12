import json
import os 

def save_users():
  from models.user import User
  with open("data/users.json", "w") as f:
    json.dump([user.to_dict() for user in User.all_users], f, indent=2)

def save_projects():
  from models.project import Project
  with open("data/projects.json", "w") as f:
    json.dump([project.to_dict() for project in Project.all_projects], f, indent=2)

def save_tasks():
  from models.task import Task
  with open("data/tasks.json", "w") as f:
    json.dump([task.to_dict() for task in Task.all_tasks], f, indent=2)

def load_users():
  from models.user import User
  if not os.path.exists("data/users.json"):
    return
  with open("data/users.json", "r") as f:
    data = json.load(f)
    for dict in data:
      user = User.from_dict(dict)
      User.all_users.append(user)

def load_projects():
  from models.project import Project
  if not os.path.exists("data/projects.json"):
    return
  with open("data/projects.json", "r") as f:
    data = json.load(f)
    for dict in data:
      project = Project.from_dict(dict)
      Project.all_projects.append(project)

def load_tasks():
  from models.task import Task
  if not os.path.exists("data/tasks.json"):
    return
  with open("data/tasks.json", "r") as f:
    data = json.load(f)
    for dict in data:
      task = Task.from_dict(dict)
      Task.all_tasks.append(task)