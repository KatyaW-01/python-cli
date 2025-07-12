from models.user import User
from models.project import Project
from models.task import Task
from utils.file_io import load_users

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

def handle_add_task(args):
  try:
    Task.create(args.title,args.status,args.assigned_to)
    print("Task successfully created")
  except ValueError as e:
    print(f"Error: {e}")

def handle_display_users(args):
  load_users()
  if len(User.all_users) == 0:
    print("No users found")
    return
  for user in User.all_users:
    print(f"Id: {user.id}, Name: {user.name}, Email: {user.email}")