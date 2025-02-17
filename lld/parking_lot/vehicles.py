from abc import ABC, abstractmethod

from lld.parking_lot.constants import ParkingSpotType
from lld.parking_lot.parking_ticket import ParkingTicket


class Vehicle(ABC):

    def __init__(self, parking_requirement, parking_spot_type: ParkingSpotType):
        self.parking_req = parking_requirement
        self.parking_spot_type = parking_spot_type
        self.parking_ticket = None

    def set_parking_ticket(self, parking_ticket: ParkingTicket):
        self.parking_ticket = parking_ticket

class ElectricVehicleDecorator:

    def __init__(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.full_charge = False

    def charge(self):
        self.full_charge = True