from abc import ABC, abstractmethod
from enums import Color, Size


class Vehicle(ABC):
    def __init__(self, license_plate, color, size):
        self.__license_plate = license_plate
        self.__color = color
        self.__size = size

    def get_size(self):
        return self.__size

    def get_license(self):
        return self.__license_plate


class Bike(Vehicle):
    def __init__(self, license_plate, color):
        super().__init__(license_plate, color, Size.SMALL)


class Car(Vehicle):
    def __init__(self, license_plate, color):
        super().__init__(license_plate, color, Size.MEDIUM)


class Truck(Vehicle):
    def __init__(self, license_plate, color):
        super().__init__(license_plate, color, Size.LARGE)


class Bus(Vehicle):
    def __init__(self, license_plate, color):
        super().__init__(license_plate, color, Size.XLARGE)




