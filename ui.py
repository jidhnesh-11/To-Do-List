
#contains all widgets and calls functions from taak_manager module!

import tkinter as tk

import task_manager as tm #now can use CRUD functions
import themes as th

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
      task_window.geometry("400x450")
      task_window.resizable(False , False)
      task_window.configure(bg= th.toplevel_BG )
      
      card = tk.Frame(task_window,
                      bg="white",
                      padx=30,
                      pady=30,
                      highlightthickness=2,
                      highlightbackground="#E5E7EB")
      card.pack(fill="both", expand=True, padx=15, pady=15)
      
      tk.Label(card,
                           text="Add New Task!",
                           font= ("Seouge UI" , 12 , "bold"),
                           bg="white",
                           fg=th.add_task_label_color).pack(padx=5,pady=5)
      
      entry = tk.Entry(card, bg="#FDF4D2")
      entry.pack(pady=5, padx=5)
      
      priority_label = tk.Label(card,
                                text="Priority- ")
      priority_label.pack(pady=5, padx=5)
      
      priority_combo = ttk.Combobox(card,
                                    values= ("Low" , "Medium" , "High"),
                                    state="readonly") #comboBox!!
      
      priority_combo.set("Low") #default is low!
      priority_combo.pack(padx=5, pady=5)
      
      
      due_date_label = tk.Label(card,
                                text="Due date ( YYYY-MM-DD ): ")
      due_date_label.pack( padx=5,pady=5)
      
      due_date_entry = tk.Entry(card)
      
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
               
  
  
      button=tk.Button(card,
                           text="Add Task!!!!!!",
                           bg="#28E4C4",
                           fg="#071A2F",
                           command= addTaskTopLevel)
      button.pack()
      
  ############# endddddddddddddddddddddd #############
  
    
  #sidebar in a frame  LEFT SIDE!!
  sidebar= tk.Frame(window,   #main frame!!!!
                      bg= th.sidebar_BG,
                      width=250)
    
  sidebar.pack_propagate(False) # tkinter knows to use the width /height rather than applying default locked in frame
    
  sidebar.pack(side= "left",fill="y")
    
  #framesss of sidebar!!
  
  profile_frame = tk.Frame(sidebar,
                           bg=th.sidebar_BG)
  profile_frame.pack(fill="x", padx= 10, pady=(10,5))  
  
  pfp = tk.PhotoImage(file= 'cat_pfp.png').subsample(7,7) #built in library to resizee imageeeeee!!
    
  window.pfp = pfp # keeps the referenced image instead of deleting it , if not used the image isnt rendered lol
  
  usr_photo_name = tk.Label(profile_frame,
                              image= pfp,
                              text="   Jidhnesh",
                              compound='left',
                              bg= th.sidebar_BG,
                              fg="white",
                              font=("Seouge UI",15)) 
  usr_photo_name.pack(anchor='w',padx=10,pady=10)
  
  #separator lineeeeee!
  
  sep1= tk.Frame(sidebar,
                 bg= "#E3F2FD",
                 height=2)
  sep1.pack(fill="x", padx=10, pady=5)
    
  #task butttonnnnnnnnnn!!
  
  addTaskButton= tk.Button(sidebar,
                             text=" + New Task ",
                             bg="#C8DFDB",
                             fg="#3368A0",
                             width=30,
                             command= open_task_window)
  addTaskButton.pack(padx=5,pady=5)
   
  #2nd separtor lineee
  
  sep2 = tk.Frame(sidebar, bg="#E3F2FD", height=2)
  sep2.pack(fill="x", padx=10, pady=5)
  
  # right side that holds content and header!!!
  right_area = tk.Frame(window,
                          bg= th.content_BG)
  right_area.pack(side="right", fill="both", expand=True)
    
  #actual content!!! inside the "main frame"
  
  header=tk.Frame(right_area,
                    bg= th.header_color,
                    height=80,
                    relief= "sunken",
                    padx=5,
                    pady=5)
  header.pack_propagate(False) #again to not use default hegiht and width but for header
  header.pack(fill="x") 
  
  
  content= tk.Frame(right_area,
                      bg= th.content_BG,
                      relief="flat")
  content.pack( fill="both",expand=True, padx=10, pady=10)
    
  #header in a frame
  
  
  
  view_label = tk.Label(header,
                          text="All Tasks",
                          bg=th.header_color,
                          fg="white",
                          font=("Seouge UI",15,"bold")
                          )
  view_label.pack(side="left", padx=20)
    
  date_label= tk.Label(header,
                 fg=th.current_date,
                 bg= th.header_color,
                 text= current_date,
                 font=("Seouge UI",15,"bold"))
  date_label.pack(side="right", padx=20) #to show todays date!!
  
  
  
  
  '''
  datetime module eg!
  today = datetime.now().strftime("%A, %d %B %Y")
  print(today)  --- Output: Saturday, 30 August 2026
  
  %A  Full weekday name (Saturday)

  %d  Day of month (30)

  %B  Full month name (August)

  %Y  Full year (2026)
  '''
  
 
  
  
  def change_view(view):
    
    
    
    nonlocal current_view

    '''
    Why nonlocal?
    Because current_view is defined in the enclosing function showWidget(), not in the global scope. The nonlocal keyword tells Python to modify that variable instead of creating a new local one!!
    '''
    #default view
    current_view = view
    
    view_titles= {
      
      "today": "Today's Tasks",
      "all": "All Tasks",
      "completed": "Completed Tasks",
      "settings": "Settings"
    }
    
    view_label.config(text=view_titles.get(view,"Tasks"))
    
    
  
  
  #button to show toadys task in the sideframe  
  btn_today = tk.Button(sidebar,
                        text=" Toaday's Tasks ",
                        width=30,
                        command= lambda:change_view("Today"))
  btn_today.pack(padx=5, pady=5)
  
  '''
  Why lambda?
  Button commands expect a function without arguments. lambda: change_view("today") creates an anonymous function that, when clicked, calls change_view with the correct argument
  '''
  
  
  
  #button to show All tasks in the sideframe
  btn_all_tasks = tk.Button(sidebar,
                            text="All Tasks ",
                            activebackground= "#BDCDD6",
                            bg="#EEE9DA",
                            fg="#6096B4",
                            width=30,
                            command=lambda:change_view("all"))
  btn_all_tasks.pack(padx=5, pady=5)
  
  btn_completed = tk.Button(sidebar,
                              text="Completed ",
                              width=30,
                              command=lambda:change_view("completed"))
  btn_completed.pack(padx=5, pady=5)
    
  btn_settings = tk.Button(sidebar,
                              text="Settings ",
                              width=30,
                              command=lambda:change_view("settings"))
  btn_settings.pack(padx=5, pady=5)
   
  
    
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
    
    if column == "#5": #del col
    
      confirm = messagebox.askyesno("Delete task","Delete This Task?") # returns True if yes else False
      
      if confirm:
        tm.delete_task(task_id)
        refresh_task_list()
        
    if column == "#1": #check Box col
      
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
  
  
