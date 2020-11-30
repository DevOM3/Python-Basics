print("1 = Stone\n2 = Paper\n3 = Scissor\n\n")

a=int(input("Enter your choice :\t"))
import random
b=random.randrange(1,4)
print("You entered ",a)
print("Computer entered ",b)

if a==1 and b==2:
    print("Computer won\n")

if a==1 and b==3:
    print("You won !!!\n")

if a==b:
    print("Tie !!!")

if b == 1 and a == 2:
    print("You won\n")

if b == 1 and a == 3:
    print("Computer won !!!\n")

if a==3 and b==1:
    print("Computer won ")

if a==3 and b==2:
    print("You won !!!")
if a==2 and b==3:
    print("You won !!!")

input()