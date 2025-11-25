class MiejsceTeatralne:
    def __init__(self, numer, cena, udogodnienia=None):
        self.numer = numer
        self.cena = cena
        self.udogodnienia = udogodnienia if udogodnienia else []
        self.dostepne = True

    def zarezerwuj(self):
        if self.dostepne:
            self.dostepne = False
            return True
        return False

    def anuluj_rezerwacje(self):
        self.dostepne = True

    def __str__(self):
        status = "wolne" if self.dostepne else "zajęte"
        return f"Miejsce {self.numer}: {status}, cena: {self.cena} PLN"


class MiejsceZwykle(MiejsceTeatralne):
    def __init__(self, numer):
        super().__init__(numer, cena=20)


class MiejsceVIP(MiejsceTeatralne):
    def __init__(self, numer):
        super().__init__(numer, cena=50, udogodnienia=["lepszy widok", "więcej miejsca"])


class MiejsceDlaNiepelnosprawnych(MiejsceTeatralne):
    def __init__(self, numer):
        super().__init__(numer, cena=15, udogodnienia=["miejsce przy przejściu"])