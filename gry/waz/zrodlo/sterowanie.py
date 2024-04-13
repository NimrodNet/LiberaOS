class Sterowanie:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        try:
            self.historia_kierunkow = []
            self.dodaj_kierunek(self.zwroc_kierunek_w_prawo())
            return True
        except:
            print("Klasa Sterowanie, metoda inicjuj(). \n" +
            "Nie można zainicjować modułu.")
            return False

    def zwroc_historie_kierunkow(self):
        try:
            return self.historia_kierunkow
        except:
            print("Klasa Sterowanie, metoda zwroc_historie_kierunkow(). \n" +
            "Nie można zwrócić historii kierunków.")
            return False

    def dodaj_kierunek(self, kierunek):
        try:
            self.zwroc_historie_kierunkow().append(kierunek)
            return True
        except:
            print("Klasa Sterowanie, metoda dodaj_kierunek(). \n" +
            "Nie można dodać kierunku.")
            return False

    def zwroc_rozmiar_historii_kierunkow(self):
        try:
            return len(self.zwroc_historie_kierunkow())
        except:
            print("Klasa Sterowanie, metoda zwroc_rozmiar_historii_kierunkow(). \n" +
            "Nie można zwrócić rozmiaru historii kierunków.")
            return False

    def zwroc_kierunek_w_prawo(cls):
        try:
            return [1, 0, 0, 0]
        except:
            print("Klasa Sterowanie, metoda zwroc_kierunek_w_prawo(). \n" +
            "Nie można zwrócić kierunku w prawo.")
            return False

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
            if do_przodu:
                kierunek = kierunki[0]
                self.dodaj_kierunek(kierunek)
            if do_tylu:
                kierunek = kierunki[1]
                self.dodaj_kierunek(kierunek)
            if w_prawo:
                kierunek = kierunki[2]
                self.dodaj_kierunek(kierunek)
            if w_lewo:
                kierunek = kierunki[3]
                self.dodaj_kierunek(kierunek)
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
