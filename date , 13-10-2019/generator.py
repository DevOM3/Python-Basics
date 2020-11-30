'''
generator is the function which we can divide whenever we want to use it in broken form
the keyword "yield" is used to break te function whenever we want
it automatically returns , so we have to store it in the a  variable
it has some functions which are used to manipulate it

difference between function and generator is that function's return ends the generator and for generator yield pauses
the generator
'''

i = 1

def function(n):
    print("This is ",n)
    yield
    n = n + 1
    print("This is ",n)
    yield
    n = n + 1
    print("This is ",n)
    yield
    n = n + 1
    print("This is ",n)
    yield


g = function(i)
g.__next__()
g.__next__()
g.__next__()
g.__next__()