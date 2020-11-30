'''map is alternative of while ... it can be use to call the function with giving mulriple parameters at a time of calling
that  function
syntax : - map(function name , sequence)
syntax : - map(lambda , parameters )
'''


# for function
def square( a , b):
    a = a + 5
    b = b + 5
    return a + b

ls = [1,2,3,4,5]
ls1 = [6,7,8,9,0]
print(list(map(square,ls,ls1)))




#using dictionary
def square( a , b):
    a = a + 5
    b = b + 5
    return a + b

ls = {1:6,2:7,3:8,4:9,5:0}
ls1 = {6:5,7:4,8:3,9:2,0:1}
print(list(map(square,ls,ls1)))



# using tuple
def square( a , b):
    a = a + 5
    b = b + 5
    return a + b

ls = (1,2,3,4,5)
ls1 = (6,7,8,9,0)
print(list(map(square,ls,ls1)))



# for lambda
ls2 = [1,2,3,4,5]

print(list(map(lambda n : n * n,ls2)))