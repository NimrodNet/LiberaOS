import glob
import os

class Pobierz:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        try:
            self.ustaw([])
            return True
        except:
            print("Klasa Pobierz_liste_plikow, metoda inicjuj(). \n" + 
            "Nie można zainicjować listy plików.")
            return False

    def ustaw(self, lista_plikow):
        try:
            self.lista_plikow = lista_plikow
            return True
        except:
            print("Klasa Pobierz, metoda ustaw(). \n" + 
            "Nie można ustawić listy plików.")
            return False

    def zwroc(self):
        try:
            return self.lista_plikow
        except:
            print("Klasa Pobierz, metoda zwroc(). \n" + 
            "Nie można zwrócić listy plików.")
            return False

    def zwroc_etykiety_plikow(self, sciezki):
        try:
            etykiety = []
            for sciezka in sciezki:
                etykieta = os.path.basename(sciezka)
                etykiety.append(etykieta)
            return etykiety
        except:
            print("Klasa Pobierz, metoda zwroc_etykiety_plikow(). \n" + 
            "Nie można zwrócić etykiet plików.")
            return False

    def ustaw_sciezki(self, numery_sciezek):
        try:
            pliki = self.zwroc()
            sciezki = []
            liczba_sciezek = len(numery_sciezek)
            for indeks in range(0, liczba_sciezek):
                numer_sciezki = numery_sciezek[indeks]
                sciezka = pliki[numer_sciezki]
                sciezki.append(sciezka)
            self.ustaw(sciezki)
            return self.zwroc()
        except:
            print("Klasa Pobierz, metoda ustaw_sciezki(). \n" + 
            "Nie można ustawić ścieżek.")
            return False

    def ustaw_sciezki_z_zakresu(self, od, do):
        try:
            pliki = self.zwroc()
            sciezki = []
            zakres = []
            for numer in range(od, do + 1):
                zakres.append(numer)
            self.ustaw_sciezki(zakres)
            return self.zwroc()
        except:
            print("Klasa Pobierz, metoda ustaw_sciezki_z_zakresu(). \n" + 
            "Nie można ustawić ścieżek z zakresu.")
            return False

    def pobierz(self, sciezki, wszystkie = True):
        try:
           lista_plikow = []
           sciezki_to_znaki = type(sciezki) == str
           lista_sciezek = sciezki
           if sciezki_to_znaki:
               lista_sciezek = [sciezki]
           for sciezka in lista_sciezek:
               sciezka = os.path.abspath(sciezka) + "/"
               pliki = glob.glob(sciezka + "**", recursive = wszystkie)
               for plik in pliki:
                   lista_plikow.append(plik)
           self.ustaw(lista_plikow)
           return self.zwroc()
        except:
            print("Klasa Pobierz, metoda pobierz(). \n" +
            "Nie udało się pobrać listy plików.")
            return False

    def sortuj(self, odwrotnie=False):
        try:
           pliki = self.zwroc()
           pliki.sort(reverse=odwrotnie)
           self.ustaw(pliki)
           return self.zwroc()
        except:
            print("Klasa Pobierz, metoda sortuj(). \n" +
            "Nie udało się posortować listy plików.")
            return False

    def wyswietl(self):
        try:
           pliki = self.zwroc()
           for plik in pliki:
               print(plik)
           return self.zwroc()
        except:
            print("Klasa Pobierz, metoda wyswietl(). \n" +
            "Nie udało się wyświetlić listy plików.")
            return False

    def zapisz(self, sciezka):
        try:
           plik_do_zapisu = open(sciezka, "w")
           dane_do_zapisu = ""
           pliki = self.zwroc()
           for plik in pliki:
               dane_do_zapisu += plik + "\n"
           plik_do_zapisu.write(dane_do_zapisu)
           plik_do_zapisu.close()
           return True
        except:
            print("Klasa Pobierz, metoda zapisz(). \n" +
            "Nie udało się zapisać listy plików.")
            return False
