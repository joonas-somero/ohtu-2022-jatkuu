import statistics
import unittest
from statistics import Statistics, sort_by_points
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_returns_correct_player(self):
        player = self.statistics.search("Kurri")
        self.assertEqual(player.name, "Kurri")

    def test_search_returns_none_when_player_not_found(self):
        self.assertIsNone(self.statistics.search("Selänne"))

    def test_team_returns_all_players_on_team(self):
        team = self.statistics.team("EDM")
        (self.assertIn(team, name) for name in ["Semenko", "Kurri", "Gretzky"])

    def test_top_scorers_are_sorted_by_score(self):
        scorers = self.statistics.top_scorers(4)
        self.assertEqual(
            [player.points for player in scorers],
            [35+89, 45+54, 42+56, 37+53, 4+12]
        )
