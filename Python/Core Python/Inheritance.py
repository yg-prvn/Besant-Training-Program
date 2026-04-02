from abc import ABC, abstractmethod

class Vehicle:
    name = ""
    year = 2020

    def __init__(self, name, year):
        self.name = name
        self.year = year

    def carData(self):
        print(self.name)

    @abstractmethod
    def printModel(self):
        pass

class TypeVehicle(Vehicle):
    v_type = ""

    def __init__(self, name, year, v_type):
        super().__init__(name, year)
        self.v_type = v_type

    def printData(self):
        print(self.v_type)

    def printModel(self):
        print(self.year)

obj = TypeVehicle("Tata", 2025, "EV")
obj.printData()


'''
Access Modifiers:
Public : All ()
Private : Not even child classes, only same class (__)
Protected : Within same class & child class (_)
'''