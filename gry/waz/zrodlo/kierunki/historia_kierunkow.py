class Historia_kierunkow:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        try:
            self.historia_kierunkow = []
            return True
        except:
            print("Klasa Historia_kierunkow, metoda inicjuj(). " +
            "Nie można zainicjować historii kierunków.")
            return False

    def zwroc(self):
        try:
            return self.historia_kierunkow
        except:
            print("Klasa Historia_kierunkow, metoda zwroc(). " + 
            "Nie można zwrócić historii kierunków.")
            return False

    def dodaj(self, kierunek):
        try:
            self.zwroc().append(kierunek)
            return True
        except:
            print("Klasa Historia_kierunkow, metoda dodaj(). " + 
            "Nie można dodać historii kierunków.")
            return False

    def zwroc_ostatni(self):
        try:
            dlugosc = len(self.zwroc())
            indeks = dlugosc - 1
            return self.zwroc()[indeks]
        except:
            print("Klasa Historia_kierunkow, metoda zwroc_ostatni(). " + 
            "Nie można dodać historii kierunków.")
            return False
