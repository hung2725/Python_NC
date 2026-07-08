# Phạm Thế Hùng -2374802010164
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Pham THe Hung - GUI")  

# Tạo style riêng cho LabelFrame
style = ttk.Style()
style.configure("Custom.TLabelframe.Label", foreground="Blue")

# Tạo LabelFrame chính
mighty = ttk.LabelFrame(win, text='TheHung', style="Custom.TLabelframe")
mighty.grid(column=0, row=0, padx=8, pady=4)

# Label "Enter a name:"
a_label = ttk.Label(mighty, text="Enter a name:")
a_label.grid(column=0, row=0, sticky=tk.W)

# Modified Button Click Function
def click_me(): 
    action.configure(text='Hello ' + name.get() + ' ' + number_chosen.get())

# Adding a Textbox Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky=tk.W)   # sticky để giống hình

# Label "Choose a number:"
ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0, sticky=tk.W)

# Combobox
number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1, sticky=tk.W)
number_chosen.current(0)

# Adding a Button
action = ttk.Button(mighty, text="Click Me!", command=click_me)   
action.grid(column=2, row=1, sticky=tk.W)

# Creating three checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)                   

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W)                     

# GUI Callback function 
def checkCallback(*ignoredArgs):
    if chVarUn.get(): check3.configure(state='disabled')
    else:             check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:             check2.configure(state='normal') 

# trace the state of the two checkbuttons
chVarUn.trace('w', lambda *args: checkCallback())    
chVarEn.trace('w', lambda *args: checkCallback())   

# Using a scrolled Text control    
scrol_w  = 30
scrol_h  =  3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=5, columnspan=3, sticky="WE")   # sticky để giãn ngang   

# Radiobuttons
colors = ["Blue", "Gold", "Red"]   
def radCall():
    radSel = radVar.get()
    if   radSel == 0: win.configure(background=colors[0])
    elif radSel == 1: win.configure(background=colors[1])
    elif radSel == 2: win.configure(background=colors[2])

radVar = tk.IntVar()
radVar.set(99)                                 
for col in range(3):                             
    curRad = tk.Radiobutton(mighty, text=colors[col], variable=radVar, 
                            value=col, command=radCall)          
    curRad.grid(column=col, row=6, sticky=tk.W)             

# Create a container to hold labels
buttons_frame = ttk.LabelFrame(mighty, text='Labels in a Frame - TheHung', style="Custom.TLabelframe")
buttons_frame.grid(column=0, row=7, columnspan=3, padx=1, pady=4, sticky=tk.W)

# Place labels into the container element
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)

name_entered.focus()      # Place cursor into name Entry

#======================
# Start GUI
#======================
win.mainloop()
