class Sovelluslogiikka:
    def __init__(self, tulos=0):
        self.tulos = tulos
        self.historia = []

    def miinus(self, arvo):
        self.tulos = self.tulos - arvo

    def plus(self, arvo):
        self.tulos = self.tulos + arvo

    def nollaa(self):
        self.tulos = 0

    def aseta_arvo(self, arvo):
        self.tulos = arvo
        
    def historia_sisaan(self):
        self.historia.append(self.tulos)

    def historia_ulos(self):
        self.tulos = self.historia.pop()
