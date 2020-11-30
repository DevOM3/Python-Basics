from datetime import date
dt = date.today()

print("Food Ordering Software\n\n")


def user_operations():
    return int(input("You can perform following operations\n"
                     "1. Search Food\n"
                     "2. Hotels and Menus\n"
                     "3. You order History\n"
                     "4. Edit Account\n"
                     "5. Create Account\n"
                     "6. Exit\n"
                     "Enter your Choice :- \t"))


def create_account():
    name = input("Enter your name          : ").upper().replace(" ", "_")
    phno = input("Enter your Mobile Number : ")
    mail = input("Enter your Email ID      : ")
    add = input("Enter your Address      : ").upper().replace(" ", "_")
    acc = open("accounts.txt", 'a')
    acc.write(name + " " + phno + " " + add + " " + mail)
    acc.close()


def edit_logic(no):
    edit = open("accounts.txt", 'r')
    data1 = edit.readlines()
    j = 0
    for i in data1:
        ls = list(i.split())
        ls[no - 1] = input("Enter the updated value : ").upper().replace(" ", "_")
        data = ls[0] + " " + ls[1] + " " + ls[2] + " " + ls[3]
        data1[j] = data
        j = j + 1
    edit.close()
    edit = open("accounts.txt", 'w')
    edit.writelines(data1)
    edit.close()


def edit_acc():
    ch = int(input("What do you want to edit ? \n"
                   "1. Name\n"
                   "2. Phone No.\n"
                   "3. Address\n"
                   "4. E-mail ID\n"
                   "Enter your choice :- "))
    if ch == 1:
        edit_logic(1)
    elif ch == 2:
        edit_logic(2)
    elif ch == 3:
        edit_logic(3)
    elif ch == 4:
        edit_logic(4)
    else:
        print("\nWrong Selection ! \nTry Again!!!\n\n")


def hotel_menu():
    hot = open("Hotel list.txt", 'r')
    h = hot.readlines()
    for i in h:
        lst = list(i.split())
        print("\n", lst[0].capitalize().replace("_", " ") + ":")
        menu = open(f"{lst[0].lower()}.txt", 'r')
        m = menu.readlines()
        for j in m:
            ls = list(j.split(" "))
            print(" Menu    : ", ls[0], "\n",
                  "Price   : ", ls[1],
                  "\n Food_ID : ", ls[2])
        menu.close()
    hot.close()


def search_food():
    search = input("What you want to eat today ? : ").upper().replace(" ", "_")
    hot = open("Hotel list.txt", 'r')
    h = hot.readlines()
    for i in h:
        lst = list(i.split())
        menu = open(f"{lst[0].lower()}.txt", 'r')
        m = menu.readlines()
        for j in m:
            ls = list(j.split())
            if search in ls[0]:
                print("\n Hotel   : ", lst[0].capitalize().replace("_", " "), "\n",
                      "Menu    : ", ls[0].capitalize().replace("_", " "), "\n"
                      f" Price   : {ls[1]}\n"
                      f" Book ID : {ls[2]}")
        menu.close()
    hot.close()


def op_file(file):
    op = open(file, 'r')
    opn = op.readlines()
    for i in opn:
        ls = list(i.split())
        print(f"Menu    : {ls[0]}\n"
              f"Price   : {ls[1]}\n"
              f"Book ID : {ls[2]}\n")
    op.close()


def search_hotel():
    search = int(input("Where do you want to eat ?  \n"
                       "1. Hydrabadi Biryani\n"
                       "2. China Town\n"
                       "3. Yumwich\n"
                       "4. McDonalds\n"
                       "5. Amarpreet\n"
                       "6. Dominoz\n"
                       "Enter your choice :- "))
    if search == 1:
        op_file("hydrabadi_biryani.txt")
    elif search == 2:
        op_file("china_town.txt")
    elif search == 3:
        op_file("yumwich.txt")
    elif search == 4:
        op_file("mcdonalds.txt")
    elif search == 5:
        op_file("amarpreet.txt")
    elif search == 6:
        op_file("dominoz.txt")
    else:
        print("\nWrong Selection ! \nTry Again!!!\n\n")
        global flag
        flag = False


def ordr():
    acc = open("accounts.txt", 'r')
    acc_read = acc.readlines()
    hot = open("Hotel list.txt", 'r')
    h = hot.readlines()
    order = input("Enter the Food ID of the item you want to order : ")
    for i in h:
        lst = list(i.split())
        menu = open(f"{lst[0].lower()}.txt", 'r')
        m = menu.readlines()
        for j in m:
            ls = list(j.split())
            for k in acc_read:
                acc_lst = list(k.split())
                if order == ls[2]:
                    print("\nYour order Bill is : \n",
                          "Food Item : ", ls[0].capitalize().replace("_", " "), "\n",
                          "Price     : ", ls[1], "\n",
                          "Food ID   : ", ls[2], "\n",
                          "Hotel     : ", lst[0].capitalize().replace("_", " "), "\n",
                          "Name      : ", acc_lst[0].capitalize().replace("_", " "), "\n"
                          " Phone no. : ", acc_lst[1], "\n"
                          " Address   : ", acc_lst[2].capitalize().replace("_", " "), "\n",
                          "E-mail ID : ", acc_lst[3].lower(), "\n",
                          "Date      :", dt, "\n")

                    per_his = open("personal_history.txt", 'a')
                    per_his.write(ls[0] + " " + ls[1] + " " + ls[2] + " " + lst[0] + " " + acc_lst[0] + " " +
                                  acc_lst[1] + " " + acc_lst[2] + " " + acc_lst[3].lower() + " " + str(dt) + "\n")
                    per_his.close()
        menu.close()
    hot.close()
    acc.close()


def history():
    per_his = open("personal_history.txt", 'r')
    his = per_his.readlines()
    for i in his:
        lst = list(i.split(" "))
        print(" Food Item : ", lst[0].capitalize().replace("_", " "), "\n",
              "Price     : ", lst[1], "\n",
              "Food ID   : ", lst[2], "\n",
              "Hotel     : ", lst[3], "\n",
              "Name      : ", lst[4].capitalize().replace("_", " "), "\n"
              " Phone no. : ", lst[5], "\n"
              " Address   : ", lst[6].capitalize().replace("_", " "), "\n",
              "E-mail ID : ", lst[7].lower(), "\n",
              "Date      : ", dt, "\n")


def loop():
    while True:

        uop = user_operations()
        if uop == 1:
            search_type = int(input("How do you want to search by : \n"
                                    "1. Food\n"
                                    "2. Hotel\n"
                                    "Enter your choice : \t"))
            if search_type == 1:
                search_food()
                ordr()
            elif search_type == 2:
                search_hotel()
                ordr() if flag is True else None
            else:
                print("\nWrong Selection ! \nTry Again!!!\n\n")

        elif uop == 2:
            hotel_menu()
            ordr()
        elif uop == 3:
            history()
        elif uop == 4:
            edit_acc()
        elif uop == 5:
            create_account()
        elif uop == 6:
            exit()
        else:
            print("\nWrong Selection ! \nTry Again!!!\n\n")


flag = True
loop()
