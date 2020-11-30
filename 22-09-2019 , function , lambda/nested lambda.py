# in python instead of inline function there is an option available called as "lambda" which is used to convert a function in a
# single line whichh is returned to a variable and then we can call that variable
import math
add,sr,f=lambda x,y: x+y,lambda x:math.sqrt(x),lambda x:math.factorial(x)

# this is as good as
# def add(x,y):
#     return x+y




print("Addition is    :",add(20,10))
print("Square Root is :",sr(20))
print("Factorial is   :",f(5))