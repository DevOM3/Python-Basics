from tkinter import *
import sqlite3

con = sqlite3.connect("trialdb")
cur = con.cursor()
c = cur.execute("SELECT * FROM trial")

i = 0


def click(event):
    global i
    op = event.widget.cget("text")
    cr = cur.execute("SELECT * FROM trial")
    ls = cr.fetchall()
    if op == "First":
        name.config(text=ls[0][0])
        ph_no.config(text=ls[0][1])
        city.config(text=ls[0][2])
        i = 0

    elif op == "Last":
        name.config(text=ls[len(ls) - 1][0])
        ph_no.config(text=ls[len(ls) - 1][1])
        city.config(text=ls[len(ls) - 1][2])
        i = (len(ls) - 2)
    elif op == "<< Prev":
        name.config(text=ls[i][0])
        ph_no.config(text=ls[i][1])
        city.config(text=ls[i][2])
        i = i - 1
        if i < 0:
            i = 0
    elif op == "Next >>":
        name.config(text=ls[i][0])
        ph_no.config(text=ls[i][1])
        city.config(text=ls[i][2])
        i = i + 1
        if i > (len(ls) - 1):
            i = (len(ls) - 1)


lst = c.fetchall()
root = Tk()
root.geometry("275x421")
root.title("Database Switching module")

Label(root, text="Database", font="ariel 35 bold").place(x=0, y=0)

name_lbl = Label(root, text="Name       :", font="lucida 15")
name_lbl.place(x=3, y=101)

name = Label(root, text=lst[0][0], font="lucida 15")
name.place(x=151, y=101)

ph_no_lbl = Label(root, text="Phone no. :", font="lucida 15")
ph_no_lbl.place(x=3, y=151)

ph_no = Label(root, text=lst[0][1], font="lucida 15")
ph_no.place(x=151, y=151)

city_lbl = Label(root, text="City          :", font="lucida 15")
city_lbl.place(x=3, y=201)

city = Label(root, text=lst[0][2], font="lucida 15")
city.place(x=151, y=201)

prev = Button(root, text="<< Prev", font="lucida 11")
prev.place(x=3, y=271)
prev.bind("<Button-1>", click)

first = Button(root, text="First", font="lucida 11")
first.place(x=81, y=271)
first.bind("<Button-1>", click)

last = Button(root, text="Last", font="lucida 11")
last.place(x=141, y=271)
last.bind("<Button-1>", click)

next_info = Button(root, text="Next >>", font="lucida 11")
next_info.place(x=195, y=271)
next_info.bind("<Button-1>", click)

root.mainloop()
