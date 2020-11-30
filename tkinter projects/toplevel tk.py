from tkinter import *

root = Tk()
root.title("Root")


def click():
    tl = Toplevel(root)
    tl.title("TopLevel")

    tl.mainloop()


Button(root, text="Toplevel", command=click).pack()



root.mainloop()
