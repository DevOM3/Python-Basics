'''
While loop for dice spinning
Break is as it is
Continue is as it is
'''

import random

print("This is a Die game \n\n\n")
print("Enter number of players :\t")
p=int(input())
print("Press key when you are ready:")
r=input()

b=random.randrange(1,7)
i=int(0)
no=int(-1)
j=p
while True:
    b = random.randrange(1, 7)
    print("For player ",i+1," : ")

    print("You Spinned : ", b)
    print("\n")

    if b!=6 :
        i=i+1
        if i == j:
            i=no
            i=i+1
            continue
    if b==6:
        print("One more chance for player ",i+1)
        c = random.randrange(1, 7)
        print(c)
        if c==6:
            print("Player ",i+1," won")
            break
        else:
            continue

input()




