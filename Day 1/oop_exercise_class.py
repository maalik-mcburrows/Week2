class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def description(self):
        return"The car is a {} {} {}.".format(self.year, self.make, self.model)
    def print_info(self):
        print("{} {} {}".format(self.year, self.make, self.model))
car = Vehicle("McLaren", "P1", 2020)
print(car.description())

car.print_info()

#     make: "McLaren"
#     model: "P1"
#     year: 2020
# car = Vehicle("McLaren", "P1", 2020)
# print(car.make, car.model, car.year)