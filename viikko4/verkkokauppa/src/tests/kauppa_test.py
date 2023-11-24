import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):

    def setUp(self) -> None:
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock(wraps=Viitegeneraattori)

        # palautetaan aina arvo 42
        self.viitteet = [100, 200, 300, 400, 500]
        self.viitegeneraattori_mock.uusi.side_effect = self.viitteet

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            if tuote_id == 2:
                return 10
            if tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "juusto", 8)
            if tuote_id == 3:
                return Tuote(3, "leipä", 6)
            
        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        self.kauppa = Kauppa(varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)

    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
       
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista


    def test_ostetaan_yksi_tuote_ja_kutsutaan_pankin_tilisiirtoa_oikeilla_arvoilla(self):
    
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pekka", ANY, "12345", ANY, 5)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista


    def test_ostetaan_kaksi_eri_tuotetta_ja_kutsutaan_pankin_tilisiirtoa_oikeilla_arvoilla(self):
       
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pakka", "11111")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pakka", ANY, "11111", ANY, 13)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostetaan_kaksi_samaa_tuotetta_ja_kutsutaan_pankin_tilisiirtoa_oikeilla_arvoilla(self):
      
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pakka", "11111")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pakka", ANY, "11111", ANY, 16)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_ostetaan_ja_toinen_tuotteista_on_loppunut_kutsutaan_pankkia_oikeilla_arvoilla(self):
        
        # tehdään ostokset
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pakka", "11111")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        self.pankki_mock.tilisiirto.assert_called_with("pakka", ANY, "11111", ANY, 5)
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

    def test_uuden_asioinnin_aloittaminen_nollaa_edelliset_tiedot(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pp", "1111")

        self.pankki_mock.tilisiirto.assert_called_with("pp", ANY, "1111", ANY, 5)

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_ostokselle(self):

        for viite in self.viitteet:
            
            self.kauppa.aloita_asiointi()
            self.kauppa.lisaa_koriin(1)
            self.kauppa.tilimaksu("pp", "1111")
            
            self.pankki_mock.tilisiirto.assert_called_with("pp", viite, "1111", ANY, 5)

    def test_ostoskorista_poistettu_tuote_ei_nay_maksussa(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(1)
        self.kauppa.tilimaksu("pp", "1111")
            
        self.pankki_mock.tilisiirto.assert_called_with("pp", ANY, "1111", ANY, 8)
