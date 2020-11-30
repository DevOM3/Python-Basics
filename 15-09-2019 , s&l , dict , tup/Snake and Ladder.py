import random

dictionary={}
i=0
initial_score=0
players=int(input("Enter Number of players playing this game :\t"))

for i in range(0,players):
    name = input("Enter your Name :\t")
    dictionary.update({name:initial_score})
print(dictionary)

while True:
    initial_score+=1
    print(f"Rolling for {initial_score}")
    input("Press Enter to Roll the Dice\t")
    b=random.randint(1,6)
    print(b)
    dictionary.update({name:b})
    if initial_score==players:
        initial_score=0
        print(dictionary)
        continue
    elif b==6:
        print(f"Again chance for {initial_score}")
        initial_score-=1
