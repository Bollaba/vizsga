from abc import ABC, abstractmethod
class Auto(ABC):
    def __init__(self, sorszam, dij, rendszam, tipus):
        self.sorszam = sorszam
        self.dij = dij
        self.rendszam = rendszam
        self.tipus = tipus
        self.is_booked = False
        self.extras = []
    @abstractmethod
    def book_auto(self):
        pass
    @abstractmethod
    def unbook_auto(self):
        pass