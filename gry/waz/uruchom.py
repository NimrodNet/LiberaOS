import pygame
from zrodlo.inicjacja import *

class Waz:

    def __init__(self):
        self.inicjuj()
        self.graj()

    def inicjuj(self):
        try:
            self.zwroc_instancje().init()
            return True
        except:
            print("Klasa Waz, metoda inicjuj(). \n" +
            "Nie można zainicjować gry.")
            return False

    def zwroc_instancje(cls):
        try:
            return pygame
        except:
            print("Klasa Waz, metoda zwroc_instancje(). \n" +
            "Nie można zwrócić instancji gry.")
            return False

    def ustaw_rozdzielczosc(self, szerokosc, wysokosc):
        try:
            return self.zwroc_instancje().display.set_mode((szerokosc, wysokosc))
        except:
            print("Klasa Waz, metoda ustaw_rozdzielczosc(). \n" +
            "Nie można ustawić rozdzielczości.")
            return False

    def zwroc_zegar(self):
        try:
            return self.zwroc_instancje().time.Clock()
        except:
            print("Klasa Waz, metoda ustaw_rozdzielczosc(). \n" +
            "Nie można ustawić rozdzielczości.")
            return False

    def zwroc_czestotliwosc(self):
        try:
            return 60
        except:
            print("Klasa Waz, metoda zwroc_czestotliwosc(). \n" +
            "Nie można zwrócić częstotliwości..")
            return False

    def graj(self):
        try:
            gra = self.zwroc_instancje()
            wyswietlacz = self.ustaw_rozdzielczosc(1280, 720)
            zegar = self.zwroc_zegar()
            flaga_gry = True
            while flaga_gry:
                for wydarzenie in gra.event.get():
                    if wydarzenie.type == gra.QUIT:
                        flaga_gry = False
                wyswietlacz.fill("purple")
                gra.display.flip()
                czestotliwosc = self.zwroc_czestotliwosc()
                zegar.tick(czestotliwosc)
            gra.quit()
            return True
        except:
            print("Klasa Waz, metoda graj(). \n" +
            "Nie można uruchomić gry.")
            return False

Waz()
