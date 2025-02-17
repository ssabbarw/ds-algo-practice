from lld.parking_lot.payment_processor import PaymentProcessor


class ExitPoint:
    def __init__(self, automated_panel, attendant):
        self.automated_panel = automated_panel
        self.attendant = attendant


    def process_payment_with_automated_panel(self):
        ExitPoint.__process_payment(self.automated_panel)

    def process_payment_with_attendant(self):
        ExitPoint.__process_payment(self.attendant)


    @staticmethod
    def __process_payment(payment_processor: PaymentProcessor):
        processed = False

        while not processed:
            processed = payment_processor.process_payment()

        return True