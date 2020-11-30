# third method for declaring the data members is the outside the class declaration from the man block
# by using this method we can give one extra attribute to the single particular object to save memory

class Fan:

    def show(self):
        print("Company : \t", self.company)
        print("Company : \t", self.colour)
        print("Company : \t", self.model)
        print("Company : \t", self.price)


f1 = Fan()
f1.company = input("Company : \t")
f1.colour = input("Colour : \t")
f1.model = input("Model : \t")
f1.price = int(input("Price : \t"))
f1.show()
