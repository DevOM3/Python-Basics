#without using range

ls=[]

i=0
j=0
k=1
l=1
m=0

while i<10:
    ls.append([])
    j=m
    while j<2:
        ls[i].append([])
        l=k
        while k<l+5:
            ls[i][j].append(k)
            k=k+1
        j=j+1
    i=i+1
print(ls)


#with using rangge

ls=[]

i=0
j=0
l=1


while i<10:
    ls.append([])
    k=0
    while k<2:
        ls[i].append([])
        ls[i][k] = list(range(l,l+5))
        k=k+1
        l=l+5
    i=i+1
print(ls)






























