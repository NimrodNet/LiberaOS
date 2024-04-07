from liscie import *
from owoce import *

class Galaz:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        print("Gałąź.")
        self.liscie = []
        self.owoce = []
        liczba_lisci = 20
        liczba_owocow = 4
        for numer in range(0, liczba_lisci):
            self.liscie.append(Lisc())
        for numer in range(0, liczba_owocow):
            self.owoce.append(Owoc())
