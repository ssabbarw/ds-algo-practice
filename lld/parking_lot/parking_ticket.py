import datetime

class ParkingTicket:
    Payment_Done = "done"
    Payment_Pending = "pending"

    def __init__(self, start_time):
        self.start_time = start_time
        self.end_time = None
        self.payment_status = ParkingTicket.Payment_Pending

    def close_ticket(self):
        if self.end_time is None:
            self.end_time = datetime.datetime.now()

    def numer_of_hours(self):
        self.close_ticket()
        return self.end_time - self.end_time + 1


