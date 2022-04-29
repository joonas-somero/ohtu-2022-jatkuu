from kps import KPS


class KPSPelaajaVsPelaaja(KPS):
    def __init__(self, tuomari):
        super().__init__(tuomari)
        self._tulosteet["pelaaja2"] = "Toisen pelaajan siirto: "

    def _toisen_siirto(self, _):
        return self._io.lue(
            self._tulosteet["pelaaja2"]
        )
