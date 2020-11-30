import time

def test():
    time.sleep(2)

t = time.clock()
test()
t1 = time.clock()

print("t is ",t)
print("t1 is ",t1)
print("difference is ",t1-t)

