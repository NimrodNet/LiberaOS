class Tekst:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        try:
            self.tekst = []
            return True
        except:
            print("Klasa Tekst, metoda inicjuj(). \n" +
            "Problem z inicjacją.")
            return False

    def dodaj(self, tekst):
        try:
            self.tekst.extend(tekst)
            return True
        except:
            print("Klasa Tekst, metoda ustaw(). \n" +
            "Nie można ustawić tekstu.")
            return False

    def wstaw(self, slowa, indeks):
        try:
            self.zwroc().insert(indeks, slowa)
            return True
        except:
            print("Klasa Tekst, metoda ustaw(). \n" +
            "Nie można ustawić tekstu.")
            return False

    def usun(self, od, do):
        try:
            del self.zwroc()[od:do]
            return self.zwroc()
        except:
            print("Klasa Tekst, metoda usun(). \n" +
            "Nie można usunąć elementu.")
            return False

    def wyczysc(self):
        try:
            self.inicjuj()
            return self.zwroc()
        except:
            print("Klasa Tekst, metoda wyczysc(). \n" +
            "Nie można wyczyścić tekstu.")
            return False

    def zwroc(self):
        try:
            return self.tekst
        except:
            print("Klasa Tekst, metoda zwroc(). \n" + 
            "Nie można zwrócić tekstu.")
            return False

    def wyswietl(self):
        try:
            tekst = self.zwroc()
            print(tekst)
            return True
        except:
            print("Klasa Tekst, metoda wyswietl(). \n" + 
            "Nie można wyświetlić tekstu.")
            return False
