l=[]

a=int(input("Enter a number : "))

i=0
j=1
while i<10:
    l.append([])
    l[i].append(a)
    l[i].append("*")
    l[i].append(j)
    l[i].append("=")
    l[i].append(a*j)
    i+=1
    j+=1

print(l)