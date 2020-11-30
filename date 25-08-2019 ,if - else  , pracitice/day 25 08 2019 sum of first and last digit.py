
'''Adding first ad last digit'''

print("Enter two numbers :\n")
'''Enter $ digit numbers only'''
a=int(input())
b=int(input())

c=(a%10)+(b%10)

d=(a/1000)+(b/1000);

print("Addition of First digit : ",d)
print("Addition if Last digit  : ",c)

