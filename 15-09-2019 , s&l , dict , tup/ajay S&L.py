import random
d={}
ls=[]
print("enter number of student")
a=int(input())
j=1
while j<=a:
    print("enter name of player",j)
    val=input()
    d.update({val:0})
    j=j+1
print(d)
k=1
r=0
i=0
while i<=70:
    k=1
    while k <= a:
        ls.append(k)
        print("enter for player", k)
        r = 0
        z=0
        m = random.randint(1, 6)
        print("you got", m)
        if m==6:
            print("Roll the dice once again")
            z=random.randint(1,6)
        print("z =",z)
        r = d[list(d)[k - 1]] + m +z
        print("r=", r)
        if r == 4:
            print("you got ladder")
            r = 14
        elif r == 8:
            print("you got ladder")
            r = 30
        elif r == 1:
            print("you got ladder")
            r = 38
        elif r == 28:
            print("you got ladder")
            r = 76
        elif r == 21:
            print("you got ladder")
            r = 42
        elif r == 50:
            print("you got ladder")
            r = 67
        elif r == 71:
            print("you got ladder")
            r = 92
        elif r == 80:
            print("you got ladder")
            r = 99
        elif r == 32:
            print("you got snake")
            r = 10
        elif r == 36:
            print("you got snake")
            r = 6
        elif r == 62:
            print("you got snake")
            r = 18
        elif r == 88:
            print("you got snake")
            r = 24
        elif r == 48:
            print("you got snake")
            r = 26
        elif r == 95:
            print("you got snake")
            r = 56
        elif r == 97:
            print("you got snake")
            r = 78
        if r>100:
            r=r-m-z
        if r==100:
            print("you won")
            break
        d.update({list(d)[k - 1]: r})
        print(d)
        k = k + 1

    i=i+1
    if r==100:
        break


