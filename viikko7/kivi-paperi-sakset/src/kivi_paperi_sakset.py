from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly
from tuomari import Tuomari


class KiviPaperiSakset:
    @staticmethod
    def aloita_kaksinpeli():
        return KPSPelaajaVsPelaaja(Tuomari())
    
    @staticmethod
    def aloita_yksinpeli():
        return KPSTekoaly(Tuomari())

    @staticmethod
    def aloita_haastava_yksinpeli():
        return KPSParempiTekoaly(Tuomari())
