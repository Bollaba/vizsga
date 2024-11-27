from AutoKolcsonzo import AutoKolcsonzo
from SzemelyAuto import SzemelyAuto
from TeherAuto import TeherAuto

class BookingSystem:
    def __init__(self):
        self._AutoKolcsonzo = AutoKolcsonzo("1Napra Kölcsönző Kft")
        self._init_data()
    def _init_data(self):
        self._AutoKolcsonzo.autok = SzemelyAuto(101, 10000)
        self._AutoKolcsonzo.autok = SzemelyAuto(102, 10000)
        self._AutoKolcsonzo.autok = TeherAuto(103, 10000)

    def user_interact(self):
        while True:
            print("1. Autók listázása")
            print("2, Autó foglalása")
            print("3. Autó lemondása")
            print("4. Kilépés")
            choice = input("Válasz a fenti menüpontok közül: ")
            if choice == "1":
                self._AutoKolcsonzo.autok
            elif choice == "2":
                auto = int(input("Add meg az autó rendszámát, amit szeretnél lefoglalni!"))
                self._AutoKolcsonzo.book_by_rendszam(auto)
            elif choice == "3":
                auto = int(input("Add meg az autó rendszámát, amit szeretnél lemondani!"))
                self._AutoKolcsonzo.unbook_by_rendszam(auto)
            elif choice == "4":
                break
booking_system = BookingSystem()
booking_system.user_interact()