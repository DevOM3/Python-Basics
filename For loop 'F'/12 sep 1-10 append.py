ls=[]

i=0
k=1

while i<10:
    ls.append([])
    j=k
    while j<k+10:
        ls[i].append(j)
        j=j+1
    k=k+10
    i=i+1
print(ls)