import random

name={}
player=[]
roll_data=[]
index=0
dice = 0
player_no=0

no_of_players=int(input("Enter number of players playing this game :\t"))

for i in range(0,no_of_players):
    player.append(input(f"Enter the name of Player {i+1} : \t"))
    name.update({player[i]:0})

print("\n",name,"\n")

i=0

def roll():
    input("Press Enter key to Roll the dice :\t")
    dice_roll = random.randint(1, 6)
    print(dice_roll)
    return dice_roll


while True:
    roll_data.append(dice)
    print(roll_data)
    print(f"\nFor {player[i]}")
    dice=roll()
    if i>=no_of_players-1:
        i=0
        player_no = 0
    else:
        i = i + 1
        player_no = player_no + 1
    if dice==6:
        print("Wooooh !!! You are Lucky tis time , You got 6 ")
        print(f"Again chance for {player[i-1]}")
        luck=roll()
        if luck!=6:
            dice = dice + luck
            dice = dice + roll_data[index]
            index += 1
        else:
            luck2=roll()
            dice = dice + luck + luck2
            dice = dice + roll_data[index]
            index += 1
    else:
        if no_of_players==1:
            dice = dice + roll_data[index]
            index += 1
        # if no_of_players==2:
        #     if index>2:
        #         dice = dice + roll_data[index - 2]
        #         index = index + 1
        #     else:
        #         index = index + 1

    if dice==1:
        print("Niceeer !!!  You climbed a Ladder ...... Now you are on 38")
        dice=38
    elif dice==4:
        print("Niceeer !!!  You climbed a Ladder ...... Now you are on 14")
        dice=14
    elif dice==8:
        print("Niceeer !!!  You climbed a Ladder ...... Now you are on 30")
        dice=30
    elif dice==21:
        print("Niceeer !!!  You climbed a Ladder ...... Now you are on 42")
        dice=42
    elif dice==28:
        print("Niceeer !!!  You climbed a Ladder ...... Now you are on 76")
        dice=76
    elif dice==50:
        print("Niceeer !!!  You climbed a Ladder ...... Now you are on 67")
        dice=67
    elif dice==71:
        print("Niceeer !!!  You climbed a Ladder ...... Now you are on 92")
        dice=92
    elif dice==88:
        print("Niceeer !!!  You climbed a Ladder ...... Now you are on 99")
        dice=99
    elif dice==34:
        print("Ouuuuuuch !!! A bloody snake bite you . Now you are on 6")
        dice=6
    elif dice==48:
        print("Ouuuuuuch !!! A bloody snake bite you . Now you are on 26")
        dice=26
    elif dice==62:
        print("Ouuuuuuch !!! A bloody snake bite you . Now you are on 18")
        dice=18
    elif dice==88:
        print("Ouuuuuuch !!! A bloody snake bite you . Now you are on 24")
        dice=24
    elif dice==95:
        print("Ouuuuuuch !!! A bloody snake bite you . Now you are on 56")
        dice=56
    elif dice==97:
        print("Ouuuuuuch !!! A bloody snake bite you . Now you are on 78")
        dice=78
    elif dice==100:
        print("You are on 100 !!! You won this game !!! Congratulations !!!")
        break
    elif dice>100:
        dice=roll_data[index-1]



    name.update({player[player_no - 1]: dice})
    print(name)
