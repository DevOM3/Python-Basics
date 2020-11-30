
from tkinter import *
import tkinter.messagebox


base = Tk()
base.geometry("300x300")
base.title("Using Menubar")

def exitmethod():
    m = tkinter.messagebox.askyesno("Confirm Exit", "Are you sure you want to exit?")
    st = "Type is",type(m)," and value is ",m
    tkinter.messagebox.showinfo("Decision", st)

    if m==1:
        base.destroy()
    if m==0:
        tkinter.messagebox.showinfo("Decision","Good Decision, continue in application")


def newproj():
    tkinter.messagebox.showinfo("Create Project","Good Choice, Create New Project now..")

menubar = Menu(base)

m1 = Menu(menubar)
m1.add_command(label="New Project",command=newproj)
m1.add_command(label="New")
m1.add_command(label="New Scratch File")
m1.add_separator()
m1.add_command(label="Save")
m1.add_command(label="Save As")
m1.add_separator()
m1.add_command(label="Exit",command=exitmethod)
menubar.add_cascade(label="File",menu=m1)

m2 = Menu(menubar)
m2.add_command(label="Undo")
m2.add_command(label="Redo")
m2.add_separator()
m2.add_command(label="Cut")
m2.add_command(label="Copy")
m2.add_command(label="Paste")
menubar.add_cascade(label="Edit",menu=m2)

m3 = Menu(menubar)
m3.add_command(label="Find Action")
m3.add_separator()
m3.add_command(label="Find")
m3.add_command(label="Getting Help")
menubar.add_cascade(label="Help",menu=m3)

base.config(menu=menubar)
# is required to set menubar
# we cannot pack() or grid() menu and menubar

base.mainloop()

'''
following code will add m2 as submenu of m1
m2 = Menu(m1)
m2.add_command(label="Undo")
m2.add_command(label="Redo")
m2.add_separator()
m2.add_command(label="Cut")
m2.add_command(label="Copy")
m2.add_command(label="Paste")
m1.add_cascade(label="Edit",menu=m2)
'''


