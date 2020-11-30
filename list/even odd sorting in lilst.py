
ls1=[]
ls2=[]
i=0
print("Enter 10 numbers")

while i<10:
    a=int(input())
    if a%2==0:
        ls1.append(a)
    elif a%2==1:
        ls2.append(a)
    i+=1

print(ls1,ls2)


