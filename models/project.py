class Project:
  all_projects = []

  def __init__(self,title,description,due_date):
    self.title = title
    self.description = description
    self.due_date = due_date
    Project.all_projects.append(self)

