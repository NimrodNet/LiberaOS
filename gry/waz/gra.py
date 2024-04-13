import pygame
from zrodlo.rozdzielczosc import *
from zrodlo.sterowanie import *

class Gra:

    def __init__(self):
        self.inicjuj()
        self.graj()

    def inicjuj(self):
        try:
            self.zwroc_instancje().init()
            print("Zainicjowałem grę.")
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
            rozdzielczosc = Rozdzielczosc()
            return rozdzielczosc.ustaw(szerokosc, wysokosc)
        except:
            print("Klasa Waz, metoda ustaw_rozdzielczosc(). \n" +
            "Nie można ustawić rozdzielczości.")
            return False

    def zwroc_czas(self):
        try:
            return self.zwroc_instancje().time
        except:
            print("Klasa Waz, metoda zwroc_czas(). \n" +
            "Nie można zwrócić czasu.")
            return False

    def zwroc_zegar(self):
        try:
            return self.zwroc_czas().Clock()
        except:
            print("Klasa Waz, metoda zwroc_zegar(). \n" +
            "Nie można zwrócić zegara.")
            return False

    def zwroc_czestotliwosc(self):
        try:
            return 60
        except:
            print("Klasa Waz, metoda zwroc_czestotliwosc(). \n" +
            "Nie można zwrócić częstotliwości.")
            return False

    def uruchom_sterowanie(self, gra, kierunek):
        try:
            sterowanie = Sterowanie()
            kierunek = sterowanie.uruchom_sterowanie(gra, kierunek)
            return kierunek
        except:
            print("Klasa Waz, metoda uruchom_sterowanie(). \n" +
            "Nie można uruchomić sterowania.")
            return False

    def graj(self):
        try:
            print("Gramy.")
            gra = self.zwroc_instancje()
            wyswietlacz = self.ustaw_rozdzielczosc(1280, 720)
            zegar = self.zwroc_zegar()
            flaga_gry = True
            przycisk = ""
            kierunek = [1, 0, 0, 0]
            indeks = 0
            sterowanie = Sterowanie()
            while flaga_gry:
                for wydarzenie in gra.event.get():
                    if wydarzenie.type == gra.QUIT:
                        flaga_gry = False
                wyswietlacz.fill("black")
                kierunek = sterowanie.uruchom_sterowanie(gra, kierunek)
                if indeks % 104 == 0:
                    liczba_kierunkow = sterowanie.zwroc_rozmiar_historii_kierunkow()
                    print(liczba_kierunkow)
                    indeks = 0
                gra.display.flip()
                czestotliwosc = self.zwroc_czestotliwosc()
                zegar.tick(czestotliwosc)
                indeks += 1
            gra.quit()
            return True
        except:
            print("Klasa Waz, metoda graj(). \n" +
            "Nie można uruchomić gry.")
            return False
