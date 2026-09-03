# root of window!

import tkinter as tk
from tkinter import ttk
import ui 

window=tk.Tk()
window.title("DoDoingDone")
window.geometry("900x500")
#window.attributes('-fullscreen', True)
window.state('zoomed')

ui.showWidget(window) #passes the window into ui
tk.mainloop()