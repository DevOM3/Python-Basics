import math

a=int(input("Enter a number :\t"))

d={1:math.sqrt(a),2:math.factorial(a)}


print("What do you want ?")
print("1. Square Root")
print("2. Factorial")

i=int(input())

print(d[i])