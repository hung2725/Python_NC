#Phạm Thế Hùng_2374802010164
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
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
scrol_w  = 30
scrol_h  =  3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=2, sticky='WE', columnspan=3)                       
# Tab2
mighty2 = tk.LabelFrame(tab2, text=' The Snake - The Hung ', fg="blue")
mighty2.grid(column=0, row=0, padx=8, pady=4)
# Checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)                   
chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)                   
chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W)                     
def checkCallback(*ignoredArgs):
    if chVarUn.get(): check3.configure(state='disabled')
    else:             check3.configure(state='normal')
    if chVarEn.get(): check2.configure(state='disabled')
    else:             check2.configure(state='normal') 
chVarUn.trace('w', lambda *args : checkCallback())    
chVarEn.trace('w', lambda *args : checkCallback())   
# Radiobuttons
colors = ["Blue", "Gold", "Red"]   
# Frame chứa labels (sẽ đổi màu nền theo Radio)
buttons_frame = tk.LabelFrame(mighty2, text=' Labels in a Frame - The Hung ', fg="blue")
buttons_frame.grid(column=0, row=7)        
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)
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
    curRad.grid(column=col, row=6, sticky=tk.W)             
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
# Display a Message Box
def _msgBox():
   # msg.showinfo('Pham The Hung Python Message Info Box', 'A Python GUI created using tkinter:\nPham The Hung The year is 2022.') 
   # msg.showwarning('Pham The Hung Python Message Warning Box', 'A Python GUI created  using tkinter:' '\nWarning: There might be a bug in this code.\nPham The Hung')
   #msg.showerror('Pham The Hung Python Message Error Box', 'A Python GUI created  using tkinter:''\nError: Houston ~ we DO have a serious PROBLEM!''\nPham The Hung')
   answer = msg.askyesnocancel("Pham The Hung Python Message Multi Choice Box", "Are you sure you really wish to do this?"'\nPham The Hung')
   print(answer)
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=_msgBox)  # Gắn hàm _msgBox
menu_bar.add_cascade(label="Help", menu=help_menu)

name_entered.focus()      
win.mainloop()
