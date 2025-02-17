from lld.parking_lot.constants import ParkingSpotType
from lld.parking_lot.display_board import DisplayBoard
from lld.parking_lot.information_portal import InformationPortal
from typing import Dict, List

from lld.parking_lot.parking_spot import ParkingSpot
from lld.parking_lot.vehicles import Vehicle


class Floor:

    def __init__(self, floor_number, information_portal: InformationPortal,
                 display_boards: List[DisplayBoard],
                 parking_spot_capacity_map: Dict[ParkingSpotType,int]):
        self.floor_number = floor_number + 1
        self.vehicle_occupied_map :Dict[ParkingSpotType, int]= {}


        self.info_portal = information_portal
        self.display_boards = display_boards
        self.available_parking_spots :Dict[ParkingSpotType, List[ParkingSpot]] = {}

        for parking_spot_type in ParkingSpotType:
            self.available_parking_spots[parking_spot_type] = ([ParkingSpot(spot_type=parking_spot_type)]
                                                     * parking_spot_capacity_map[parking_spot_type])

            self.vehicle_occupied_map[parking_spot_type] = 0


    def add_board(self, display_board: DisplayBoard):
        self.boards.append(display_board)

    def add_vehicle(self, vehicle: Vehicle):
        if (len(self.available_parking_spots[vehicle.parking_spot_type])
                - self.vehicle_occupied_map[vehicle.parking_spot_type]< 0):
            print(f"Can not park more {vehicle.parking_spot_type} on floor number {self.floor_number}")
            return False

        self.vehicle_occupied_map[vehicle.parking_spot_type] += 1
        self.update_boards(added_vehicle_type=vehicle.parking_spot_type)



    def update_boards(self, removed_vehicle_type = None, added_vehicle_type = None):
        print(f"\n**------Floor: {self.floor_number}-----------**\n")

        for board in self.display_boards:
            board.update(self.vehicle_occupied_map, removed_vehicle_type, added_vehicle_type)

        print("\n**-----------------**\n")

    def remove_vehicle(self, vehicle: Vehicle):
        if vehicle not in self.available_parking_spots[vehicle.parking_spot_type]:
            print(f"Err: Vehicle is not parked on the floor number {self.floor_number}")
            return False


        self.available_parking_spots[vehicle.parking_spot_type].remove(vehicle)
        self.update_boards(removed_vehicle_type=vehicle.parking_spot_type)








