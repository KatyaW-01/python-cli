class User:
  all_users = []

  def __init__(self,name,email):
    self.name = name
    self.email = email
    self.projects = [] #each user has a list of projects
    User.all_users.append(self)

  def add_project(self):
    pass

  def display_projects(self):
    pass
    #return all projects a user has

  def display_tasks(self):
    pass
    #display tasks assigned to a specific user

  @classmethod
  def create(cls,name,email):
    for user in cls.all_users:
      if user.name.lower() == name.lower():
        print("User with that name already exists")
        return None
    new_user = cls(name,email)
    cls.all_users.append(new_user)
    return new_user