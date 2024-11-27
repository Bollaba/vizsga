from AutoKolcsonzo import AutoKolcsonzo
from SzemelyAuto import SzemelyAuto
from TeherAuto import TeherAuto
from Berles import Berles
from datetime import date
class BookingSystem:
    def __init__(self):
        self._AutoKolcsonzo = AutoKolcsonzo("1Napra Kölcsönző Kft")
        self._init_data()
    def _init_data(self):
        self._AutoKolcsonzo.autok = SzemelyAuto(101, 10000, "ABC-101", "Ford Focus")
        self._AutoKolcsonzo.autok = SzemelyAuto(102, 15000, "ABC-102", "Volkswagen Golf")
        self._AutoKolcsonzo.autok = TeherAuto(103, 20000, "ABC-103", "IFA")



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
                auto = int(input("Add meg az autó sorszámát, amit szeretnél lefoglalni!"))
                self._AutoKolcsonzo.book_by_sorszam(auto)
            elif choice == "3":
                auto = int(input("Add meg az autó sorszámát, amit szeretnél lemondani!"))
                self._AutoKolcsonzo.unbook_by_sorszam(auto)
            elif choice == "4":
                break
booking_system = BookingSystem()
booking_system.user_interact()