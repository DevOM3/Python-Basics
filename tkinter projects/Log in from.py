from tkinter import *
from tkinter.messagebox import showinfo, showerror, showwarning


def login(event=None):
    flag = 10
    file = open("Log in info.txt", 'r')
    f = file.readlines()
    for i in f:
        lst = list(i.split())
        if id_entry.get() == lst[0] and pass_entry.get() == lst[1]:
            flag = 1
            file.close()
            break
        else:
            flag = 0
            file.close()

    if flag == 1:
        showinfo("Log in Page", "Logged in Successfully")
    elif flag == 0:
        showerror("Log in Page", "User is not Registered")


def reset(event=None):
    id_entry.delete(0, END)
    pass_entry.delete(0, END)


def signup(event=None):
    file = open("Log in info.txt", 'r+')
    if id_entry.get() in file.read():
        showwarning("Sign up", "User ID already exit, Try using different one ")
    else:
        file.write(id_entry.get() + " " + pass_entry.get() + "\n")
        showinfo("Sign up page", "Signed up Successfully")
    file.close()


root = Tk()
root.title("Log in Form")
root.geometry("300x400")

Label(root, text="Enter User ID  ", font="lucida 10 bold").place(x=20, y=40)
id_entry = Entry(root, font="9", width=28)
id_entry.place(x=20, y=65)

Label(root, text="Enter Password ", font="lucida 10 bold").place(x=20, y=100)
pass_entry = Entry(root, show="*", font="9", width=28)
pass_entry.place(x=20, y=125)
pass_entry.bind("<Return>", login)

log_b = Button(root, text="Log in", padx=7, pady=3, bd=3, relief=RAISED, command=login)
log_b.place(x=75, y=170)
log_b.bind("<Return>", login)

reset_b = Button(root, text="Reset", padx=8, pady=3, bd=3, relief=RAISED, command=reset)
reset_b.place(x=150, y=170)
reset_b.bind("<Return>", reset)

Label(root, text="New User ? ").place(x=80, y=220)
sign_up = Button(root, text="Sign Up", fg="black", bg="white", command=signup)
sign_up.place(x=150, y=220)
sign_up.bind("<Return>", signup)

root.mainloop()
