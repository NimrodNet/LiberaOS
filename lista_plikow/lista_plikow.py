import os

class Lista_plikow:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        try:
            self.lista_plikow = []
            return True
        except:
            print("Klasa Lista_plikow, metoda inicjuj(). \n" + 
            "Nie można zainicjować listy plików.")
            return False
