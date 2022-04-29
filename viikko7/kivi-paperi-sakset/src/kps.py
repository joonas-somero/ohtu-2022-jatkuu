from io_palvelu import io as oletus_io


class KPS:
    def __init__(self, tuomari, io=oletus_io):
        self._io = io
        self._tuomari = tuomari
        self._tulosteet = {
            "aloitus": "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s",
            "pelaaja1": "Ensimmäisen pelaajan siirto: ",
            "kiitokset": "Kiitos!"
        }

    def pelaa(self):
        self._io.tulosta(
            self._tulosteet["aloitus"]
        )
        
        self._pelikierros()

        self._io.tulosta(
            self._tulosteet["kiitokset"],
            self._tuomari
        )

    def _pelikierros(self):
        while True:
            ekan_siirto = self._ensimmaisen_siirto()
            if not self._onko_ok_siirto(ekan_siirto):
                break

            tokan_siirto = self._toisen_siirto(ekan_siirto)
            if not self._onko_ok_siirto(tokan_siirto):
                break

            self._tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            self._io.tulosta(
                self._tuomari
            )

    def _ensimmaisen_siirto(self):
        return self._io.lue(
          self._tulosteet["pelaaja1"]
        )

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self, ensimmaisen_siirto):
        # metodin oletustoteutus
        return "k"

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
