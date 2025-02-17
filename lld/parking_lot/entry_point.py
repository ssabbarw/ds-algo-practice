from lld.parking_lot.display_board import DisplayBoard
from lld.parking_lot.parking_ticket import ParkingTicket


class EntryPoint:
    def __init__(self, display_board):
        self.display_board = display_board

    def issue_ticket(self):
        return ParkingTicket()
