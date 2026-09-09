import tkinter as tk

import themes as th 
import auth_db as audb
import ui 

def showAuthWin(login_window, window):
  
  current_mode= "signup"
  
  def update_view_signup():
    nonlocal current_mode
    current_mode = "signup"
    
    signup_label.config(text="Sign UP")
    confirm_btn.config(text= "Sign up!")
    
    
    
  def update_view_login():
    nonlocal current_mode
    current_mode = "login"
    signup_label.config(text="Log IN")
    confirm_btn.config(text= "Log in!")
    
    
    
  def confirm_action():
    
    username = username_entry.get().strip()
    password = pass_entry.get().strip()
    
    if not username or not password:
      msg_box.config(text="Please fill all the fileds")
      return # not to fall through when usrname and pass are empty!! :-(
      
    if current_mode == "signup":
      
      success , message = audb.signup(username, password)  #unpacking the tuple eg audb.signup retruns True or Flase and a message like successful etc
      msg_box.config(text=message)
      
      
      if success:
        username_entry.delete(0, tk.END) # clear the entry
        pass_entry.delete(0, tk.END) #clear the entry!
        update_view_login() # go to login
      
    else:
      
      if(audb.login(username,password)):
        msg_box.config(text="Login Successful!")
        login_window.destroy()
        window.deiconify()
        
        ui.showWidget(window, username)
          
      else:
        msg_box.config(text="Invalid credentials.")
      
    
    
    
    
  main_frame = tk.Frame(login_window,
                        bg= th.content_BG,
                        padx=5,
                        pady=50)
  main_frame.pack()
  
  signup_label = tk.Label(main_frame,
                          text="Sign Up",
                          font=(th.font_name, 15, "bold"),
                          bg= th.content_BG)
  signup_label.grid(row=0, column=1, padx=10, pady=10)
  
  signup_btn = tk.Button(main_frame,
                         text="Sign UP",
                         command= update_view_signup)
  signup_btn.grid(row=1, column=1, padx=5, pady=5)
  
  login_btn = tk.Button(main_frame,
                         text="Log IN",
                         command= update_view_login)
  login_btn.grid(row=1, column=2, padx=5, pady=5)
  
  username_label = tk.Label(main_frame,
                            text="Username: ")
  username_label.grid(row= 2, column = 0, padx=10, pady=10)
  
  username_entry = tk.Entry(main_frame)
  username_entry.grid(row= 2, column = 1, padx=10, pady=10)
  
  
  pass_label = tk.Label(main_frame,
                              text="Password: ")
  pass_label.grid(row= 3, column = 0, padx=10, pady=10)
  
  pass_entry = tk.Entry(main_frame)
  pass_entry.grid(row= 3, column = 1, padx=10, pady=10)
  
  confirm_btn = tk.Button(main_frame,
                          text="Sign up!",
                          command=confirm_action)
  confirm_btn.grid(row=4 , column=1, padx=10, pady=10)
  
  msg_box = tk.Label(main_frame,
                     text=".")
  msg_box.grid(row=5, column = 1, padx=10, pady=10)
  