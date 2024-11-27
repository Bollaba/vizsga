class AutoKolcsonzo:
    def __init__(self, name):
        self._name = name
        self._autok = []
    @property
    def name(self):
        return self._name
    @property
    def autok(self):
        for auto in self._autok:
            print(f" Rendszám: {auto.rendszam}, Bérletidíj: {auto.dij} huf - Foglalt: {auto.is_booked}")
    @autok.setter
    def autok(self, new_auto):
        self._autok.append(new_auto)
    def book_by_rendszam(self, rendszam):
        for auto in self._autok:
            if auto.rendszam == rendszam:
                return auto.book_auto()
    def unbook_by_rendszam(self, rendszam):
        for auto in self._autok:
            if auto.rendszam == rendszam:
                return auto.unbook_auto()