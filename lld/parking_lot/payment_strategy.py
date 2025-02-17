from abc import ABC, abstractmethod
from collections import defaultdict
from constants import PaymentModeTypes
from lld.parking_lot.parking_ticket import ParkingTicket
from payment_modes import PaymentMode, UnknownPaymentMode
from typing import Dict

class PaymentStrategy(ABC):

    def __init__(self):
        self.payment_modes: Dict[PaymentModeTypes, PaymentMode] = defaultdict(UnknownPaymentMode)

    @abstractmethod
    def calculate_dues(self, parking_ticket: ParkingTicket)-> float:
        pass

    def process_payment(self, payment_mode_str: str, parking_ticket: ParkingTicket):
        payment_mode = PaymentModeTypes.get_payment_mode_type(payment_mode_str)

        amount = self.calculate_dues(parking_ticket)
        return self.payment_modes[payment_mode].process_payment(amount)


class ParkingTicketHourlyPaymentStrategy(PaymentStrategy):

    def calculate_dues(self, parking_ticket: ParkingTicket):
        no_of_hours = parking_ticket.numer_of_hours()
        dues = 0

        if no_of_hours >= 1:
            dues += 4
            no_of_hours -= 1

        for _ in range(2):
            if no_of_hours >= 1:
                dues += 3.5
                no_of_hours -= 1

        while no_of_hours >= 1:
            dues += 2.5
            no_of_hours -= 1

        return dues

class EVChargingPaymentStrategy(PaymentStrategy):

    def calculate_dues(self, parking_ticket: ParkingTicket = None) -> float:
        return 10.0
