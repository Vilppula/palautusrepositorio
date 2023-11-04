from player_reader import PlayerReader
from enum import Enum

class SortBy(Enum):
    POINTS = 1
    GOALS = 2
    ASSISTS = 3

def sort_by(by):
    if by == SortBy.POINTS:
        return lambda player: player.points
    if by == SortBy.GOALS:
        return lambda player: player.goals
    else:
        return lambda player: player.assists


class StatisticsService:
    def __init__(self, playerReader):
        self.reader = playerReader

        self._players = self.reader.get_players()

    def search(self, name):
        for player in self._players:
            if name in player.name:
                return player

        return None

    def team(self, team_name):
        players_of_team = filter(
            lambda player: player.team == team_name,
            self._players
        )

        return list(players_of_team)

    def top(self, how_many, by=SortBy.POINTS):
        sorted_players = sorted(
            self._players,
            reverse=True,
            key=sort_by(by)
        )

        result = []
        i = 0
        while i <= how_many:
            result.append(sorted_players[i])
            i += 1

        return result
