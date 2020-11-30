word = input("Enter a Word : \t")

word = ''.join(sorted(word))
w = word.isupper()
if w==True:
    print(word)

print(word)


# word = input("Enter a Word :\t")
#
# w = word.islower()
# if w==True:
#     word = ''.join(sorted(word))
# word.isalnum()
# print(word)