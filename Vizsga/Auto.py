from abc import ABC
class Auto(ABC):
    def __init__(self, rendszam, tipus, price):
        self.rendszam = rendszam
        self.tipus =tipus
        self.dij = dij
        self.is_booked = False
        self.extras = []
    def book_auto(self):
        pass
    def unbook_auto(self):
        pass