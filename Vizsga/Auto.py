from abc import ABC, abstractmethod
class Auto(ABC):
    def __init__(self, rendszam, dij):
        self.rendszam = rendszam
        self.dij = dij
        self.is_booked = False
        self.extras = []
    @abstractmethod
    def book_auto(self):
        pass
    @abstractmethod
    def unbook_auto(self):
        pass