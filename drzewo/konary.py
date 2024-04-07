from galezie import *

class Konar:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        print("Konar.")
        self.galezie = []
        liczba_galezi = 5
        for numer in range(0, liczba_galezi):
            self.galezie.append(Galaz())

    def zwroc_galaz(self, numer):
        return self.galezie[numer]
