# file = open("C:\\Users\\ompra\\Pictures\\wallpaper\\pop.jpg", "rb").read()
# print(file)

f = open("readlines.txt", "r")
data = f.readlines()
print(data)

# data[0] = "hello guys"
f.close()

f1 = open("readlines.txt", "w")
for d in data:
    f1.write(d)
    f1.write("\n")

f1.close()
print("done update")
