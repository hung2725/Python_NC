import tkinter as tk

# Create instance of tkinter
win = tk.Tk()
# assign tkinter variable to strdata variable
strData = tk.StringVar()
# set strData variable
strData.set("Phạm Thế Hùng_Hello StringVar")
#get value of strData variable
varData = strData.get()
# print out curent value ò strData
print(varData)
# Print out the default tkinter variable values
print(tk.IntVar())
print(tk.DoubleVar())
print(tk.BooleanVar())
