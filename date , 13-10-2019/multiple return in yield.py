'''
if we return multiple values using yield and accept it into a single variable it is then shown in tuple
and if we accept them in te two variables then we will ge it in those variables

'''
i = 1

def function(n):
    j = 0
    print("This is ", n)
    yield n, j
    n = n + 1
    j = j + 1
    print("This is ", n)
    yield n, j
    j = j + 1
    n = n + 1
    print("This is ", n)
    yield n, j
    j = j + 1
    n = n + 1
    print("This is ", n)
    yield n, j


g = function(i)
a = g.__next__()
print(a)
b, p = g.__next__()
print(b, p)
c = g.__next__()
print(c)
d, q = g.__next__()
print(d, q)
