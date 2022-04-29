# "Muistava tekoäly"
class TekoalyParannettu:
    def __init__(self, muistin_koko):
        self._muisti = []
        self._muistin_koko = muistin_koko

    def aseta_siirto(self, siirto):
        # jos muisti täyttyy, unohdetaan vanhin alkio
        if len(self._muisti) == self._muistin_koko:
            del self._muisti[0]
        self._muisti.append(siirto)

    def _yleisin_vastustajan_siirto(self):
        return max(set(self._muisti), key=self._muisti.count)

    def anna_siirto(self):
        # parannettu teköäly pelaa vastustajan yleisimmän siirron voittavan siirron
        voittavat_siirrot = { "k": "p", "s": "k", "p": "s"}
        vastustajan_siirto = self._yleisin_vastustajan_siirto()
        
        return voittavat_siirrot[vastustajan_siirto]
