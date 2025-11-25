from models.klient import Klient
from theater.teatr import Teatr


class Interfejs:
    def __init__(self):
        self.teatr = Teatr()
        self.klient = None

    def zaloguj_klienta(self):
        print("=== Logowanie klienta ===")
        klient_id = input("Podaj ID klienta: ")
        imie = input("Podaj imię: ")
        nazwisko = input("Podaj nazwisko: ")
        self.klient = Klient(klient_id, imie, nazwisko)
        print("Zalogowano pomyślnie!")

    def pokaz_menu(self):
        print("\n=== MENU ===")
        print("1. Wyświetl dostępne miejsca")
        print("2. Zarezerwuj miejsce")
        print("3. Anuluj rezerwację")
        print("4. Historia rezerwacji")
        print("5. Wyjście")

    def start(self):
        self.zaloguj_klienta()

        while True:
            self.pokaz_menu()
            wybor = input("Wybierz opcję (1-5): ")

            if wybor == "1":
                print("\n=== LISTA MIEJSC ===")
                print(self.teatr.pokaz_miejsca())

            elif wybor == "2":
                numer = int(input("Podaj numer miejsca do rezerwacji: "))
                wynik = self.teatr.zarezerwuj(numer, self.klient)
                print(wynik)

            elif wybor == "3":
                numer = int(input("Podaj numer miejsca do anulowania: "))
                wynik = self.teatr.anuluj(numer, self.klient)
                print(wynik)

            elif wybor == "4":
                print("\n=== HISTORIA TWOICH REZERWACJI ===")
                print(self.klient.pokaz_historie())

            elif wybor == "5":
                print("Do zobaczenia!")
                break

            else:
                print("Niepoprawna opcja, spróbuj ponownie.")