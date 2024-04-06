from pobierz import *

pobierz = [Pobierz()]
pliki = pobierz[0]
sciezki = ["pliki/"]
pliki.pobierz(sciezki)
pliki.sortuj(True)
pliki.ustaw_sciezki_z_zakresu(0, 2)
pliki.wyswietl()
