# Phạm Thế Hùng_2374802010164

import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Phạm Thế Hùng - GUI")

# Adding a Label
ttk.Label(win, text="A Label").grid(column=0, row=0) 

win.mainloop()