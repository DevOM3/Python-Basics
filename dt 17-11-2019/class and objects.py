# second method of declaring data members in the function

class Fan:
    def accept(self):
        self.company = input("Company : \t")
        self.colour = input("Colour : \t")
        self.model = input("Model : \t")
        self.price = input("Price : \t")

    def show(self):
        print("Company : \t", self.company)
        print("Company : \t", self.colour)
        print("Company : \t", self.model)
        print("Company : \t", self.price)


f1 = Fan()
f1.accept()
f1.show()
