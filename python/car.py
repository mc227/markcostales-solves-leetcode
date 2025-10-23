class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def display(self):
        print(f"My car has make {self.make} and model {self.model}")


my_car = Car("Honda","CRV")

my_car.display()