class PlayerStats:
    def __init__(self, reader):
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):   
        return (p for p in sorted(self.players, key=lambda p: p.points, reverse=True)
            if p.nationality == nationality)
