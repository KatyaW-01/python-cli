import argparse
from models.user import User
from utils.file_io import save_users

def handle_add_user(args):
  User.create(args.name,args.email)

def main():
  parser = argparse.ArgumentParser(description="Project Management Tool")
  subparsers = parser.add_subparsers(dest="command",required=True)

  #subcommand add user
  add_parser = subparsers.add_parser('add-user',help="add a new user")
  add_parser.add_argument('name', help="name of the user")
  add_parser.add_argument('email', help="email of the user")
  add_parser.set_defaults(func=handle_add_user)

  #subcommand add project
  

  #call functions
  args = parser.parse_args()
  args.func(args)

if __name__ == "__main__":
  main()

