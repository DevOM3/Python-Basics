from tkinter import *
from tkinter.messagebox import askyesno as ayn
from datetime import date
dt = date.today()

root = Tk()
root.geometry("340x320")


def click():
    yn = ayn("Are you Sure", "Do you want to select this option")
    if yn == YES:
        print(var.get())
    else:
        # operations()
        print("No")



var = IntVar()
var.set(0)
Label(text="Food Ordering Software", font="arial 21 bold", pady=10).pack(anchor=W)
rb = Radiobutton(root, text="Search food", variable=var, value=1, padx=5, pady=5).pack(anchor=W)
rb = Radiobutton(root, text="Hotels and Menus", variable=var, value=2, padx=5, pady=5).pack(anchor=W)
rb = Radiobutton(root, text="Order History", variable=var, value=3, padx=5, pady=5).pack(anchor=W)
rb = Radiobutton(root, text="Edit Account", variable=var, value=4, padx=5, pady=5).pack(anchor=W)
rb = Radiobutton(root, text="Create Account", variable=var, value=5, padx=5, pady=5).pack(anchor=W)
rb = Radiobutton(root, text="Exit", variable=var, value=6, padx=5, pady=5).pack(anchor=W)
b = Button(root, text="Submit", command=click).pack(anchor=W, padx=5, pady=5)

root.mainloop()
