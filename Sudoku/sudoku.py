def skeleton():
    for i in range(0, 81):
        if i == 8 or i == 17 or i == 26 or i == 35 or i == 44 or i == 53 or i == 62 or i == 71 or i == 80:
            print(f"| {list1[i]} |")
        elif i == 2 or i == 5 or i == 11 or i == 14 or i == 20 or i == 23 or i == 29 or i == 32 or i == 38 or i == 41 \
                or i == 47 or i == 50 or i == 56 or i == 59 or i == 65 or i == 68 or i == 74 or i == 77:
            print(f"| {list1[i]} |", end="")
        else:
            print(f"| {list1[i]} ", end="")

        if i == 26 or i == 53:
            print("========================================")


def redundent():
    global value
    if list1[0] == list1[1] == list1[2] == list1[3] == list1[4] == \
            list1[5] == list1[6] == list1[7] == list1[8] or \
       list1[9] == list1[10] == list1[11] == list1[12] == list1[13] == \
            list1[14] == list1[15] == list1[16] == list1[17] or\
       list1[18] == list1[19] == list1[20] == list1[21] == list1[22] == \
            list1[23] == list1[24] == list1[25] == list1[26]or\
       list1[27] == list1[28] == list1[29] == list1[30] == list1[31] == \
            list1[32] == list1[33] == list1[34] == list1[35] or\
       list1[36] == list1[37] == list1[38] == list1[39] == list1[40] == \
            list1[41] == list1[42] == list1[43] == list1[44] or\
       list1[45] == list1[46] == list1[47] == list1[48] == list1[49] == \
            list1[50] == list1[51] == list1[52] == list1[53] or\
       list1[54] == list1[55] == list1[56] == list1[57] == list1[58] == \
            list1[59] == list1[60] == list1[61] == list1[62] or\
       list1[63] == list1[64] == list1[65] == list1[66] == list1[67] == \
            list1[68] == list1[69] == list1[70] == list1[71] or\
       list1[72] == list1[73] == list1[74] == list1[75] == list1[76] == \
            list1[77] == list1[78] == list1[79] == list1[80] or\
       list1[0] == list1[1] == list1[2] == list1[9] == list1[10] == \
            list1[11] == list1[18] == list1[19] == list1[20] or \
       list1[3] == list1[4] == list1[5] == list1[12] == list1[13] == \
            list1[14] == list1[21] == list1[22] == list1[23] or \
       list1[6] == list1[7] == list1[8] == list1[15] == list1[16] == \
            list1[17] == list1[24] == list1[25] == list1[26] or \
       list1[27] == list1[28] == list1[29] == list1[36] == list1[37] == \
            list1[38] == list1[45] == list1[46] == list1[47] or\
       list1[30] == list1[31] == list1[32] == list1[39] == list1[40] == \
            list1[41] == list1[48] == list1[49] == list1[50] or\
       list1[33] == list1[34] == list1[35] == list1[42] == list1[43] == \
            list1[44] == list1[51] == list1[52] == list1[53] or\
       list1[54] == list1[55] == list1[56] == list1[63] == list1[64] == \
            list1[65] == list1[72] == list1[73] == list1[74] or\
       list1[57] == list1[58] == list1[59] == list1[66] == list1[67] == \
            list1[68] == list1[75] == list1[76] == list1[77] or\
       list1[60] == list1[61] == list1[62] == list1[69] == list1[70] == \
            list1[71] == list1[78] == list1[79] == list1[80] or\
       list1[0] == list1[9] == list1[18] == list1[27] == list1[36] == \
            list1[45] == list1[54] == list1[63] == list1[72] or\
       list1[1] == list1[10] == list1[19] == list1[28] == list1[37] == \
            list1[46] == list1[55] == list1[64] == list1[73] or\
       list1[2] == list1[11] == list1[20] == list1[29] == list1[38] == \
            list1[47] == list1[56] == list1[65] == list1[74] or\
       list1[3] == list1[12] == list1[21] == list1[30] == list1[39] == \
            list1[48] == list1[57] == list1[66] == list1[75] or\
       list1[4] == list1[13] == list1[22] == list1[31] == list1[40] == \
            list1[49] == list1[58] == list1[67] == list1[76] or\
       list1[5] == list1[14] == list1[23] == list1[32] == list1[41] == \
            list1[50] == list1[59] == list1[68] == list1[77] or\
       list1[6] == list1[15] == list1[24] == list1[33] == list1[42] == \
            list1[51] == list1[60] == list1[69] == list1[78] or\
       list1[7] == list1[16] == list1[25] == list1[34] == list1[43] == \
            list1[52] == list1[61] == list1[70] == list1[79] or\
       list1[8] == list1[17] == list1[26] == list1[35] == list1[44] == \
            list1[53] == list1[62] == list1[71] == list1[80]:
        pass
    else:
        print("Redundent numbers are not allowed in same row....")
        value = " "


list1 = [5, 3, " ", " ", 7, " ", " ", " ", " ",
         6, " ", " ", 1, 9, 5, " ", " ", " ",
         " ", 9, 8, " ", " ", " ", " ", 6, " ",
         8, " ", " ", " ", 6, " ", " ", " ", 3,
         4, " ", " ", 8, " ", 3, " ", " ", 1,
         7, " ", " ", " ", 2, " ", " ", " ", 6,
         " ", 6, " ", " ", " ", " ", 2, 8, " ",
         " ", " ", " ", 4, 1, 9, " ", " ", 5,
         " ", " ", " ", " ", 8, " ", " ", 7, 9]


skeleton()
print("\n\n\nAbove is the structure od Sudoku .......")
print("Rules :\n")
print("1) No same number is  allowed in a same row or column .")
print("2) It is not allowed to enter a same number in the same block .")
print("Blocks and positions in blocks are numbered as :\n"
      "| 1 | 2 | 3 |\n"
      "| 4 | 5 | 6 |\n"
      "| 7 | 8 | 9 |\n")
print("Enter the block and position")

while True:

    block = int(input("Enter the block :"))
    position = int(input("Enter the position :"))
    print("Enter the value between 1 to 9 you want to insert at the block and the position you suggested :- ")
    value = int(input("Enter the value You want to Enter :- "))

    if block == 1 and position == 1 or block == 1 and position == 2 or block == 1 and position == 4 or block == 1 and \
            position == 8 or block == 1 and position == 9 or block == 2 and position == 2 or block == 2 and \
            position == 4 or block == 2 and position == 5 or block == 2 and position == 6 or block == 3 and \
            position == 8 or block == 4 and position == 1 or block == 4 and position == 4 or block == 4 and \
            position == 7 or block == 5 and position == 2 or block == 5 and position == 4 or block == 5 and \
            position == 6 or block == 5 and position == 8 or block == 6 and position == 3 or block == 6 and \
            position == 6 or block == 6 and position == 9 or block == 7 and position == 2 or block == 8 and \
            position == 4 or block == 8 and position == 5 or block == 8 and position == 6 or block == 8 and \
            position == 8 or block == 9 and position == 1 or block == 9 and position == 2 or block == 9 and \
            position == 6 or block == 9 and position == 8 or block == 9 and position == 9:
        print("You cannot overrite the existing values ")
    elif block == 1 and position == 3:
        redundent()
        list1[2] = value
        skeleton()
    elif block == 2 and position == 1:
        redundent()
        list1[3] = value
        skeleton()
    elif block == 2 and position == 3:
        redundent()
        list1[5] = value
        skeleton()
    elif block == 3 and position == 1:
        redundent()
        list1[6] = value
        skeleton()
    elif block == 3 and position == 2:
        redundent()
        list1[7] = value
        skeleton()
    elif block == 3 and position == 3:
        redundent()
        list1[8] = value
        skeleton()
    elif block == 1 and position == 5:
        redundent()
        list1[10] = value
        skeleton()
    elif block == 1 and position == 6:
        redundent()
        list1[11] = value
        skeleton()
    elif block == 3 and position == 4:
        redundent()
        list1[15] = value
        skeleton()
    elif block == 3 and position == 5:
        redundent()
        list1[16] = value
        skeleton()
    elif block == 3 and position == 6:
        redundent()
        list1[17] = value
        skeleton()
    elif block == 1 and position == 7:
        redundent()
        list1[18] = value
        skeleton()
    elif block == 2 and position == 7:
        redundent()
        list1[21] = value
        skeleton()
    elif block == 2 and position == 8:
        redundent()
        list1[22] = value
        skeleton()
    elif block == 2 and position == 9:
        redundent()
        list1[23] = value
        skeleton()
    elif block == 3 and position == 7:
        redundent()
        list1[24] = value
        skeleton()
    elif block == 3 and position == 9:
        redundent()
        list1[26] = value
        skeleton()
    elif block == 4 and position == 2:
        redundent()
        list1[28] = value
        skeleton()
    elif block == 4 and position == 3:
        redundent()
        list1[29] = value
        skeleton()
    elif block == 5 and position == 1:
        redundent()
        list1[30] = value
        skeleton()
    elif block == 5 and position == 3:
        redundent()
        list1[32] = value
        skeleton()
    elif block == 6 and position == 1:
        redundent()
        list1[33] = value
        skeleton()
    elif block == 6 and position == 2:
        redundent()
        list1[34] = value
        skeleton()
    elif block == 4 and position == 5:
        redundent()
        list1[37] = value
        skeleton()
    elif block == 4 and position == 6:
        redundent()
        list1[38] = value
        skeleton()
    elif block == 5 and position == 5:
        redundent()
        list1[40] = value
        skeleton()
    elif block == 6 and position == 4:
        redundent()
        list1[42] = value
        skeleton()
    elif block == 6 and position == 5:
        redundent()
        list1[43] = value
        skeleton()
    elif block == 4 and position == 8:
        redundent()
        list1[46] = value
        skeleton()
    elif block == 4 and position == 9:
        redundent()
        list1[47] = value
        skeleton()
    elif block == 5 and position == 7:
        redundent()
        list1[48] = value
        skeleton()
    elif block == 5 and position == 9:
        redundent()
        list1[50] = value
        skeleton()
    elif block == 6 and position == 7:
        redundent()
        list1[51] = value
        skeleton()
    elif block == 6 and position == 8:
        redundent()
        list1[52] = value
        skeleton()
    elif block == 7 and position == 1:
        redundent()
        list1[54] = value
        skeleton()
    elif block == 7 and position == 3:
        redundent()
        list1[56] = value
        skeleton()
    elif block == 8 and position == 1:
        redundent()
        list1[57] = value
        skeleton()
    elif block == 8 and position == 2:
        redundent()
        list1[58] = value
        skeleton()
    elif block == 8 and position == 3:
        redundent()
        list1[59] = value
        skeleton()
    elif block == 9 and position == 3:
        redundent()
        list1[62] = value
        skeleton()
    elif block == 7 and position == 4:
        redundent()
        list1[63] = value
        skeleton()
    elif block == 7 and position == 5:
        redundent()
        list1[64] = value
        skeleton()
    elif block == 7 and position == 6:
        redundent()
        list1[65] = value
        skeleton()
    elif block == 9 and position == 4:
        redundent()
        list1[69] = value
        skeleton()
    elif block == 9 and position == 5:
        redundent()
        list1[70] = value
        skeleton()
    elif block == 7 and position == 7:
        redundent()
        list1[72] = value
        skeleton()
    elif block == 7 and position == 8:
        redundent()
        list1[73] = value
        skeleton()
    elif block == 7 and position == 9:
        redundent()
        list1[74] = value
        skeleton()
    elif block == 8 and position == 7:
        redundent()
        list1[75] = value
        skeleton()
    elif block == 8 and position == 9:
        redundent()
        list1[77] = value
        skeleton()
    elif block == 9 and position == 7:
        redundent()
        list1[78] = value
        skeleton()
