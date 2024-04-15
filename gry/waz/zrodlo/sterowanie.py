from zrodlo.tablice.tablica import *

class Sterowanie:

    def __init__(self):
        self.kierunki = Tablica()

    def uruchom_sterowanie(self, gra, kierunek):
        try:
            nacisnieto = gra.key.get_pressed()
            klawisze = self.zwroc_klawisze(gra)
            klawisz_w = klawisze[0]
            klawisz_s = klawisze[1]
            klawisz_a = klawisze[2]
            klawisz_d = klawisze[3]
            strzalka_do_gory = klawisze[4]
            strzalka_w_dol = klawisze[5]
            strzalka_w_lewo = klawisze[6]
            strzalka_w_prawo = klawisze[7]
            do_przodu = nacisnieto[klawisz_w] or nacisnieto[strzalka_do_gory]
            do_tylu = nacisnieto[klawisz_s] or nacisnieto[strzalka_w_dol]
            w_prawo = nacisnieto[klawisz_d] or nacisnieto[strzalka_w_prawo]
            w_lewo = nacisnieto[klawisz_a] or nacisnieto[strzalka_w_lewo]
            kierunek_do_gory = [0, 1, 0, 0]
            kierunek_w_dol = [0, -1, 0, 0]
            kierunek_w_prawo = [1, 0, 0, 0]
            kierunek_w_lewo = [-1, 0, 0, 0]
            kierunki = [kierunek_do_gory, kierunek_w_dol, kierunek_w_prawo,
                        kierunek_w_lewo]
            ostatni_kierunek = self.kierunki.ostatni()
            if do_przodu:
                if ostatni_kierunek != kierunek_w_dol:
                    kierunek = kierunek_do_gory
            if do_tylu:
                if ostatni_kierunek != kierunek_do_gory:
                    kierunek = kierunek_w_dol
            if w_prawo:
                if ostatni_kierunek != kierunek_w_lewo:
                    kierunek = kierunek_w_prawo
            if w_lewo:
                if ostatni_kierunek != kierunek_w_prawo:
                    kierunek = kierunek_w_lewo
            self.kierunki.dodaj(kierunek)
            return kierunek
        except:
            print("Klasa Sterowanie, metoda uruchom_sterowanie(). \n" +
            "Nie można uruchomić sterowania.")
            return False

    def zwroc_klawisze(self, gra):
        try:
            klawisze = []
            klawisze.append(gra.K_w)
            klawisze.append(gra.K_s)
            klawisze.append(gra.K_a)
            klawisze.append(gra.K_d)
            klawisze.append(gra.K_UP)
            klawisze.append(gra.K_DOWN)
            klawisze.append(gra.K_LEFT)
            klawisze.append(gra.K_RIGHT)
            return klawisze
        except:
            print("Klasa Sterowanie, metoda zwroc_klawisze(). \n" +
            "Nie można zwrócić klawiszy.")
            return False
