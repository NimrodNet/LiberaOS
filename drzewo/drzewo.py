from korzen import *

class Drzewo:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        print("Drzewo.")
        self.korzen = Korzen()

    def zwroc_korzen(self):
        return self.korzen
