from models.project import Project
from utils.file_io import save_users

class User:
  all_users = []
  next_id = 1

  def __init__(self,user_id, name,email):
    self.id = user_id
    self.name = name
    self.email = email
    self.projects = [] 
    
  def add_project(self,project_id):
    for project in self.projects:
          if project.id == project_id:
            print("Project has already been added")
            return None
    for project in Project.all_projects:
      if project.id == project_id:
        self.projects.append(project)
        return
    print("Project not found")
        
  def display_projects(self):
    return self.projects 
  
  #turn object data into dictionary for writing to json file
  def to_dict(self):
    return {
      "id": self.id,
      "name": self.name,
      "email": self.email,
      "projects": [project.id for project in self.projects]
    }
  
  #for loading data from json file, creates the objects again 
  @classmethod
  def from_dict(cls,data):
    user = cls(data["id"], data["name"], data["email"]) 
    user.projects = []
    return user

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
    save_users()
    return new_user
  
  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self,value):
    if not isinstance(value, str):
            raise TypeError("Name must be a string")
    if len(value) < 3:
        raise ValueError("Name must be at least 3 characters long")
    self._name = value