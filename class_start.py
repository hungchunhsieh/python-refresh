class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed)

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if hassidecar:
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype

    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at", self.speed)

car1 = Car("gas")
car2 = Car("electric")
m1 = Motorcycle(enginetype = "gas", hassidecar = True)

print(car1.enginetype)
print(car2.enginetype)
print(m1.wheels)

car1.drive(30)
car2.drive(50)
m1.drive(80)

car_park = []

car_park.append(car1)
car_park.append(car2)
car_park.append(m1)
for i in car_park:
    if type(i) == Car:
        print(i.enginetype)
    if type(i) == Motorcycle:
        print("object:", i)

print(car_park)


