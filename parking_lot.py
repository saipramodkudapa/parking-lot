from spot import Spot
from vehicle import Vehicle
from enums import Size, Color
from collections import deque


class ParkingLot:
    def __init__(self, _id, zipcode, num_small, num_medium, num_large, num_xlarge):
        self.___id = _id
        self.__zipcode = zipcode
        self.__small_slots = deque([Spot('S'+str(i), Size.SMALL) for i in range(num_small)])
        self.__medium_slots = deque([Spot('M'+str(i), Size.MEDIUM) for i in range(num_medium)])
        self.__large_slots = deque([Spot('L'+str(i), Size.LARGE) for i in range(num_large)])
        self.__xlarge_slots = deque([Spot('XL'+str(i), Size.XLARGE) for i in range(num_xlarge)])
        self.assigned_slots = {}

    def switcher(self, type):
        mapping = {
            Size.SMALL: self.__small_slots,
            Size.MEDIUM: self.__medium_slots,
            Size.LARGE: self.__large_slots,
            Size.XLARGE: self.__xlarge_slots
        }
        return mapping.get(type, None)

    def assign(self, vehicle: Vehicle) -> Spot:
        vehicle_type = vehicle.get_size()
        free_slots = self.switcher(vehicle_type)

        if free_slots:
            assigned_slot = free_slots.popleft()
            self.assigned_slots[vehicle.get_license()] = assigned_slot
            return assigned_slot.get_spot_id()
        else:
            print('Invalid Vehicle Size')

    def free(self, vehicle: Vehicle):
        if vehicle.get_license() not in self.assigned_slots:
            print('Vehicle not parked')
            return None
        assigned_slot = self.assigned_slots[vehicle.get_license()]
        slots = self.switcher(vehicle.get_size())
        slots.appendleft(assigned_slot)
        del self.assigned_slots[vehicle.get_license()]
        return assigned_slot

    def is_full(self) -> bool:
        small = len(self.__small_slots) == 0
        medium = len(self.__small_slots) == 0
        large = len(self.__large_slots) == 0
        xlarge = len(self.__xlarge_slots) == 0
        return small and medium and large and xlarge

    def print_parking_lot(self):

        print('small slots', len(self.__small_slots))
        print('medium slots', len(self.__medium_slots))
        print('large slots', len(self.__large_slots))
        print('X-large slots', len(self.__xlarge_slots))
