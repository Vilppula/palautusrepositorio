import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.url = url
        

    def read(self):
        response = requests.get(self.url, timeout=10).json()
        players = []

        for player_dict in response:
            player = Player(player_dict)
            players.append(player)

        return players
