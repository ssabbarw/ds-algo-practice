from collections import defaultdict
from enum import Enum
from typing import Dict, Iterator



class ParkingSpotType(Enum):
    Car = "Car"
    Truck = "Truck"
    Van = "Van"
    MotorCycle = "Motor"
    EV = "EV"
    Empty = "Empty"


class PaymentModeTypes(Enum):
    Card = "Card"
    Cash = "Cash"
    Unknown = "Unknown"

    def __init__(self):
        self.payment_mode_types: Dict[str, ParkingSpotType] = defaultdict(PaymentModeTypes.Unknown)
        self.payment_mode_types[PaymentModeTypes.Card.lower()] = PaymentModeTypes.Card
        self.payment_mode_types[PaymentModeTypes.Cash.lower()] = PaymentModeTypes.Cash

    def get_payment_mode_type(self, payment_mode_str: str):
        return self.payment_mode_types[payment_mode_str.lower()]

