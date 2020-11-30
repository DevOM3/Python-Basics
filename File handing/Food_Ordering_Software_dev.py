print("Food Ordering Software for Practioners\n")


def practioner_opertions():
    return int(input("What you want to do : \n"
                     "1. Update Hotels\n"
                     "2. Update Hotel menus and prices\n"
                     "3. Show Hotel list\n"
                     "4. Show Menu of Particular Hotel\n"
                     "5. Quit\n"
                     "Enter your Choice :- \t"))


def hotel():
    hot = open("Hotel list.txt", 'w')
    hot.write("HYDRABADI_BIRYANI\n"
              "CHINA_TOWN\n"
              "YUMWICH\n"
              "MCDONALDS\n"
              "AMARPREET\n"
              "DOMINOZ\n")
    hot.close()


def hydrabadi():
    hb = open("hydrabadi_biryani.txt", 'w')
    hb.write("CHICKEN_BIRYANI 150\n"
             "MUTTON_BIRYANI 210\n"
             "ANDA_BIRYANI 120\n"
             "VEG_BIRYANI 100\n"
             "FISH_BIRYANI 160\n")
    hb.close()


def china_town():
    ct = open("china_town.txt", 'w')
    ct.write("FRIED_RICE 150\n"
             "MANCHURIAN 120\n"
             "SCHEZWAN_HAKKA_NOODLES 170\n"
             "NON-VEG_HAKKA_NOODLES 200\n"
             "MANCHURIAN_HAKKA_NOODLES 190\n")
    ct.close()


def yumwich():
    yw = open("yumwich.txt", 'w')
    yw.write("PANERR_SANDWICH 95\n"
             "CHEESE_SANDWICH 65\n"
             "FRIES_SANDWICH 75\n"
             "GRILL_SANDWICH 99\n"
             "CHICKEN_SANDWICH 120\n")
    yw.close()


def mcdonalds():
    md = open("mcdonalds.txt", 'w')
    md.write("HAPPY_MEAL 120\n"
             "VEG_ROLL 70\n"
             "FREMCH_FRIES 160\n"
             "MCCHICKEN 201\n"
             "MEXICAN_TIKKI 145\n")
    md.close()


def amarpreet():
    amar = open("amarpreet.txt", 'w')
    amar.write("MASALA_ROTI 10\n"
               "CHICKEN_CURY 110\n"
               "PANEER-CURY 100\n"
               "SHEV_CURY 90\n"
               "GARLIC_NAN 30\n")
    amar.close()


def dominoz():
    dz = open("dominoz.txt", 'w')
    dz.write("PANEER 150\n"
             "FARMHOUSE 130\n"
             "MARGARITA 99\n"
             "CHICKEN 160\n"
             "MASALA 120\n")
    dz.close()


def update(*kwargs):
    upd = open(kwargs[0], 'a')
    if len(kwargs) == 2:
        upd.write(kwargs[1] + " ")
        open(f"{kwargs[1]}.txt", 'w').close()
    elif len(kwargs) == 4:
        up = open(kwargs[0], 'r')
        if kwargs[3] not in up.read():
            upd.write(kwargs[1] + " " + kwargs[2] + " " + kwargs[3])
        else:
            print("Food_ID already Exist , Try again Later !!!")
    upd.close()


def options():
    h = int(input("Enter the number of Hotel to which you want to update this menu and price : \n"
                  "1. Hydrabadi Biryani\n"
                  "2. China Town\n"
                  "3. Yumwich\n"
                  "4. McDonalds\n"
                  "5. Amarpreet\n"
                  "6. Dominoz\n"
                  "Enter your choice :- \t"))
    return h


def op_file(file):
    opn = open(file, 'r').readlines()
    for i in opn:
        ls = list(i.split())
        print(f"Menu  : {ls[0]}\n"
              f"Price : {ls[1]}\n"
              f"Id    : {ls[2]}")


def loop():
    while True:
        pop = practioner_opertions()

        if pop == 1:
            hotels = input("Enter the name of hotel you want to add :- \t").upper().replace(" ", "_")
            update("Hotel list.txt", hotels)

        elif pop == 2:
            menu = input("Enter the Menu :- ").upper().replace(" ", "_")
            price = input("Enter the Price :- ")
            food_id = input("Enter Food ID :- ")
            hot = options()
            if hot == 1:
                update("hydrabadi_biryani.txt", menu, price, food_id)
            elif hot == 2:
                update("china_town.txt", menu, price, food_id)
            elif hot == 3:
                update("yumwich.txt", menu, price, food_id)
            elif hot == 4:
                update("mcdonalds.txt", menu, price, food_id)
            elif hot == 5:
                update("amarpreet.txt", menu, price, food_id)
            elif hot == 6:
                update("dominoz.txt", menu, price, food_id)

        elif pop == 3:
            r = open("Hotel list.txt", 'r').read()
            print("\n" + r)

        elif pop == 4:
            o = options()
            if o == 1:
                op_file("hydrabadi_biryani.txt")
            elif o == 2:
                op_file("china_town.txt")
            elif o == 3:
                op_file("yumwich.txt")
            elif o == 4:
                op_file("mcdonalds.txt")
            elif o == 5:
                op_file("amarpreet.txt")
            elif o == 6:
                op_file("dominoz.txt")
            else:
                print("Wrong Selection ! \nTry Again !!!\n")
        elif pop == 5:
            quit()
        else:
            print("Wrong Selection ! \nTry Again !!!\n")


loop()
# hotel()
# amarpreet()
# dominoz()
# china_town()
# hydrabadi()
# yumwich()
# mcdonalds()
