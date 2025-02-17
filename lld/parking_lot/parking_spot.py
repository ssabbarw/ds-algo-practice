from lld.parking_lot.constants import ParkingSpotType
from lld.parking_lot.payment_strategy import PaymentStrategy, EVChargingPaymentStrategy
from lld.parking_lot.vehicles import Vehicle, ElectricVehicleDecorator


class ParkingSpot:
    def __init__(self, spot_type: ParkingSpotType):
        self.type = spot_type



class ElectricPanelParkingSpotDecorator:

    def __init__(self, payment_strategy: EVChargingPaymentStrategy, parking_spot: ParkingSpot):
        self.payment_strategy = payment_strategy
        self.payment_spot = parking_spot

    def charge_vehicle(self, vehicle: ElectricVehicleDecorator):
        vehicle.charge()

    def process_payment(self):
        self.payment_strategy.process_payment()






