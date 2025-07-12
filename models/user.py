class User:
  all_users = []
  next_id = 1

  def __init__(self,user_id, name,email):
    self.id = user_id
    self.name = name
    self.email = email
    self.projects = [] #each user has a list of projects
    

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
    user_id = cls.next_id
    cls.next_id += 1
    new_user = cls(user_id,name,email)
    cls.all_users.append(new_user)
    return new_user
  