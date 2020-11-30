import random
i = 1
guess = 0

name = input("Enter your Name : \t")
print("Welcome ",name,"!!! Let's get started ......")
input("Press Enter key to start the game")

random_number = random.randint(20,90)
# print(random_number)
while True:
    # guess = int(input("\nEnter your guessed Number : \t"))
    try:
        guess = int(input("\nEnter your guessed Number : \t"))
    except Exception as e:
        print("Only numbers are allowed")

    if guess > random_number:
        print("The Number is Smaller than ",guess)
        i = i + 1
        continue
    elif guess < random_number:
        print("The Number is Greater than ",guess)
        i = i + 1
        continue
    else:
        print("Congratulations !!! \nYou Won!!! \nYou Guessed it right it is : ",random_number)
        break


print(f"\nYou used {i} chances")