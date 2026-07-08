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

#===================================================================
class ToolTip(object):
    def __init__(self, widget, tip_text=None):
        self.widget = widget
        self.tip_text = tip_text
        widget.bind('<Enter>', self.mouse_enter)
        widget.bind('<Leave>', self.mouse_leave)
        self.tip_window = None

    def mouse_enter(self, _event):
        self.show_tooltip()

    def mouse_leave(self, _event):
        self.hide_tooltip()

    def show_tooltip(self):
        if self.tip_text:
            x_left = self.widget.winfo_rootx()
            y_top = self.widget.winfo_rooty() - 18
            self.tip_window = tk.Toplevel(self.widget)
            self.tip_window.overrideredirect(True)
            self.tip_window.geometry("+%d+%d" % (x_left, y_top))
            label = tk.Label(
                self.tip_window, text=self.tip_text, justify=tk.LEFT,
                background="#ffffe0", relief=tk.SOLID, borderwidth=1,
                font=("tahoma", "8", "normal")
            )
            label.pack(ipadx=1)

    def hide_tooltip(self):
        if self.tip_window:
            self.tip_window.destroy()
            self.tip_window = None


#===================================================================
class OOP():
    def __init__(self):
        self.win = tk.Tk()
        ToolTip(self.win, 'Hello GUI_PhamTheHung')
        self.win.title("Pham The Hung - GUI")
        self.create_widgets()

    def click_me(self):
        self.action.configure(text='Hello ' + self.name.get() + ' ' + self.number_chosen.get())

    def _spin(self):
        value = self.spin2.get()
        print(value)
        self.scr.insert(tk.INSERT, value + '\n')

    def _spin2(self):
        value = self.spin2.get()
        print(value)
        self.scr.insert(tk.INSERT, value + '\n')

    def checkCallback(self, *ignoredArgs):
        if self.chVarUn.get(): self.check3.configure(state='disabled')
        else:                  self.check3.configure(state='normal')
        if self.chVarEn.get(): self.check2.configure(state='disabled')
        else:                  self.check2.configure(state='normal')

    def radCall(self):
        radSel = self.radVar.get()
        if   radSel == 0: self.buttons_frame.configure(bg="blue")
        elif radSel == 1: self.buttons_frame.configure(bg="gold")
        elif radSel == 2: self.buttons_frame.configure(bg="red")

    def run_progressbar(self):
        self.progress_bar["maximum"] = 100
        for i in range(101):
            sleep(0.05)
            self.progress_bar["value"] = i
            self.progress_bar.update()
        self.progress_bar["value"] = 0

    def start_progressbar(self):
        self.progress_bar.start()

    def stop_progressbar(self):
        self.progress_bar.stop()

    def progressbar_stop_after(self, wait_ms=1000):
        self.win.after(wait_ms, self.progress_bar.stop)

    def usingGlobal(self):
        global GLOBAL_CONST
        print(GLOBAL_CONST)
        GLOBAL_CONST = 777
        print(GLOBAL_CONST)

    def _quit(self):
        self.win.quit()
        self.win.destroy()

    def _msgBox(self):
        answer = msg.askyesnocancel("Python Message Multi Choice Box(Pham The Hung)", 
            "Are you sure you really wish to do this?\nPham The Hung")
        print(answer)

    def create_widgets(self):
        tabControl = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tabControl)
        tabControl.add(tab1, text='Tab 1')
        tab2 = ttk.Frame(tabControl)
        tabControl.add(tab2, text='Tab 2')
        tabControl.pack(expand=1, fill="both")

        self.mighty = tk.LabelFrame(tab1, text=' The Hung ', fg="blue")
        self.mighty.grid(column=0, row=0, padx=8, pady=4)

        a_label = ttk.Label(self.mighty, text="Enter a name:")
        a_label.grid(column=0, row=0, sticky='W')

        self.name = tk.StringVar()
        name_entered = ttk.Entry(self.mighty, width=12, textvariable=self.name)
        name_entered.grid(column=0, row=1, sticky='W')
        self.action = ttk.Button(self.mighty, text="Click Me!", command=self.click_me)
        self.action.grid(column=2, row=1)
        ttk.Label(self.mighty, text="Choose a number:").grid(column=1, row=0)

        number = tk.StringVar()
        self.number_chosen = ttk.Combobox(self.mighty, width=12, textvariable=number, state='readonly')
        self.number_chosen['values'] = (1, 2, 4, 42, 100)
        self.number_chosen.grid(column=1, row=1)
        self.number_chosen.current(0)

        self.spin = Spinbox(self.mighty, values=(1, 2, 4, 42, 100), width=5, bd=8, command=self._spin)
        self.spin.grid(column=0, row=2)
        ToolTip(self.spin, 'This is a Spinbox control')

        self.spin2 = Spinbox(self.mighty, values=(0, 50, 100), width=5, bd=9, command=self._spin2, relief=tk.RIDGE)
        self.spin2.grid(column=1, row=2)
        ToolTip(self.spin2, 'This is a Spinbox control')

        scrol_w = 30
        scrol_h = 3
        self.scr = scrolledtext.ScrolledText(self.mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scr.grid(column=0, row=3, sticky='WE', columnspan=3)

        self.mighty2 = tk.LabelFrame(tab2, text=' The Snake - The Hung ', fg="blue")
        self.mighty2.grid(column=0, row=0, padx=8, pady=4)

        self.chVarDis = tk.IntVar()
        check1 = tk.Checkbutton(self.mighty2, text="Disabled", variable=self.chVarDis, state='disabled')
        check1.select()
        check1.grid(column=0, row=0, sticky=tk.W)

        self.chVarUn = tk.IntVar()
        self.check2 = tk.Checkbutton(self.mighty2, text="UnChecked", variable=self.chVarUn)
        self.check2.deselect()
        self.check2.grid(column=1, row=0, sticky=tk.W)

        self.chVarEn = tk.IntVar()
        self.check3 = tk.Checkbutton(self.mighty2, text="Enabled", variable=self.chVarEn)
        self.check3.deselect()
        self.check3.grid(column=2, row=0, sticky=tk.W)

        self.chVarUn.trace('w', lambda *args: self.checkCallback())
        self.chVarEn.trace('w', lambda *args: self.checkCallback())

        colors = ["Blue", "Gold", "Red"]
        self.radVar = tk.IntVar()
        self.radVar.set(99)
        for col in range(3):
            curRad = tk.Radiobutton(self.mighty2, text=colors[col], variable=self.radVar, value=col, command=self.radCall)
            curRad.grid(column=col, row=1, sticky=tk.W)
            ToolTip(curRad, 'This is a Radiobutton control')

        self.progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
        self.progress_bar.grid(column=0, row=3, pady=2)

        self.buttons_frame = tk.LabelFrame(self.mighty2, text='ProgressBar', fg='blue')
        self.buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)


        ttk.Button(self.buttons_frame, text=" Run Progressbar   ", command=self.run_progressbar).grid(column=0, row=0, sticky='W')
        ttk.Button(self.buttons_frame, text=" Start Progressbar  ", command=self.start_progressbar).grid(column=0, row=1, sticky='W')
        ttk.Button(self.buttons_frame, text=" Stop immediately ", command=self.stop_progressbar).grid(column=0, row=2, sticky='W')
        ttk.Button(self.buttons_frame, text=" Stop after second ", command=self.progressbar_stop_after).grid(column=0, row=3, sticky='W')

        for child in self.buttons_frame.winfo_children():
            child.grid_configure(padx=2, pady=2)

        for child in self.mighty2.winfo_children():
            child.grid_configure(padx=8, pady=2)

        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)

        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=self._msgBox)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        # self.win.iconbitmap("pyc.ico")

        self.usingGlobal()
        print('GLOBAL_CONST:', GLOBAL_CONST)
        name_entered.focus()
        self.win.iconbitmap("pyc.ico") 


#======================
# Start GUI
#======================
oop = OOP()
oop.win.mainloop()
