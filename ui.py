
#contains all widgets and calls functions from taak_manager module!

import tkinter as tk
import task_manager as tm #now can use CRUD functions
from tkinter import ttk 
from tkinter import messagebox

from datetime import datetime #to show date (due date and toadys current date!!)


def showWidget(window):
  current_date= datetime.now().strftime("%A , %d %B %Y") #today's date
  current_date_formatted= datetime.now().strftime("%Y-%m-%d")  # YYYY-MM-DD
  
  current_view= "all" 
  
  
  ############# NEW WINDOW Top level ##############
  def open_task_window(): #to open new toplevel to add tasks!/
      
      task_window= tk.Toplevel(window)
      task_window.title(" Add Tasks ")
      task_window.geometry("300x350")
      
      tk.Label(task_window,
                           text="Add New Task!",
                           bg="white",
                           fg="Black").pack(padx=5,pady=5)
      
      entry = tk.Entry(task_window, bg="#FDF4D2")
      entry.pack(pady=5)
      
      priority_label = tk.Label(task_window,
                                text="Priority- ")
      priority_label.pack()
      
      priority_combo = ttk.Combobox(task_window,
                                    values= ("Low" , "Medium" , "High"),
                                    state="readonly")
      
      priority_combo.set("Low") #default is low!
      priority_combo.pack(padx=5, pady=5)
      
      
      due_date_label = tk.Label(task_window,
                                text="Due date ( YYYY-MM-DD ): ")
      due_date_label.pack( padx=5,pady=5)
      
      due_date_entry = tk.Entry(task_window)
      
      due_date_entry.insert(0, current_date_formatted  ) # predef values to match toadys day
      due_date_entry.pack(padx=5,pady=5)
      
      def addTaskTopLevel():  
              title= entry.get().strip() #get the task
              priority= priority_combo.get().lower()  #get the priority (lol i forgot braces and it returned the method :P)
              due_date= due_date_entry.get()    #get the due date
              
              if title:
                    
                tm.addTask(title, due_date, priority ) #add task
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
  
  
  
  tk.Label(header,
                 fg="black",
                 text= current_date).pack(side="left", padx=100) #to show todays date!!
  
  view_label = tk.Label(header,
                        text="All Tasks",
                        bg="black",
                        fg="white",
                        font=("Arial",12,"bold")
                        )
  view_label.pack(side="left", padx=50)
  
  
  
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
  
  
  
  def change_view(view):
    
    nonlocal current_view
    
    #default view
    
    
    
    '''
    Why nonlocal?
    Because current_view is defined in the enclosing function showWidget(), not in the global scope. The nonlocal keyword tells Python to modify that variable instead of creating a new local one!!
    '''
    
    current_view = view
    view_label.config(text= current_view + " Tasks") # formatting is missing but good for now! :P , it chnages according to current page , lol here was a bug i tried to place this out of this func()
    
    
    refresh_task_list()  #refresh and show evrything (what list holds) again!!
   
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
                        command= lambda:change_view("today"))
  btn_today.pack(fill="x", pady=5)
  
  '''
  Why lambda?
  Button commands expect a function without arguments. lambda: change_view("today") creates an anonymous function that, when clicked, calls change_view with the correct argument
  '''
  
  
  
  #button to show All tasks in the sideframe
  btn_all_tasks = tk.Button(sidebar,
                            text="All Tasks ",
                            command=lambda:change_view("all"))
  btn_all_tasks.pack(fill="x", pady=5)
  
  btn_completed = tk.Button(sidebar,
                              text="Completed ",
                              command=lambda:change_view("completed"))
  btn_completed.pack(fill="x", pady=5)
    
  btn_settings = tk.Button(sidebar,
                              text="Settings ",
                              command=lambda:change_view("settings"))
  btn_settings.pack(fill="x", pady=5)
   
  
    
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
  
  tree.column("due_date", width=100, anchor="center")
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
    
    if column == "#5":
    
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
      
     # show tasks wth checkbox icon!
      
    all_task_to_show = tm.getTasks()  # create new list by storing all the tasks!
      
    if current_view =="today":
        all_task_to_show= [t for t in all_task_to_show if t["due_date"]== current_date_formatted] # to filter and see toadys tasks!
       
    elif current_view == "completed":
        all_task_to_show = [t for t in all_task_to_show if t["done"]]
        
    for task in all_task_to_show:  #created new list acc to the current_view!!
        check_symbol = "☑" if task["done"] else "☐"
        tree.insert(
          
          "",
          "end",
          iid= str(task["id"]),
          values=(check_symbol, task["title"],task["due_date"], task["priority"] , "🗑")
        )

  
  
      
      
    

  
  refresh_task_list()
  
  
