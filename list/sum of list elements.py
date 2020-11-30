print("Enter 5 elements")
ls=[]
i=0

while i<5:
    a=int(input())
    ls.append(a)
    i+=1
print(ls)
j=0
s=0
while j<5:
    s=s+ls[j]
    j+=1
print(s)
