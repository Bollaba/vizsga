from Auto import Auto
class SzemelyAuto(Auto):
    def __init__(self, sorszam, dij, rendszam, tipus):
        super().__init__(sorszam, dij, rendszam, tipus)
        self.extras = ["radio", "ulesfutes"]
    def book_auto(self):
        if not self.is_booked:
            self.is_booked = True
        else:
            print("Hiba, az autó már foglalt!")
    def unbook_auto(self):
        if self.is_booked:
            self.is_booked = False
        else:
            print("Hiba, az autó nem volt foglalt!")