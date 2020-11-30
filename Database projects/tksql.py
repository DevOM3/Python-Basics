from tkinter import *
import sqlite3

# con.execute("CREATE TABLE STUD(ROLL NUMBER(6) PRIMARY KEY, NAME VARCHAR(20), CITY VARCHAR(20))")


def add_data():
    con = sqlite3.connect("student_db")
    con.execute("INSERT INTO STUD (ROLL, NAME, CITY) VALUES (?, ?, ?)", (int(e1.get()), e2.get(), e3.get()))
    con.commit()
    con.close()
    print("Data added")


def update_data():
    con = sqlite3.connect("student_db")
    con.execute(f"UPDATE STUD SET CITY='{str(e3.get())}' WHERE ROLL={int(e1.get())}")
    con.commit()
    con.close()
    print("Data Updated")


def delete_data():
    con = sqlite3.connect("student_db")
    con.execute(f"DELETE FROM STUD WHERE ROLL = {(int(e1.get()))}")
    con.commit()
    con.close()
    print("Data deleted")


def reset_data():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)


root = Tk()

lbl = Label(root, text="Student Roll Number : ", font="lucida 11")
lbl.place(x=3, y=10)

e1 = Entry(root, font="lucida 11")
e1.place(x=150, y=10)

lbl1 = Label(root, text="Student Name        : ", font="lucida 11")
lbl1.place(x=3, y=50)

e2 = Entry(root, font="lucida 11")
e2.place(x=150, y=50)

lbl2 = Label(root, text="Student City       : ", font="lucida 11")
lbl2.place(x=3, y=90)

e3 = Entry(root, font="lucida 11")
e3.place(x=150, y=90)

add = Button(root, text="Add", padx=10, pady=5, command=add_data)
add.place(x=3, y=130)

update = Button(root, text="Update", padx=10, pady=5, command=update_data)
update.place(x=63, y=130)

delete = Button(root, text="Delete", padx=10, pady=5, command=delete_data)
delete.place(x=143, y=130)

reset = Button(root, text="Reset", padx=10, pady=5, command=reset_data)
reset.place(x=223, y=130)

root.mainloop()
