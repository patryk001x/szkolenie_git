class HistoriaRezerwacji:
    def __init__(self):
        self.zdarzenia = []

    def dodaj(self, opis):
        self.zdarzenia.append(opis)

    def pokaz(self):
        if not self.zdarzenia:
            return "Brak historii rezerwacji."
        return "\n".join(self.zdarzenia)