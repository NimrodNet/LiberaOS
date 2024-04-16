class Miejsce:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        try:
            wartosc = [1]
            x = [0]
            y = [0]
            kierunek = [1, 0, 0, 0]
            self.miejsce = [wartosc, x, y, kierunek]
            return True
        except:
            print("Klasa Miejsce, metoda inicjuj()." + 
            "Nie można zainicjować miejsca.")
            return False

    def zwroc(self):
        try:
            return self.miejsce
        except:
            print("Klasa Miejsce, metoda zwroc()." + 
            "Nie można zwrócić miejsca.")
            return False

    def ustaw(self, numer, wartosc):
        try:
            self.zwroc()[numer][0] = wartosc
            return True
        except:
            print("Klasa Miejsce, metoda ustaw()." + 
            "Nie można ustawić wartości.")
