from lld.parking_lot.constants import ParkingSpotType
from lld.parking_lot.display_board import DisplayBoard
from lld.parking_lot.entry_point import EntryPoint
from lld.parking_lot.exit_point import ExitPoint
from lld.parking_lot.floor import Floor
from lld.parking_lot.information_portal import InformationPortal

from lld.parking_lot.payment_processor import AutomatedExitPanel, Attendant, PaymentProcessor
from lld.parking_lot.payment_strategy import ParkingTicketHourlyPaymentStrategy, EVChargingPaymentStrategy
from lld.parking_lot.vehicles import Vehicle


class ParkingLot:
    def __init__(self,number_of_entries, number_of_exits, number_of_floors, n_cars_each_floor, n_trucks_each_floor
                 , n_vans_each_floor, n_motorcycles_each_floor, n_evs_each_floor):

        parking_lot_parking_spots_capacity_map ={
            ParkingSpotType.Car: n_cars_each_floor * number_of_floors,
            ParkingSpotType.Truck: n_trucks_each_floor * number_of_floors,
            ParkingSpotType.Van: n_vans_each_floor * number_of_floors,
            ParkingSpotType.MotorCycle: n_motorcycles_each_floor * number_of_floors,
            ParkingSpotType.EV: n_evs_each_floor * number_of_floors,
        }

        entry_display_boards = [DisplayBoard(parking_lot_parking_spots_capacity_map)] * number_of_entries
        self.entrance_panel = DisplayBoard(parking_lot_parking_spots_capacity_map)

        self.parking_payment_strategy = ParkingTicketHourlyPaymentStrategy()

        self.entries = [EntryPoint(entry_display_boards[i]) for i in range(number_of_entries)]
        self.exits = [ExitPoint(AutomatedExitPanel(payment_strategy=self.parking_payment_strategy)
                           , Attendant(payment_strategy=self.parking_payment_strategy, name="Your attendant"))] * number_of_exits

        self.ev_charging_payment_strategy = EVChargingPaymentStrategy()

        self.floors = []

        parking_floor_parking_spots_capacity_map = {
            ParkingSpotType.Car: n_cars_each_floor,
            ParkingSpotType.Truck: n_trucks_each_floor,
            ParkingSpotType.Van: n_vans_each_floor,
            ParkingSpotType.MotorCycle: n_motorcycles_each_floor,
            ParkingSpotType.EV: n_evs_each_floor,
        }

        for i in number_of_floors:
            self.floors.append(Floor(
                i,
                InformationPortal(payment_strategy=self.parking_payment_strategy),
                [entry_display_boards, DisplayBoard(parking_floor_parking_spots_capacity_map)],
                {ParkingSpotType.Car: n_cars_each_floor,
                 ParkingSpotType.Truck: n_trucks_each_floor,
                    ParkingSpotType.Van: n_vans_each_floor,
                 ParkingSpotType.MotorCycle: n_motorcycles_each_floor,
                 ParkingSpotType.EV: n_evs_each_floor}))

    def vehicle_entry(self, entry_point: EntryPoint,vehicle: Vehicle):
        vehicle.set_parking_ticket(entry_point.issue_ticket())

    def vehicle_exit(self, exit_point: ExitPoint, vehicle: Vehicle, payment_processor: PaymentProcessor):

        if type(payment_processor) is Attendant:
            exit_point.attendant.process_payment(vehicle.parking_ticket)
        else:
            exit_point.automated_panel.process_payment(vehicle.parking_ticket)

