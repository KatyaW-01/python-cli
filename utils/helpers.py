from models.user import User
from models.project import Project

def handle_add_user(args):
  try:
    User.create(args.name,args.email)
    print("User successfully created")
  except ValueError as e:
    print(f"Error: {e}")

def handle_add_project(args):
  try:
    Project.create(args.title,args.description,args.due_date)
    print("Project successfully created")
  except ValueError as e:
    print(f"Error: {e}")