from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title('Digital SoftUni Clock')


def clock():
    tick = strftime(" - %H:%M:%S - ")
    label.config(text=tick)
    label.after(1000, clock)


label = Label(root, font=('sans', 80), background='black', foreground='purple')
label.pack(anchor='center')
clock()
mainloop()