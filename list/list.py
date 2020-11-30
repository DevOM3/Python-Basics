'''list is like Array'''

print("List is given Below:\n")
print("Enter 5 values :\n")

ls=[]
i=1

while i<=5:
    a = int(input())
    ls.append(a)
    i+=1
print(ls)
sz=ls.__len__()
i=0
while i<sz:

    print(ls[i],end=" ")
    i+=1