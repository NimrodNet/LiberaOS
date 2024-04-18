import math
from PIL import Image, ImageDraw

class Grafika:

    def stworz(self, rozmiar, kolor):
        szerokosc = rozmiar[0]
        wysokosc = rozmiar[1]
        czerwony = kolor[0]
        zielony = kolor[1]
        niebieski = kolor[2]
        grafika = Image.new("RGB", (szerokosc, wysokosc), (czerwony, zielony, niebieski))
        self.grafika = grafika

    def zwroc(self):
        return self.grafika

    def pokaz(self):
        self.grafika.show()

class Rysunek:

    def stworz(self, grafika):
        self.rysunek = ImageDraw.Draw(grafika)

    def zwroc(self):
        return self.rysunek

class Prostokat:

    def rysuj(self, rysunek, rozmiar):
        szerokosc = rozmiar[0]
        wysokosc = rozmiar[1]
        x = rozmiar[2]
        y = rozmiar[3]
        szerokosc = szerokosc + x
        wysokosc = wysokosc + y
        ksztalt = [ (x, y), (szerokosc, wysokosc) ]
        rysunek.rectangle(ksztalt, fill="white", outline="black")


przybornik = Grafika()
przybornik.stworz([200, 200], [32, 46, 125])
grafika = przybornik.zwroc()

rysunek = Rysunek()
rysunek.stworz(grafika)
plotno = rysunek.zwroc()

prostokat = Prostokat()
prostokat.rysuj(plotno, [50, 50, 0, 0])

przybornik.pokaz()
