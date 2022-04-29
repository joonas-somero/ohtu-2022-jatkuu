from xml.etree.ElementTree import PI
from pisteet import Pisteet


class Tuomari:
    def __init__(self):
        self._pisteet = Pisteet()
        self._logiikka = {
            "k": {"k": self._pisteet.tasapeli, "s": self._pisteet.eka_voittaa, "p": self._pisteet.toka_voittaa},
            "s": {"k": self._pisteet.toka_voittaa, "s": self._pisteet.tasapeli, "p": self._pisteet.eka_voittaa},
            "p": {"k": self._pisteet.eka_voittaa, "s": self._pisteet.toka_voittaa, "p": self._pisteet.tasapeli},
        }

    def kirjaa_siirto(self, ekan_siirto, tokan_siirto):
        self._logiikka[ekan_siirto][tokan_siirto]()

    def __str__(self):
        return f"Pelitilanne: {self._pisteet.ekan_pisteet} - {self._pisteet.tokan_pisteet}\nTasapelit: {self._pisteet.tasapelit}"
