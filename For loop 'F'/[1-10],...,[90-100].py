ls=[]


i=1
j=1
while i<=10:
    ls.append(list(range(j,j+10)))
    i+=1
    j+=10
print(ls)