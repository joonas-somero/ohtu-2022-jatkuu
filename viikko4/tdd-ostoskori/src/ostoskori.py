from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self._kori = {}

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2
        return sum(ostos.lukumaara() for ostos in self._kori.values())

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        return sum(ostos.hinta() for ostos in self._kori.values())

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen
        nimi = lisattava.nimi()
        if nimi in self._kori:
            self._kori[nimi].muuta_lukumaaraa(1)
        else:
            self._kori[nimi] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        nimi = poistettava.nimi()
        self._kori[nimi].muuta_lukumaaraa(-1)
        if self._kori[nimi].lukumaara() == 0:
            del self._kori[nimi]

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self._kori = {}

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        return list(self._kori.values())
