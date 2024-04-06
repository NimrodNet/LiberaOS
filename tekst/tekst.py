class Tekst:

    def inicjuj(self, tekst):
        try:
            self.tekst = []
            self.tekst.append(tekst)
            return True
        except:
            print("Klasa Tekst, metoda ustaw(). \n" +
            "Nie można ustawić tekstu.")
            return False

    def dodaj(self, tekst):
        try:
            self.tekst = []
            self.tekst.append(tekst)
            return True
        except:
            print("Klasa Tekst, metoda ustaw(). \n" +
            "Nie można ustawić tekstu.")
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
