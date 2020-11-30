from tkinter import *



def submit(event=None):
    Label(root, text="Addition is         : ").grid(row=3, column=0)
    e = Entry(root)
    e.grid(row=3, column=1)
    e.insert(END, int(e1.get()) + int(e2.get()))


def reset():
    e1.delete(0, len(str(e1.get())))
    e2.delete(0, len(str(e2.get())))


root = Tk()
root.geometry("440x300")
root.config(bg="light yellow")
root.title("Events")

Label(root, text="Enter First Number  : ").grid(row=0, column=0)
e1 = Entry(root)
e1.grid(row=0, column=1)

Label(root, text="Enter Second Number : ").grid(row=1, column=0)
e2 = Entry(root)
e2.grid(row=1, column=1)
e2.bind("<Return>", submit)

b1 = Button(root, text="Submit", command=submit)
b1.grid(row=2, column=0)
b1.bind("<Return>", submit)

b2 = Button(root, text="Reset", command=reset)
b2.grid(row=2, column=1)

root.mainloop()
