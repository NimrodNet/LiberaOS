class Tablica:

    def __init__(self):
        self.inicjuj()

    def inicjuj(self):
        try:
            self.tablica = []
            return True
        except:
            print("Klasa Tablica, metoda inicjuj(). Nie można zainicjować klasy.")
            return False

    def dodaj(self, element):
        try:
            self.zwroc().append(element)
            return self
        except:
            print("Klasa Tablica, metoda dodaj(). Nie można dodać elementu.")
            return False

    def zwroc(self):
        try:
            return self.tablica
        except:
            print("Klasa Tablica, metoda zwroc(). Nie można zwrócić tablicy.")
            return False

    def wyswietl(self):
        try:
            for element in self.zwroc():
                print(element)
            return True
        except:
            print("Klasa Tablica, metoda wyswiet(). Nie można wyświetlić elementów.")
            return False
