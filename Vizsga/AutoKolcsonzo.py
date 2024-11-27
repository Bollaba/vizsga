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
            print(f" Sorszám:{auto.sorszam}, Rendszám: {auto.rendszam},Típus:{auto.tipus}, Bérletidíj: {auto.dij} huf - Foglalt: {auto.is_booked}")
    @autok.setter
    def autok(self, new_auto):
        self._autok.append(new_auto)
    def book_by_sorszam(self, sorszam):
        for auto in self._autok:
            if auto.sorszam == sorszam:
                return auto.book_auto()
    def unbook_by_sorszam(self, sorszam):
        for auto in self._autok:
            if auto.sorszam == sorszam:
                return auto.unbook_auto()