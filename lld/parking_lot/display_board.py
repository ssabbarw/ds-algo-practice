from typing import Dict

from lld.parking_lot.constants import ParkingSpotType


class DisplayBoard:

    def __init__(self, parking_spots_capacity_map: Dict[ParkingSpotType, int]):
        self.parking_spots_capacity_map = parking_spots_capacity_map
        self.parking_spots_used_map = {}

        for parking_spot_type in ParkingSpotType:
            self.parking_spots_used_map[parking_spot_type] = 0

    def update(self, removed_vehicle_type=None, added_vehicle_type = None):

        print(f"\n**------Floor: {self.floor_number}-----------**\n")

        string = ""
        for parking_spot_type in ParkingSpotType:

            if parking_spot_type == removed_vehicle_type:
                self.parking_spots_used_map[parking_spot_type] -= 1

            if parking_spot_type == added_vehicle_type:
                self.parking_spots_used_map[parking_spot_type] += 1

            string += (f'''\nAvailable {parking_spot_type} parking spots:
                       f"{len(self.parking_spots_capacity_map[parking_spot_type]) 
                          - self.parking_spots_used_map[parking_spot_type]}''')

        for board in self.display_boards:
            board.display(string)

        print("\n**-----------------**\n")

        print(string)

