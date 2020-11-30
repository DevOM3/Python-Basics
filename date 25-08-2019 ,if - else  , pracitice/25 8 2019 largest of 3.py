'''largest of 3 using logical op'''

a=int(input())
b=int(input())
c=int(input())

if a<b and b<c:
    print(c," is largest")
elif b<a and c<a:
    print(a," is largest")
else:
    print(b," is largest")