
#contains all widgets and calls functions from taak_manager module!

import tkinter as tk
import task_manger as tm #now can use CRUD functions

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
    
  btn_today = tk.Button(sidebar,
                        text=" Toaday's Tasks ",
                        command=show_todays_tasks)
  btn_today.pack(fill="x", pady=5)
  
  btn_all_tasks = tk.Button(sidebar,
                            text="All Tasks ",
                            command=show_all_tasks)
  btn_all_tasks.pack(fill="x", pady=5)
  
   
  label=tk.Label(window,
                 text="To Do List",
                 bg="teal",
                 fg="black")
  label.pack(padx=10,pady=10)

  

  
  def open_task_window(): #to open new toplevel to add tasks!/
      
      task_window= tk.Toplevel(window)
      task_window.title(" Add Tasks ")
      task_window.geometry("300x300")
      
      def addTaskTopLevel():  
              title= entry.get().strip()
                  
              if title:
                    
                tm.addTask(title) #add task
                    
                entry.delete(0, tk.END) #clear the entry
                    
                all_tasks ="\n".join(tm.getTasks()) #to display the list thats contains all the task in tm
                    
                display_label.config(text=all_tasks)
      
      tk.Label(task_window,
                     text="Add New Task!",
                     bg="white",
                     fg="Black").pack(padx=5,pady=5)
      
      
      
      
      entry=tk.Entry(task_window,
                       bg="#FDF4D2"
                       )
      entry.pack()
      
      button=tk.Button(task_window,
                           text="Add Task!!!!!!",
                           bg="#28E4C4",
                           fg="#071A2F",
                           command= addTaskTopLevel)
      button.pack()
      
      display_label=tk.Label(task_window,
                         text="       ",
                         bg="#FDF4D2",
                         fg="#AF719D")
      display_label.pack(padx=5 ,pady=5)
      
      
      
       
      
    
  addTaskButton= tk.Button(window,
                           text="Add Task",
                           bg="#C8DFDB",
                           fg="#3368A0",
                           command= open_task_window)
  addTaskButton.pack()
  
  

    
    
  
  
  
  
  
  
  

    