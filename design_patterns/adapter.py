class OldPaymentSystem:
    def make_transaction(self, amount_in_rupees):
        print(f"{amount_in_rupees} was paid")

class NewPaymentSystem:
    def process_payment(self, amount, currency):
        print(f"{amount} {currency} was paid")

class PaymentSystemAdapter:
    def __init__(self, old_gateway):
        self.old_gateway = old_gateway

    def process_payment(self, amount, currency):
        if currency is "inr":
            return self.old_gateway.make_transaction(amount)

        converted_inr = amount * 10

        return self.old_gateway.make_transaction(converted_inr)


