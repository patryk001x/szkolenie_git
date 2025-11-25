from models.miejsce import (
    MiejsceZwykle,
    MiejsceVIP,
    MiejsceDlaNiepelnosprawnych
)


class Teatr:
    def __init__(self):
        self.miejsca = []
        self.utworz_miejsca()

    def utworz_miejsca(self):
        # 1–10: miejsca zwykłe
        for i in range(1, 11):
            self.miejsca.append(MiejsceZwykle(i))

        # 11–15: miejsca VIP
        for i in range(11, 16):
            self.miejsca.append(MiejsceVIP(i))

        # 16–18: miejsca dla niepełnosprawnych
        for i in range(16, 19):
            self.miejsca.append(MiejsceDlaNiepelnosprawnych(i))

    def pokaz_miejsca(self):
        return "\n".join(str(m) for m in self.miejsca)

    def znajdz_miejsce(self, numer):
        for miejsce in self.miejsca:
            if miejsce.numer == numer:
                return miejsce
        return None

    def zarezerwuj(self, numer, klient):
        miejsce = self.znajdz_miejsce(numer)
        if miejsce is None:
            return "Nie ma takiego miejsca!"

        if miejsce.dostepne:
            miejsce.zarezerwuj()
            opis = f"Klient {klient.imie} {klient.nazwisko} zarezerwował miejsce {numer} (cena: {miejsce.cena} PLN)"
            klient.dodaj_rezerwacje(opis)
            return "Rezerwacja udana!"
        else:
            return "Miejsce jest już zajęte!"

    def anuluj(self, numer, klient):
        miejsce = self.znajdz_miejsce(numer)
        if miejsce is None:
            return "Nie ma takiego miejsca!"

        if not miejsce.dostepne:
            miejsce.anuluj_rezerwacje()
            opis = f"Klient {klient.imie} {klient.nazwisko} anulował rezerwację miejsca {numer}"
            klient.dodaj_rezerwacje(opis)
            return "Rezerwacja anulowana!"
        else:
            return "Miejsce nie jest zarezerwowane."