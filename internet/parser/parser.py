import requests

class Parser:

    def otworz(self, link):
        self.rzadanie = requests.get(link)
        return self.rzadanie.text
