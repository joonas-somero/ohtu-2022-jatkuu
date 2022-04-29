from kivi_paperi_sakset import KiviPaperiSakset
from io_palvelu import io as oletus_io


class Valikko:
    def __init__(self, io=oletus_io):
        self._io = io
        self._valinnat = {
            "a": KiviPaperiSakset.aloita_kaksinpeli,
            "b": KiviPaperiSakset.aloita_yksinpeli,
            "c": KiviPaperiSakset.aloita_haastava_yksinpeli
        }
        self._valikkoteksti = (
                f"Valitse pelataanko"
                f"\n (a) Ihmistä vastaan"
                f"\n (b) Tekoälyä vastaan"
                f"\n (c) Parannettua tekoälyä vastaan"
                f"\nMuilla valinnoilla lopetetaan"
                f"\n"
        )
    
    def _valitse(self, valinta):
        if valinta in self._valinnat:
            self._valinnat[valinta]().pelaa()
        else:
            exit(1)

    def avaa(self):
        while True:
            vastaus = self._io.lue(self._valikkoteksti)
            self._valitse(vastaus)
