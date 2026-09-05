# root of window!

import tkinter as tk
from tkinter import ttk
import ui 

window=tk.Tk()
window.title("DoDoingDone")
window.geometry("850x550")
#window.attributes('-fullscreen', True)
window.state('zoomed')

ui.showWidget(window) #passes the window into ui
tk.mainloop() 