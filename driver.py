from parking_lot import ParkingLot
from vehicle import Vehicle, Car, Bike
from enums import Color, Size

Parking_Lot = ParkingLot('1', '500038', 5, 5, 5, 5)
honda_city = Car('TS09ER5767', Color.WHITE)
hero_honda = Bike('TS09ER9999', Color.BLACK)

print(Parking_Lot.assign(honda_city))
print(Parking_Lot.assign(hero_honda))
Parking_Lot.print_parking_lot()


# Parking_Lot.free(honda_city)
# Parking_Lot.print_parking_lot()

