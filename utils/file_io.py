import json
import os 
from models.user import User
from models.project import Project
from models.task import Task

def save_users():
  with open("data/users.json", "w") as f:
    json.dump([User.to_dict() for user in User.all_users], f, indent=2)