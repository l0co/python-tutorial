#######################################################################################################################
print("class can be derived from another class")

class Vehicle:
    def __init__(self, name: str):
        self.name = name

    def start(self, end: str = "\n"):
        print("brrrr...", end=end)

class Car(Vehicle):  # inheritance
    def __init__(self):
        super().__init__("car")  # calling super constructor

    def start(self, end: str = "\n"):
        super().start(" ")  # calling super method
        print("wrrrr...")

bike: Vehicle = Vehicle("bike")
car: Vehicle = Car()

bike.start()  # STDOUT: brrrr...
car.start()  # STDOUT: brrrr... wrrrr...

#######################################################################################################################
print("\ninstanceof")
print(isinstance(bike, Vehicle))  # STDOUT: True
print(isinstance(car, Vehicle))  # STDOUT: True
print(isinstance(bike, Car))  # STDOUT: False
print(isinstance(car, Car))  # STDOUT: True

#######################################################################################################################
print("\nClass.isAssignableFrom()")
print(issubclass(Car, Vehicle))  # STDOUT: True
print(issubclass(Vehicle, Car))  # STDOUT: False
print(issubclass(Vehicle, Vehicle))  # STDOUT: True (!)

#######################################################################################################################
print("\nclass can be derived even from more classes")

class Animal:
    def __init__(self, numberOfLegs: int):
        self.numberOfLegs = numberOfLegs

    def scare(self):
        print("aah!")

class Horse(Animal, Vehicle):
    def __init__(self):
        Vehicle.__init__(self, "horse")  # calling super constructor 1 (second method to call constructor)
        Animal.__init__(self, 4)  # calling super constructor 2

    def scare(self):
        super().scare()
        self.start()  # animal should start after being scared

    def start(self, end: str = "\n"):
        super().start(" ")  # calling super method
        print("n-e-e-e-i-g-h")


horse: Horse = Horse()
print(horse.name)  # STDOUT: horse
print(horse.numberOfLegs)  # STDOUT: 4
horse.start()  # STDOUT: brrrr... n-e-e-e-i-g-h
horse.scare()  # STDOUT: aah!
               #         brrrr... n-e-e-e-i-g-h

animal: Animal = horse
# should work, and works
animal.scare()  # STDOUT: aah!
                #         brrrr... n-e-e-e-i-g-h
# shouldn't work, but works
animal.start()  # STDOUT: brrrr... n-e-e-e-i-g-h
