from kps import KPS
from tekoaly import Tekoaly


class KPSTekoaly(KPS):
    def __init__(self, tuomari):
        super().__init__(tuomari)
        self._tulosteet["pelaaja2"] = "Tietokone valitsi: {siirto}"
        self.tekoaly = Tekoaly()
        

    def _toisen_siirto(self, _):
        tokan_siirto = self.tekoaly.anna_siirto()
        self._io.tulosta(
            self._tulosteet["pelaaja2"].format(siirto = tokan_siirto)
        )

        return tokan_siirto
