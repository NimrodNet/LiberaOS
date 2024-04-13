from gra import *

class Waz:

    def __init__(self):
        self.inicjuj()

    def inicjuj(cls):
        try:
            Gra()
            return True
        except:
            print("Klasa Waz, metoda inicjuj(). \n" +
            "Nie można zainicjować gry.")

Waz()
