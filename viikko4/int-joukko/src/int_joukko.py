KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):
        if self.__tarkista_parametrit(kapasiteetti, kasvatuskoko):
            self.__kapasiteetti = kapasiteetti
            self.__kasvatuskoko = kasvatuskoko
    
        self.__joukko = [None] * self.__kapasiteetti
        self.__alkioiden_lkm = 0

    def __tarkista_parametrit(self, kapasiteetti, kasvatuskoko):
        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti")

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")

        return True

    def __kasvata_kapasiteettia(self):
        self.__kapasiteetti = self.__kapasiteetti + self.__kasvatuskoko
        uusi_joukko = [None] * self.__kapasiteetti

        for i in range(0, self.__alkioiden_lkm):
            uusi_joukko[i] = self.__joukko[i]
        
        self.__joukko = uusi_joukko

    def __etsi(self, n):
        for i in range(0, self.__alkioiden_lkm):
            if self.__joukko[i] == n:
                return i
        return None

    def kuuluu(self, n):
        return True if self.__etsi(n) != None else False

    def lisaa(self, n):
        if self.kuuluu(n):
            return False

        if self.__alkioiden_lkm == self.__kapasiteetti:
            self.__kasvata_kapasiteettia()
        
        self.__joukko[self.__alkioiden_lkm] = n
        self.__alkioiden_lkm += 1

        return True

    def poista(self, n):
        poistettavan_indeksi = self.__etsi(n)
        if poistettavan_indeksi != None:
            for i in range(poistettavan_indeksi, self.__alkioiden_lkm-1):
                self.__joukko[i] = self.__joukko[i+1]
            
            self.__alkioiden_lkm -= 1
            return True     
        return False

    def mahtavuus(self):
        return self.__alkioiden_lkm

    def to_int_list(self):
        int_list = [None] * self.__alkioiden_lkm

        for i in range(0, self.__alkioiden_lkm):
            int_list[i] = self.__joukko[i]

        return int_list

    @staticmethod
    def yhdiste(a, b):
        joukkojen_yhdiste = IntJoukko()

        a_int_listana = a.to_int_list()
        for i in range(0, a.mahtavuus()):
            joukkojen_yhdiste.lisaa(a_int_listana[i])

        b_int_listana = b.to_int_list()
        for i in range(0, b.mahtavuus()):
            joukkojen_yhdiste.lisaa(b_int_listana[i])

        return joukkojen_yhdiste

    @staticmethod
    def leikkaus(a, b):
        joukkojen_leikkaus = IntJoukko()

        yhdiste = IntJoukko.yhdiste(a, b)
        yhdiste_int_listana = yhdiste.to_int_list()
        for i in range(0, yhdiste.mahtavuus()):
            alkio = yhdiste_int_listana[i]
            if a.kuuluu(alkio) and b.kuuluu(alkio):
                joukkojen_leikkaus.lisaa(alkio)

        return joukkojen_leikkaus

    @staticmethod
    def erotus(a, b):
        joukkojen_erotus = IntJoukko()

        a_int_listana = a.to_int_list()
        for i in range(0, a.mahtavuus()):
            alkio = a_int_listana[i]
            if not b.kuuluu(alkio):
                joukkojen_erotus.lisaa(alkio)

        return joukkojen_erotus

    def __str__(self):
        merkkijono = "{"
        for i in range(0, self.__alkioiden_lkm):
            merkki = str(self.__joukko[i])
            merkkijono += merkki + ", " if i < self.__alkioiden_lkm-1 else merkki
        return merkkijono + "}"