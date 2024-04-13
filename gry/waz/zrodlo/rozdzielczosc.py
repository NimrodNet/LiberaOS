import pygame

class Rozdzielczosc:

    def ustaw(self, szerokosc, wysokosc):
        try:
            return pygame.display.set_mode((szerokosc, wysokosc))
        except:
            print("Klasa Rozdzielczosc, metoda ustaw(). \n" +
            "Nie można ustawić rozdzielczości.")
            return False
