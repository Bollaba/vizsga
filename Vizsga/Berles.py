from datetime import date
from Auto import Auto
class Berles:
    def __init__(self, auto, berles_napja, foglalas_datuma=None):
        self.auto = auto
        self.berles_napja = berles_napja
        self.foglalas_datuma = foglalas_datuma
        self._berlesek = []

    @property
    def berlesek(self):
        for berles in self._berlesek:
            print(f" Rendszám: {Auto.rendszam}, Bérlés napja: {berles.is_booked}, foglalas_datuma{None}")

    @berlesek.setter
    def berlesek(self, new_berles):
        self._berlesek.append(new_berles)

    def _init_data(self):
        self.berlesek = Berles("ABC-101", "2024.12.10", "2024.11.25")
        self.berlesek = Berles("ABC-102", "2024.12.15", "2024.11.24")
        self.berlesek = Berles("ABC-103", "2024.12.16","2024.11.20")
        self.berlesek = Berles("ABC-101", "2024.12.17", '2024.10.10')
    def __str__(self):

        if self.foglalas_datuma <= self.berles_napja:
            return f"Az autó {self.auto.rendszam} {self.foglalas_datuma}-án lett lefoglalva {self.berles_napja}-ra."
        else:
            return f"Nem megfelelő dátumot adot meg. A bérlés napja vagy a mai nap, vagy egy jövőbeni nap lehet."


