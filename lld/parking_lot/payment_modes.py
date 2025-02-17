from abc import ABC, abstractmethod

class PaymentMode(ABC):

    @abstractmethod
    def process_payment(self, amt)-> bool:
        pass

class CardPaymentMode(PaymentMode):

    def process_payment(self, amt)-> bool:

        print(f"{amt} rupees deducted from your card")
        return True

class CashPaymentMode(PaymentMode):

    def process_payment(self, amt):
        print(f"Thankyou for cash payment of rupees {amt}")
        return True

class UnknownPaymentMode(PaymentMode):

    def process_payment(self, amt):
        print(f"This payment method is not yet supported")
        return False