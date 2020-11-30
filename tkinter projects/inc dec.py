from tkinter import *


def click(event):
    txt = event.widget.cget("text")
    if txt == " - ":
        no = lbl.cget("text")
        no = no - 1
        lbl.config(text=no)
    elif txt == " + ":
        no = lbl.cget("text")
        no = no + 1
        lbl.config(text=no)


root = Tk()

bm = Button(root, text=" - ", font="21")
bm.grid(row=0, column=0, padx=7)
bm.bind("<Button-1>", click)
lbl = Label(root, text=0, font="21")
lbl.grid(row=0, column=1, padx=7)
bp = Button(root, text=" + ", font="21")
bp.grid(row=0, column=2, padx=7)
bp.bind("<Button-1>", click)

root.mainloop()
