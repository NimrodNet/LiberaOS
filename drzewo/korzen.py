from pien import *

class Korzen:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        print("Korzeń.")
        self.pien = Pien()

    def zwroc_pien(self):
        return self.pien
