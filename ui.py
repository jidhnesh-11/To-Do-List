
#contains all widgets and calls functions from taak_manager module!

import tkinter as tk
import task_manger as tm #now can use CRUD functions

def showWidget(window):
  
  label=tk.Label(window,
                 text="To Do List",
                 bg="teal",
                 fg="black")
  label.pack(padx=10,pady=10)
  
  entry=tk.Entry(window,
                 bg="#FDF4D2"
                 )
  entry.pack()
  
  def onAddClick():
    
    title= entry.get().strip()
    
    if title:
      
      tm.addTask(title) #add task
      
      entry.delete(0, tk.END) #clear the entry
      
      all_tasks ="\n".join(tm.getTasks()) #to display the list thats contains all the task in tm
      
      display_label.config(text=all_tasks)
  
  display_label=tk.Label(window,
                   text="",
                   bg="#FDF4D2",
                   fg="#AF719D")
  display_label.pack()
    
  addTaskButton= tk.Button(window,
                           text="Add Task",
                           bg="#C8DFDB",
                           fg="#3368A0",
                           command= onAddClick)
  addTaskButton.pack()
  
  
  
  
  

    