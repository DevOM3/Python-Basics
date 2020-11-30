from tkinter import *

root = Tk()
root.geometry("744x735")
root.minsize(744, 735)
root.maxsize(744, 735)
root.title("Chess")

for r in range(0, 8):
    for c in range(0, 8):
        if r == 0 and c == 0 or r == 0 and c == 2 or r == 0 and c == 4 or r == 0 and c == 6 or \
                r == 1 and c == 1 or r == 1 and c == 3 or r == 1 and c == 5 or r == 1 and c == 7 or\
                r == 2 and c == 0 or r == 2 and c == 2 or r == 2 and c == 4 or r == 2 and c == 6 or\
                r == 3 and c == 1 or r == 3 and c == 3 or r == 3 and c == 5 or r == 3 and c == 7 or \
                r == 4 and c == 0 or r == 4 and c == 2 or r == 4 and c == 4 or r == 4 and c == 6 or \
                r == 5 and c == 1 or r == 5 and c == 3 or r == 5 and c == 5 or r == 5 and c == 7 or \
                r == 6 and c == 0 or r == 6 and c == 2 or r == 6 and c == 4 or r == 6 and c == 6 or \
                r == 7 and c == 1 or r == 7 and c == 3 or r == 7 and c == 5 or r == 7 and c == 7:
            b = Button(root, bg="black", width=11, height=5, activebackground="gray21", bd=5, relief=RAISED)
            b.grid(row=r, column=c)
        else:
            b = Button(root, bg="white", width=11, height=5, activebackground="gainsboro", bd=5, relief=RAISED)
            b.grid(row=r, column=c)


root.mainloop()
