
#contains all widgets and calls functions from taak_manager module!

import tkinter as tk
import task_manager as tm #now can use CRUD functions
from tkinter import ttk 
from tkinter import messagebox

from datetime import datetime #to show date (due date and toadys current date!!)


def showWidget(window):
  
  ############# NEW WINDOW Top level ##############
  def open_task_window(): #to open new toplevel to add tasks!/
      
      task_window= tk.Toplevel(window)
      task_window.title(" Add Tasks ")
      task_window.geometry("300x150")
      
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
                entry.delete(0, tk.END) #clear the entry
                task_window.destroy()
               
  
  
      button=tk.Button(task_window,
                           text="Add Task!!!!!!",
                           bg="#28E4C4",
                           fg="#071A2F",
                           command= addTaskTopLevel)
      button.pack()
      
  ############# endddddddddddddddddddddd #############
  
  #header in a frame
  header=tk.Frame(window,
                  bg="teal",
                  height=50)
  header.pack(fill="x")
  
  today= datetime.now().strftime("%A , %d %B %Y") #today's date
  
  tk.Label(header,
                 fg="black",
                 text= today).pack(side="left", padx=100) #to show todays date!!
  
  '''
  datetime module eg!
  today = datetime.now().strftime("%A, %d %B %Y")
  print(today)   # Output: Saturday, 30 August 2026
  
  %A  Full weekday name (Saturday)

  %d  Day of month (30)

  %B  Full month name (August)

  %Y  Full year (2026)
  '''
  
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
   
   
  # +add task btn
  addTaskButton= tk.Button(sidebar,
                           text=" + New Task ",
                           bg="#C8DFDB",
                           fg="#3368A0",
                           command= open_task_window)
  addTaskButton.pack(fill="x",pady=5)
  
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
                     columns =("check","title","due_date","priority","delete"),
                     show="headings")
  
  tree.heading("check",text="")
  
  tree.heading("title",text="Task")
  tree.heading("due_date",text="Due date")
  tree.heading("priority",text="Priority")
  tree.heading("delete", text="") #no heading for del icon
  
  tree.column("check",width=40,anchor="center") #attributes for cols
  tree.column("title",width= 300,anchor="w")  #attri for cols
  
  tree.column("due_date", width=40, anchor="center")
  tree.column("priority", width=40, anchor="center")
  tree.column("delete", width=50, anchor="center")
  
  
  tree.pack(fill="both", expand=True)
  
  def on_tree_click(event):
    
    region= tree.identify("region", event.x, event.y)
    if region != "cell":
      return
    
    column = tree.identify_column(event.x)  # return #1 , #2 , #3
    row_iid = tree.identify_row(event.y)    #returns iid of clicked row
    
    if not row_iid:
      return
    
    task_id = int(row_iid)
    
    if column == "#3":
    
      confirm = messagebox.askyesno("Delete task","Delete This Task?") # returns True if yes else False
      
      if confirm:
        tm.delete_task(task_id)
        refresh_task_list()
        
    if column == "#1":
      
      tm.toggle_task(task_id)
      refresh_task_list()
    
  tree.bind("<Button-1>", on_tree_click)


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
        values=(check_symbol, task["title"], "🗑")
      )

  
  
      
      
    

  
  refresh_task_list()
  
  
