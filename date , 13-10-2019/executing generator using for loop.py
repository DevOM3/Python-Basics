
i = 1

def function(n):
    print("This is ",n)
    yield n
    n = n + 1
    print("This is ",n)
    yield n
    n = n + 1
    print("This is ",n)
    yield n
    n = n + 1
    print("This is ",n)
    yield n


g = function(i)

for j in g :
     print(j)