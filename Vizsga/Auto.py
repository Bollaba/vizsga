from abc import ABC
class Auto(ABC):
    def __init__(self, rendszam, dij):
        self.rendszam = rendszam
        self.dij = dij
        self.is_booked = False
        self.extras = []
    def book_auto(self):
        pass
    def unbook_auto(self):
        pass