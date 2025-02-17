from abc import ABC, abstractmethod

from lld.parking_lot.parking_ticket import ParkingTicket
from lld.parking_lot.payment_strategy import PaymentStrategy


class PaymentProcessor(ABC):

    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def process_payment(self, parking_ticket: ParkingTicket):
        self.greet()
        payment_mode = input("Please choose a payment mode: Card or Cash")
        self.payment_strategy.process_payment(payment_mode, parking_ticket)

    @abstractmethod
    def greet(self):
        pass


class Attendant(PaymentProcessor):

    def __init__(self, payment_strategy: PaymentStrategy, name: str):
        self.name = name
        super().__init__(payment_strategy)

    def greet(self):
        print(f"Hello, My name is {self.name}.\nPlease wait while I process your parking ticket")


class AutomatedExitPanel(PaymentProcessor):

    def greet(self):
        print(f"This automated panel welcomes you,\nPlease wait while I process your parking ticket")