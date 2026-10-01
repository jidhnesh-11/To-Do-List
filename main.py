# root of window!
import tkinter as tk
from tkinter import ttk

import ui 
import auth_ui
import auth_db

# initialize the db
auth_db.init_db()

## main window ##
window=tk.Tk()
window.title("DoDoingDone")
window.geometry("850x550")
#window.attributes('-fullscreen', True)
window.state('zoomed')
window.withdraw() # hide !!

login_window=  tk.Toplevel(window)
login_window.title("Log In / Sign In")
login_window.geometry("500x400")

auth_ui.showAuthWin(login_window, window)

window.mainloop() 