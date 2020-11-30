dict={}
'''
for i in range(1,4):
    a=input("Enter your name :\t")
    b=0
    dict.update({a:b})


print(dict)'''

while True:
    name=input("Enter your Name :\t")
    phno=int(input("Enter your Number"))
    dict.update({name:phno})
    q=input("Do you want to add another Student ? (y/n)")
    if q=='y' or q=='Y' or q=='Yes' or q=='yes':
        continue
    else:
        break
print(dict)