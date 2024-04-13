import pygame

class Inicjacja:

    def __init__(self):
        self.inicjuj()

    def inicjuj(cls):
        try:
            pygame.init()
            return True
        except:
            print("Klasa Inicjacja, metoda inicjuj(). \n" +
            "Nie można zainicjować gry.")
            return False
