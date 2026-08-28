
#pure python and contains CRUD for tasks and other ncessary functions

tasks = []
next_id = 1

  
def addTask(title):
  
  global next_id
  task ={
    "id": next_id,
    "title": title,
    "done": False
  }
  
  tasks.append(task)
  
  next_id += 1
  return task["id"]
  
def getTasks():
  return list(tasks)

def delete_task(task_id):
  global tasks #lists used here , 
  
  
  tasks = [t for t in tasks if t["id"] != task_id] #keeps only those which doesnt match the task_id , deltes the rest if them / donest add them
  
def toggle_task(task_id):
  
  for t in tasks:
    if t["id"] == task_id:
      t["done"] = not t["done"]
      return t["done"]
    
  return None
  
  