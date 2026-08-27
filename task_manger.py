
#pure python and contains CRUD for tasks and other ncessary functions

tasks = []


  
def addTask(title):
  
  tasks.append(title)
  print("task added ",title)
  
def getTasks():
  return list(tasks)
  
  