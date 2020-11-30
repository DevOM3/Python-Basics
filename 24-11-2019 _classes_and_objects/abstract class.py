class A:
    __x = 22
    _y = 21
    def _hello(self):
        print("Namaskaram !!!")
    def __bye(self):
        print("Nikal, ......... , pehli fursat mein nukal !!!!!!")

a = A()
a._y = 20
print(a._y)
print(a._A__x)
a._hello()
a._A__bye()

