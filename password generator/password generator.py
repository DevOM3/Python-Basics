import random

software = input("For which Software you want to create Password : \t")

scase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
         'v', 'w', 'x', 'y', 'z']
ucase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
         'V', 'W', 'X', 'Y', 'Z']
sy = ['!', '@', ' ', '#', '%', '$', '^', '&', '*', '(', ')', '+', '-', '/', '|', '[', ']', '{', '}', ';', ':', ',',
      '.', '<', '>', '?', '"', '=']
num = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

no = []
symbols = []
spassword = []
upassword = []

for i in scase:
    spassword.append(i)

for i in ucase:
    upassword.append(i)

for i in sy:
    symbols.append(i)

for i in num:
    no.append(i)

password = random.choice(no) + random.choice(upassword) + random.choice(spassword) + random.choice(upassword) \
           + random.choice(no) \
           + random.choice(symbols) + random.choice(upassword) + random.choice(upassword) + random.choice(no) \
           + random.choice(spassword) \
           + random.choice(spassword) + random.choice(spassword)

print(password)

password_vault = open("password.txt", 'a')
password_vault.write("\n" + software + ":" + password)
password_vault.close()
