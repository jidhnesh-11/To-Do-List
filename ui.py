
#contains all widgets and calls functions from taak_manager module!

import tkinter as tk
import task_manger as tm #now can use CRUD functions
from tkinter import ttk 

def showWidget(window):
  
  #header in a frame
  header=tk.Frame(window,
                  bg="teal",
                  height=50)
  header.pack(fill="x")
  
  #main area in a frame
  main= tk.Frame(window,
                 bg="#FDF4D2")
  main.pack(fill="both",expand=True)
  
  #sidebar in a frame
  sidebar= tk.Frame(main,   #main frame!!!!
                    bg="#C8DFDB",
                    width=150)
  sidebar.pack(side= "left",fill="y")
  
  
  #actual content!!! inside the "main frame"
  
  content= tk.Frame(main,
                    bg="#FFFCE1")
  content.pack(side="right", fill="both",expand=True)
  
  def show_todays_tasks():
    print("Showing Toadys tasks")
    
  def show_all_tasks():
    print("Showing all tasks")
   
  #button to show toadys task in the sideframe  
  btn_today = tk.Button(sidebar,
                        text=" Toaday's Tasks ",
                        command=show_todays_tasks)
  btn_today.pack(fill="x", pady=5)
  
  #button to show All tasks in the sideframe
  btn_all_tasks = tk.Button(sidebar,
                            text="All Tasks ",
                            command=show_all_tasks)
  btn_all_tasks.pack(fill="x", pady=5)
  
  #main treeview inside the "content" frame!
  tree= ttk.Treeview(content,
                     columns =("check","title"),
                     show="headings")
  tree.heading("check",text="")
  tree.heading("title",text="task")
  
  tree.column("check",width=40,anchor="center") #attributes for cols
  tree.column("title",width= 300,anchor="w")  #attri for cols
  
  tree.pack(fill="both", expand=True)
  


  #refresh the tasks and show in the "content" frame
  
  def refresh_task_list():
    
    for item in tree.get_children(): #deleete the tasks
      tree.delete(item)
      
    for task in tm.getTasks(): # show tasks wth checkbox icon!
      
      check_symbol = "☑" if task["done"] else "☐"
      tree.insert(
        
        "",
        "end",
        iid= str(task["id"]),
        values=(check_symbol, task["title"])
      )

  
  def open_task_window(): #to open new toplevel to add tasks!/
      
      task_window= tk.Toplevel(window)
      task_window.title(" Add Tasks ")
      task_window.geometry("300x200")
      
      tk.Label(task_window,
                           text="Add New Task!",
                           bg="white",
                           fg="Black").pack(padx=5,pady=5)
      
      entry = tk.Entry(task_window, bg="#FDF4D2")
      entry.pack(pady=5)
      
      def addTaskTopLevel():  
              title= entry.get().strip()
                  
              if title:
                    
                tm.addTask(title) #add task
                refresh_task_list()
                task_window.destroy
                entry.delete(0, tk.END) #clear the entry
  
  
      button=tk.Button(task_window,
                           text="Add Task!!!!!!",
                           bg="#28E4C4",
                           fg="#071A2F",
                           command= addTaskTopLevel)
      button.pack()
      
      
    
  addTaskButton= tk.Button(window,
                           text="Add Task",
                           bg="#C8DFDB",
                           fg="#3368A0",
                           command= open_task_window)
  addTaskButton.pack()
  
  
