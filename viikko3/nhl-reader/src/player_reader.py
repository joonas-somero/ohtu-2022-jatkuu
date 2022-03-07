from urllib import request


import requests
from player import Player


class PlayerReader:
    def __init__(self, url):
        self._url = url
        
    def get_players(self):
        response = requests.get(self._url).json()
        players = (Player(
            p['name'],
            p['nationality'],
            p['assists'],
            p['goals'],
            p['penalties'],
            p['team'],
            p['games'])
            for p in response
        )
        return players
