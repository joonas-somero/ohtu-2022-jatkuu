import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    # tehdään toteutus saldo-metodille
    def varasto_saldo(self, tuote_id):
        if tuote_id in range(1,3):
            return 10
        else:
            return 0


    # tehdään toteutus hae_tuote-metodille
    def varasto_hae_tuote(self, tuote_id):
        if tuote_id == 1:
            return Tuote(1, "maito", 5)
        if tuote_id == 2:
            return Tuote(2, "leipä", 3)


    # alustetaan testit
    def setUp(self):
        # asiakas nimeltä Pekka tilinumerollaan 12345
        self.asiakas = { "nimi": "pekka", "tilinumero": "12345" }

        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()


        # otetaan toteutukset käyttöön
        self.varasto_mock.saldo.side_effect = self.varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = self.varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

        # aloitetaan asiointi
        self.kauppa.aloita_asiointi()


    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        # tehdään ostokset
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(*self.asiakas.values())
        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista


    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(*self.asiakas.values())

        self.pankki_mock.tilisiirto.assert_called_with(self.asiakas["nimi"], ANY, self.asiakas["tilinumero"], ANY, 5)


    def test_kahdella_eri_tuotteella_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu(*self.asiakas.values())

        self.pankki_mock.tilisiirto.assert_called_with(self.asiakas["nimi"], ANY, self.asiakas["tilinumero"], ANY, 8)


    def test_kahdella_samalla_tuotteella_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(*self.asiakas.values())

        self.pankki_mock.tilisiirto.assert_called_with(self.asiakas["nimi"], ANY, self.asiakas["tilinumero"], ANY, 10)


    def test_loppuneella_tuotteella_pankin_metodia_tilisiirto_kutsutaan_oikeilla_arvoilla(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu(*self.asiakas.values())

        self.pankki_mock.tilisiirto.assert_called_with(self.asiakas["nimi"], ANY, self.asiakas["tilinumero"], ANY, 5)


    def test_kaupan_metodi_aloita_asiointi_nollaa_edellisen_ostoksen_tiedot(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu(*self.asiakas.values())

        self.pankki_mock.tilisiirto.assert_called_with(*([ANY]*4), 8)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(*self.asiakas.values())

        self.pankki_mock.tilisiirto.assert_called_with(*([ANY]*4), 5)


    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu(*self.asiakas.values())

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu(*self.asiakas.values())

        self.assertEqual(self.viitegeneraattori_mock.uusi.call_count, 2)


    def test_tuotteen_poistaminen_ostoskorista_kutsuu_varaston_metodia_palauta_varastoon(self):
        self.kauppa.lisaa_koriin(1)
        self.kauppa.poista_korista(1)

        self.varasto_mock.palauta_varastoon.assert_called_with(self.varasto_hae_tuote(1))
