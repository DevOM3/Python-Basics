# del is used when we want to delete an objet whole
# in can delete an attribute in python 2 but only object in python 3


class Fan:
    company = ""
    price = 0
    colour = ""
    model = ""

    def show(self):
        print("Company : \t", self.company)
        print("Company : \t", self.colour)
        print("Company : \t", self.model)
        print("Company : \t", self.price)
    def accept(self):
        self.company = input("Company : \t")
        self.colour = input("Colour : \t")
        self.model = input("Model : \t")
        self.price = input("Price : \t")



f1 = Fan()
del f1
f1.accept()
f1.show()








