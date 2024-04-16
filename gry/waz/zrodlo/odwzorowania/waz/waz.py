from zrodlo.odwzorowania.waz.miejsce import *

class Waz:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        try:
            self.miejsce = [Miejsce()]
            return True
        except:
            print("Klasa Waz, metoda inicjuj()." +
            "Nie można zainicjować węża.")
            return False

    def zwroc(self):
        try:
            return self.miejsce
        except:
            print("Klasa Waz, metoda zwroc()." +
            "Nie można zwrócić położenia.")
            return False

    def na(self, indeks):
        try:
            return self.zwroc()[indeks]
        except:
            print("Klasa Waz, metoda miejsce()." +
            "Nie można określić położenia.")
            return False

    def rozmiar(self):
        try:
            return len(self.zwroc())
        except:
            print("Klasa Waz, metoda rozmiar()." +
            "Nie można zwrócić rozmiaru..")
            return False

    def wyswietl(self):
        try:
            rozmiar = self.rozmiar()
            for indeks in range(0, rozmiar):
                miejsce = self.na(indeks)
                print(miejsce.zwroc())
            return True
        except:
            print("Klasa Waz, metoda wyświetl()." +
            "Nie można wyświetlić położenia węża.")
            return False
