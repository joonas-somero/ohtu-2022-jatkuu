class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_points = 0
        self.player2_points = 0

    @property
    def has_a_player_with_atleast_four_points(self):
        return self.player1_points >= 4 or self.player2_points >= 4

    @property
    def has_a_player_with_atleast_two_more_points_than_opponent(self):
        return abs(self.player1_points - self.player2_points) >= 2

    @property
    def has_atleast_three_points_won_on_each_side(self):
        return self.player1_points > 3 and self.player2_points > 3

    @property
    def has_winner(self):
        return all((
            self.has_a_player_with_atleast_four_points,
            self.has_a_player_with_atleast_two_more_points_than_opponent
            ))

    @property
    def has_advantaged_player(self):
        return self.player1_points != self.player2_points and max(self.player1_points, self.player2_points) > 3

    @property
    def is_tied(self):
        return self.player1_points == self.player2_points

    def get_leader(self):
        players = {"player1": self.player1_points, "player2": self.player2_points}
        return max(players, key=lambda player: players[player])

    def get_call(self, points):
        calls = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        return calls[points]

    def get_winning_call(self):
        return f"Win for {self.get_leader()}"

    def get_advantaged_call(self):
        return f"Advantage {self.get_leader()}"

    def get_tied_call(self):
        if self.has_atleast_three_points_won_on_each_side:
            return "Deuce"
        return f"{self.get_call(self.player1_points)}-All"

    def won_point(self, player_name):
        if player_name == "player1":
            self.player1_points = self.player1_points + 1
        else:
            self.player2_points = self.player2_points + 1

    def get_score(self):
        if self.has_winner:
            return self.get_winning_call()
        elif self.has_advantaged_player:
            return self.get_advantaged_call()
        elif self.is_tied:
            return self.get_tied_call()
        else:
            return f"{self.get_call(self.player1_points)}-{self.get_call(self.player2_points)}"
