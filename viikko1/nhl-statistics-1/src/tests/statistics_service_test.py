import unittest
from statistics_service import StatisticsService, SortBy
from player import Player

class PlayerReaderStub:
  def get_players(self):
    return[
      Player("Semenko", "EDM", 4, 12),
      Player("Lemieux", "PIT", 45, 54),
      Player("Kurri",   "EDM", 37, 53),
      Player("Yzerman", "DET", 42, 56),
      Player("Gretzky", "EDM", 35, 89)
    ]

class TestStatisticsService(unittest.TestCase):
  
  def setUp(self):
    self.stub = PlayerReaderStub()
    self.stats = StatisticsService(self.stub)
    
  def test_luokasta_luodaan_oikeanlainen_olio(self):
    self.assertIsInstance(self.stats, StatisticsService)

  def test_nimellä_haku_palauttaa_pelaajan(self):
    sp = self.stats.search("Kurri")
    self.assertEqual(sp.name, "Kurri")

  def test_jos_pelaajaa_ei_ole_palautetaan_none(self):
    sp = self.stats.search("Curry")
    self.assertEqual(sp, None)

  def test_tiimihaku_palauttaa_tiimin_pelaajat(self):
    all_edm_names = list(map(lambda player: player.name,
      filter(lambda player: player.team == "EDM", self.stub.get_players())
    ))
    for player in self.stats.team("EDM"):
      self.assertIn(player.name, all_edm_names)
  
  def test_palautetaan_kolme_parasta_pisteiden_perusteella(self):
    top_3 = list(
      map(lambda player: player.name,
      self.stats.top(2)
    ))
    self.assertEqual(top_3, ["Gretzky", "Lemieux", "Yzerman"])
  
  def test_palautetaan_kolme_parasta_maalien_perusteella(self):
    top_3 = list(
      map(lambda player: player.name,
      self.stats.top(2, SortBy.GOALS)
    ))
    self.assertEqual(top_3, ["Lemieux", "Yzerman", "Kurri"])
    
  def test_palautetaan_kolme_parasta_syottojen_perusteella(self):
    top_3 = list(
      map(lambda player: player.name,
      self.stats.top(2, SortBy.ASSISTS)
    ))
    self.assertEqual(top_3, ["Gretzky", "Yzerman", "Lemieux"])
    
    