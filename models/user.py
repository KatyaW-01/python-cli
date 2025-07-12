from project import Project

class User:
  all_users = []
  next_id = 1

  def __init__(self,user_id, name,email):
    self.id = user_id
    self.name = name
    self.email = email
    self.projects = [] #each user has a list of projects
    

  def add_project(self,project_id):
    for project in self.projects: #loop through project array in this class
          if project.id == project_id:
            print("Project has already been added")
            return None
    for project in Project.all_projects: #loop through project array from project class
      if project.id == project_id:
        self.projects.append(project)
        return
    print("Project not found")
        
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
  