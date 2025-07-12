import json
import os 
from models.user import User
from models.project import Project
from models.task import Task

def save_users():
  with open("data/users.json", "w") as f:
    json.dump([User.to_dict() for user in User.all_users], f, indent=2)

def save_projects():
  with open("data/projects.json", "w") as f:
    json.dump([Project.to_dict() for project in Project.all_projects], f, indent=2)

def save_tasks():
  with open("data/tasks.json", "w") as f:
    json.dump([Task.to_dict() for task in Task.all_tasks], f, indent=2)

def load_users():
  if not os.path.exists("data/users.json"):
    return
  with open("data/users.json", "r") as f:
    data = json.load(f)
    for dict in data:
      user = User.from_dict(dict)
      User.all_users.append(user)

def load_projects():
  if not os.path.exists("data/projects.json"):
    return
  with open("data/projects.json", "r") as f:
    data = json.load(f)
    for dict in data:
      project = Project.from_dict(dict)
      Project.all_projects.append(project)