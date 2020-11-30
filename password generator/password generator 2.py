import random

software = input("For which Software you want to create Password : \t")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', ' ', '#', '%', '$', '^', '&', '*', '(', ')',
           '+', '-', '/', '|', '[', ']', '{', '}', ';', ':', ',', '.', '<', '>', '?', '"', '=', '1', '2', '3', '4',
           '5', '6', '7', '8', '9', '0']

password = ""
for i in range(0, 14):
    password = password + random.choice(letters)
print(password)


password_vault = open("password.txt", 'a')
password_vault.write("\n" + software + ":" + password)
