import argparse
from models.user import User
from utils.helpers import handle_add_user, handle_add_project, handle_add_task, handle_display_users

def main():
  parser = argparse.ArgumentParser(description="Project Management Tool")
  subparsers = parser.add_subparsers(dest="command",required=True)

  #subcommand add user
  add_user_parser = subparsers.add_parser('add-user',help="add a new user")
  add_user_parser.add_argument('name', help="name of the user")
  add_user_parser.add_argument('email', help="email of the user")
  add_user_parser.set_defaults(func=handle_add_user)

  #subcommand add project
  add_project_parser = subparsers.add_parser('add-project', help="add a project")
  add_project_parser.add_argument('title',help="project title")
  add_project_parser.add_argument('description',help="project description")
  add_project_parser.add_argument('due_date', help="project due date")
  add_project_parser.set_defaults(func=handle_add_project)

  #subcommand add task
  add_task_parser = subparsers.add_parser('add-task',help="add a task")
  add_task_parser.add_argument('title',help="task title")
  add_task_parser.add_argument('status',help="task status")
  add_task_parser.add_argument('assigned_to',help="project the task is assigned to")
  add_project_parser.set_defaults(func=handle_add_task)

  #subcommand display users
  list_users_parser = subparsers.add_parser('list-users',help="list all users")
  list_users_parser.set_defaults(func=handle_display_users)

  #subcommand add project to user
  add_project_to_user_parser = subparsers.add_parser('assign-project',help="add a project to a user")
  add_project_to_user_parser.add_argument('user_id', type=int, help="the id of the user you want to assign the project to")
  add_project_to_user_parser.add_argument('project_id', type=int, help="the id of the project you want to assign to the user")

  #add_project_to_user_parser.set_defaults(func=)

  #call functions
  args = parser.parse_args()
  args.func(args)

if __name__ == "__main__":
  main()

