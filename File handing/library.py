from datetime import date

print("Library\n\n")


def search_book(so, s):
    def prnt():
        print(f"\nBook ID : {ls1[1]}\nBook Name : {ls1[0]}\nAuthor : {ls1[2]}\n")
    rb = open("book.txt", 'r')
    rl = rb.readlines()
    for j in rl:
        ls1 = list(j.split())
        if so == 1:
            if s == ls1[0]:
                prnt()
        if so == 2:
            if s == ls1[1]:
                prnt()
        if so == 3:
            if s == ls1[2]:
                prnt()


while True:
    print("Enter which operation you want to do for the library among the following operation number:-\n")
    action = int(input("1. Issue Book\n2. Return Book\n3. Not returned Books\n4. Personal History\n5. Add new Book\n"
                       "6. Add new Student\n7. All Books\n8. Search Book\n10. Exit\n"
                       "Enter your choice :-\t"))

    if action == 1:
        en = input("Enter your Enrollment no :- ")
        bid = input("Enter the Book ID :- ")

        stud = open("stud_info.txt", 'r')
        book = open("book.txt", 'r')

        if en in stud.read() and bid in book.read():
            return_stat = "No"
            return_dt = None
            issue = open("issue_book.txt", 'a')
            issue.write(f"{bid} {en} {date.today()} {return_stat} {return_dt}\n")
            issue.close()
            print("Data saved")
        else:
            print("Data not found\n")

    elif action == 2:
        bk = input("Enter the Book ID :- ")
        ob = open("issue_book.txt", 'r')
        data = ob.readlines()
        i = 0
        for d in data:
            ls = list(d.split(" "))
            if ls[3] == "No" and ls[4] == "None\n" and ls[0] == bk:
                ls[3] = "Yes"
                ls[4] = str(date.today()) + "\n"
                data1 = f"{ls[0]} {ls[1]} {ls[2]} {ls[3]} {ls[4]}"
                data[i] = data1
            i = i + 1
        ob.close()
        ob = open("issue_book.txt", 'w')
        ob.writelines(data)
        ob.close()

    elif action == 3:
        ret = open("issue_book.txt", 'r')
        l_ret = ret.readlines()
        i = 0
        for r in l_ret:
            lst = list(r.split())
            if lst[3] == "No":
                print(f"\nEnrollment No : {lst[1]}\nBook ID      : {lst[0]}\n")
        ret.close()

    elif action == 4:
        en_no = input("Enter your Enrollment no. :- ")
        det = open("issue_book.txt", 'r')
        d = det.readlines()
        i = 0
        for i in d:
            ls = list(i.split())
            if en_no == ls[0]:
                print(f"\nBook ID        : {ls[0]}\nEnrollment no. : {ls[1]}\nIssue Dt.      : {ls[2]}\n"
                      f"Return Status : {3}\nReturn Dt.     : {ls[4]}\n")
        det.close()

    elif action == 5:
        b_name = input("Enter book name :- ").replace(" ", "_")
        bid = int(input("Enter Book ID :- "))
        author = input("Enter the Author name :- ").replace(" ", "_")
        book = open("book.txt", 'a')
        book.write(f"{b_name} {bid} {author}\n")
        book.close()
        print("Data saved")

    elif action == 6:
        name = input("Enter student name :- ").replace(" ", "_")
        enr_no = int(input("Enter Enrollment number :- "))
        std = input("Enter you Class :- ")
        mob = int(input("Enter Mobile number :- "))
        stud = open("stud_info.txt", 'a')
        stud.write(f"{name} {enr_no} {std} {mob}\n")
        stud.close()
        print("Data saved")

    elif action == 7:
        b_list = open("book.txt", 'r')
        r = b_list.readlines()
        for i in r:
            ls = list(i.split())
            print(f"\nBook ID : {ls[1]}\nBook Name : {ls[0]}\nAuthor : {ls[2]}\n")

    elif action == 8:
        search_option = int(input("\nSearch by :\n1. Book ID\n2. Book Name\n3. Author\n"))
        search = input("Enter what you want to search :- \t").upper().replace(" ", "_")
        print(search)
        search_book(search_option, search)

    elif action == 9:
        pass

    elif action == 10:
        exit()

    else:
        print("Wrong Selection\n")
