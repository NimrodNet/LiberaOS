from konary import *

class Pien:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        print("Pień.")
        self.konary = []
        liczba_konarow = 20
        for numer in range(0, liczba_konarow):
            self.konary.append(Konar())
