# class Const:
#     def __init__(self):
#         print("Hello from Constructor")
#
#     def __del__(self):
#         print("Hello from destructor")
#
#
# c = Const()
#
# c.__init__()
# c.__del__()0

class Const:
    def __init__(self):
        print("Hello from Constructor")

    def __del__(self):
        print("Hello from destructor")
        return "madarchod"

c = Const()

c.__init__()
k = c.__del__()
print(k)