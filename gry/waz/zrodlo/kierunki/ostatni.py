class Ostatni:

    def ustaw(self, kierunki):
        try:
            dlugosc = len(kierunki)
            ostatni_indeks = dlugosc - 1
            ostatni = kierunki[ostatni_indeks]
            return True
        except:
            print("Klasa Ostatni, metoda ustaw(). " +
            "Nie można ustawić ostatniego elementu.")
            return False
