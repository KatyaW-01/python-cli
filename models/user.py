class User:
  all_users = []

  def __init__(self,name,email):
    self.name = name
    self.email = email
    User.all_users.append(self)

  def add_project(self):
    pass

  def display_projects(self):
    pass
    #return all projects a user has