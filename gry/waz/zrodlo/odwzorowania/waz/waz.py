from zrodlo.odwzorowania.waz.miejsce import *

class Waz:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        try:
            self.miejsce = Miejsce()
            return True
        except:
            print("Klasa Waz, metoda inicjuj()." +
            "Nie można zainicjować węża.")
            return False
