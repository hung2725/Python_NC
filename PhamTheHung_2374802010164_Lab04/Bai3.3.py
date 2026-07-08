#Phạm Thế Hùng_2374802010164
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
from time import sleep         # careful - this can freeze the GUI

GLOBAL_CONST = 42

# Create instance
win = tk.Tk()   
win.title("Pham The Hung - GUI")  

tabControl = ttk.Notebook(win)          
tab1 = ttk.Frame(tabControl)            
tabControl.add(tab1, text='Tab 1')      
tab2 = ttk.Frame(tabControl)            
tabControl.add(tab2, text='Tab 2')      
tabControl.pack(expand=1, fill="both")  

# LabelFrame tab1
mighty = tk.LabelFrame(tab1, text=' The Hung ', fg="blue")
mighty.grid(column=0, row=0, padx=8, pady=4)

a_label = ttk.Label(mighty, text="Enter a name:")
a_label.grid(column=0, row=0, sticky='W')

def click_me(): 
    action.configure(text='Hello ' + name.get() + ' ' + number_chosen.get())

name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')               
action = ttk.Button(mighty, text="Click Me!", command=click_me)   
action.grid(column=2, row=1)                                
ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)

number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

# Spinbox callback 
def _spin():
    value = spin2.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')   # dùng scr đúng tên biến

# Adding a Spinbox widget
spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=8,  command=_spin)
spin.grid(column=0, row=2)

# Spinbox2 callback function 
def _spin2():
    value = spin2.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')

# Adding a second Spinbox widget
spin2 = Spinbox(mighty, values=(0, 50, 100), width=5, bd=9,  command=_spin2, relief=tk.RIDGE)
spin2.grid(column=1, row=2)


scrol_w  = 30
scrol_h  =  3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=3, sticky='WE', columnspan=3)   # chuyển xuống row=3                  

# Tab2
mighty2 = tk.LabelFrame(tab2, text=' The Snake - The Hung ', fg="blue")
mighty2.grid(column=0, row=0, padx=8, pady=4)

# Checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=0, sticky=tk.W)                   

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=0, sticky=tk.W)                   

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=0, sticky=tk.W)                     

def checkCallback(*ignoredArgs):
    if chVarUn.get(): check3.configure(state='disabled')
    else:             check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:             check2.configure(state='normal') 

chVarUn.trace('w', lambda *args : checkCallback())    
chVarEn.trace('w', lambda *args : checkCallback())   

# Radiobuttons
colors = ["Blue", "Gold", "Red"]   

def radCall():
    radSel = radVar.get()
    if   radSel == 0: buttons_frame.configure(bg="blue")   # đổi nền xanh
    elif radSel == 1: buttons_frame.configure(bg="gold")   # đổi nền vàng
    elif radSel == 2: buttons_frame.configure(bg="red")    # đổi nền đỏ

radVar = tk.IntVar()
radVar.set(99)                                 
for col in range(3):                             
    curRad = tk.Radiobutton(mighty2, text=colors[col], variable=radVar, 
                            value=col, command=radCall)          
    curRad.grid(column=col, row=1, sticky=tk.W)             # row=6    
# Add a Progressbar to Tab 2
progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
progress_bar.grid(column=0, row=3, pady=2)  
def run_progressbar():
    progress_bar["maximum"] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = i   
        progress_bar.update()      
    progress_bar["value"] = 0       
def start_progressbar():
    progress_bar.start()
def stop_progressbar():
    progress_bar.stop()
def progressbar_stop_after(wait_ms=1000):    
    win.after(wait_ms, progress_bar.stop)
# Create a container to hold buttons
buttons_frame = ttk.LabelFrame(mighty2, text=' ProgressBar ')
buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)        

# Add Buttons for Progressbar commands
ttk.Button(buttons_frame, text=" Run Progressbar   ", command=run_progressbar).grid(column=0, row=0, sticky='W')  
ttk.Button(buttons_frame, text=" Start Progressbar  ", command=start_progressbar).grid(column=0, row=1, sticky='W')  
ttk.Button(buttons_frame, text=" Stop immediately ", command=stop_progressbar).grid(column=0, row=2, sticky='W')  
ttk.Button(buttons_frame, text=" Stop after second ", command=progressbar_stop_after).grid(column=0, row=3, sticky='W') 
for child in buttons_frame.winfo_children():  
    child.grid_configure(padx=2, pady=2) 
 
for child in mighty2.winfo_children():  
    child.grid_configure(padx=8, pady=2) 
# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()

# Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)  # ⬅ nhấn Exit thoát app
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)

def _msgBox():
   # msg.showinfo('Python Message Info Box', 'A Python GUI created using tkinter:\nPham The Hung The year is 2022.') 
   # msg.showwarning('Python Message Warning Box', 'A Python GUI created  using tkinter:' '\nWarning: There might be a bug in this code.\nPham The Hung')
   #msg.showerror('Python Message Error Box', 'A Python GUI created  using tkinter:''\nError: Houston ~ we DO have a serious PROBLEM!''\nPham The Hung')
   answer = msg.askyesnocancel("Python Message Multi Choice Box(Pham The Hung)", "Are you sure you really wish to do this?"'\nPham The Hung')
   print(answer)
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msgBox)  # Gắn hàm _msgBox
menu_bar.add_cascade(label="Help", menu=help_menu)

# Change the main windows icon
win.iconbitmap("pyc.ico")

# #print the global works
# print(GLOBAL_CONST)

def usingGlobal():
    global GLOBAL_CONST
    print(GLOBAL_CONST)
    GLOBAL_CONST = 777
    print(GLOBAL_CONST)


# call function
usingGlobal()

# call the global from outside the function
print('GLOBAL_CONST:', GLOBAL_CONST)

name_entered.focus()      
win.mainloop()