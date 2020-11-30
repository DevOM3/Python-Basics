'''
reurning value is possible by using yield keyword:

yield variable
'''


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
a = g.__next__()
print(a)
b = g.__next__()
print(b)
c = g.__next__()
print(c)
d = g.__next__()
print(d)