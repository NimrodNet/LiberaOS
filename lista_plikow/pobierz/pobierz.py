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
                print(etykieta)
            return etykiety
        except:
            print("Klasa Pobierz, metoda zwroc_etykiete_pliku(). \n" + 
            "Nie można zwrócić etykiety pliku.")
            return False

    def zwroc_nazwy_plikow(self):
        try:
            nazwy = []
            etykiety = self.zwroc_etykiety_plikow(sciezki)
            for etykieta in etykiety:
                nazwy.append(etykieta[0])
            return nazwy
        except:
            print("Klasa Pobierz, metoda zwroc_nazwy_plikow(). \n" + 
            "Nie można zwrócić nazw plików.")
            return False

    def zwroc_element(self, indeks):
        try:
            self.ustaw(self.lista_plikow[indeks])
            return self.zwroc()
        except:
            print("Klasa Pobierz, metoda zwroc_element(). \n" + 
            "Nie można zwrócić elementu listy.")
            return False

    def zwroc_sciezke(self, indeks, numer_sciezki):
        try:
            self.ustaw([self.lista_plikow[indeks][numer_sciezki]])
            return self.zwroc()
        except:
            print("Klasa Pobierz, metoda zwroc_sciezki(). \n" + 
            "Nie można zwrócić ścieżki.")
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
               lista_plikow.append(pliki)
           self.ustaw(lista_plikow)
           return self.zwroc()
        except:
            print("Klasa Pobierz, metoda pobierz(). \n" +
            "Nie udało się pobrać listy plików.")
            return False

    def sortuj(self):
        try:
           pliki = self.zwroc()
           lista_plikow = []
           for sciezki in pliki:
               sciezki.sort()
               lista_plikow.append(sciezki)
           self.ustaw(lista_plikow)
           return self.zwroc()
        except:
            print("Klasa Pobierz, metoda sortuj(). \n" +
            "Nie udało się posortować listy plików.")
            return False

    def sortuj_odwrotnie(self):
        try:
           pliki = self.zwroc()
           lista_plikow = []
           for sciezki in pliki:
               sciezki.sort(reverse = True)
               lista_plikow.append(sciezki)
           self.ustaw(lista_plikow)
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
