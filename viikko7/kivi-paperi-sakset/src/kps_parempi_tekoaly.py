from kps import KPS
from tekoaly_parannettu import TekoalyParannettu

OLETUS_MUISTIN_KOKO = 10


class KPSParempiTekoaly(KPS):
    def __init__(self, tuomari, muistin_koko=OLETUS_MUISTIN_KOKO):
        super().__init__(tuomari)
        self.tekoaly = TekoalyParannettu(muistin_koko)

    def _toisen_siirto(self, ensimmäinen_siirto):
        self.tekoaly.aseta_siirto(ensimmäinen_siirto)
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto
