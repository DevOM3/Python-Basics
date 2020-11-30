# in python instead of inline function there is an option available called as "lambda" which is used to convert a function in a
# single line whichh is returned to a variable and then we can call that variable
import math
add=lambda x,y: x+y
# this is as good as
# def add(x,y):
#     return x+y

sr=lambda x:math.sqrt(x)

f=lambda x:math.factorial(x)

print("Addition is    :",add(20,10))
print("Square Root is :",sr(20))
print("Factorial is   :",f(5))