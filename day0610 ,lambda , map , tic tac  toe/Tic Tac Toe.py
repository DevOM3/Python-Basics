print("\t\tTic Tac Toe\n\n")

p1 = input("Enter the name of Player 1 :\t")
p2 = input("Enter the name of Player 2 :\t")

first = "X"
second = "O"
n = 1
blocks = []
occupied = []
inputs = [0]
chance = 1


def nos():
    try:
        if n == 1:
            print(f"\n\nChance for {p1} :")
        elif n == 2:
            print(f"\n\nChance for {p2} :")
        block = int(input("Enter the number of block where you want to place Your Symbol : \t"))
        inputs.append(block)
        return nblock
    except:
        print("Syntax error ........Enter correct choice")


for i in range(0, 9):
    blocks.append(i+1)
    print("|", blocks[i], "|", end=" ")
    if i == 2 or i == 5:
        print()


while True:
    chance = chance + 1
    no = nos()

    if no == 1:
        if n == 1:
            blocks[no-1] = first
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 2
        else:
            blocks[no-1] = second
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 1

    elif no == 2:
        if n == 1:
            blocks[no-1] = first
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 2
        else:
            blocks[no-1] = second
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 1

    elif no == 3:
        if n == 1:
            blocks[no-1] = first
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 2
        else:
            blocks[no-1] = second
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 1

    elif no == 4:
        if n == 1:
            blocks[no-1] = first
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 2
        else:
            blocks[no-1] = second
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 1

    elif no == 5:
        if n == 1:
            blocks[no-1] = first
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 2
        else:
            blocks[no-1] = second
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 1

    elif no == 6:
        if n == 1:
            blocks[no-1] = first
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 2
        else:
            blocks[no-1] = second
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 1
    elif no == 7:
        if n == 1:
            blocks[no-1] = first
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 2
        else:
            blocks[no-1] = second
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 1
    elif no == 8:
        if n == 1:
            blocks[no-1] = first
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 2
        else:
            blocks[no-1] = second
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 1

    elif no == 9:
        if n == 1:
            blocks[no-1] = first
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 2
        else:
            blocks[no-1] = second
            for i in range(0, 9):
                print("|", blocks[i], "|", end=" ")
                if i == 2 or i == 5:
                    print()
            n = 1

    if blocks[0] == blocks[1] == blocks[2] or blocks[3] == blocks[4] == blocks[5] \
       or blocks[6] == blocks[7] == blocks[8]\
       or blocks[0] == blocks[3] == blocks[6] or blocks[1] == blocks[4] == blocks[7] \
       or blocks[2] == blocks[5] == blocks[8] or blocks[0] == blocks[4] == blocks[8] \
       or blocks[2] == blocks[4] == blocks[6]:
        if n == 1:
            print(f"\n\nCongratulation!!!\n{p1} Won")
            break
        else:
            print(f"\n\nCongratulation!!!\n{p2} Won")
            break
    elif (blocks[0]) != 1 and (blocks[1]) != 2 and (blocks[2]) != 3 and \
            (blocks[3]) != 4 and (blocks[4]) != 5 and (blocks[5]) != 6 and (blocks[6]) != 7 \
            and (blocks[7]) != 8 and (blocks[8]) != 9:
        print("\n\nIt's Tie .........!!!")
        break
    else:
        continue
