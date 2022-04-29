class Pisteet:
    def __init__(self):
        self.__ekan_pisteet = 0
        self.__tokan_pisteet = 0
        self.__tasapelit = 0

    @property
    def ekan_pisteet(self):
        return self.__ekan_pisteet

    @property
    def tokan_pisteet(self):
        return self.__tokan_pisteet

    @property
    def tasapelit(self):
        return self.__tasapelit

    def eka_voittaa(self):
        self.__ekan_pisteet += 1

    def toka_voittaa(self):
        self.__tokan_pisteet += 1

    def tasapeli(self):
        self.__tasapelit += 1

pisteet = Pisteet()