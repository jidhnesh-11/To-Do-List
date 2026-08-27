# root of window!

import tkinter as tk
from tkinter import ttk
import ui 

window=tk.Tk()

window.geometry("500x500")

ui.showWidget(window) #passes the window into ui
tk.mainloop()