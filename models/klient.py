class Klient:
    def __init__(self, klient_id, imie, nazwisko):
        self.klient_id = klient_id
        self.imie = imie
        self.nazwisko = nazwisko
        self.historia = []

    def dodaj_rezerwacje(self, opis):
        self.historia.append(opis)

    def __str__(self):
        return f"{self.imie} {self.nazwisko} (ID: {self.klient_id})"

    def pokaz_historie(self):
        if not self.historia:
            return "Brak rezerwacji."
        return "\n".join(self.historia)