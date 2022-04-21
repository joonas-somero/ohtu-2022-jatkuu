from statistics import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, Not, HasFewerThan, Or

def main():
    url = "https://nhlstatisticsforohtu.herokuapp.com/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    matcher = And(
        HasAtLeast(5, "goals"),
        HasAtLeast(5, "assists"),
        PlaysIn("PHI")
    )

    for player in stats.matches(matcher):
        print(player)

    matcher1 = And(
        Not(HasAtLeast(1, "goals")),
        PlaysIn("NYR")
    )

    matcher2 = And(
        HasFewerThan(1, "goals"),
        PlaysIn("NYR")
    )

    for player_1, player_2 in zip(stats.matches(matcher1), stats.matches(matcher2)):
        print(f"{player_1}\t{player_2}")
    
    matcher3 = Or(
        HasAtLeast(30, "goals"),
        HasAtLeast(50, "assists")
    )

    for player in stats.matches(matcher3):
        print(player)

    matcher4 = And(
        HasAtLeast(40, "points"),
        Or(
            PlaysIn("NYR"),
            PlaysIn("NYI"),
            PlaysIn("BOS")
        )
    )

    for player in stats.matches(matcher4):
        print(player)

if __name__ == "__main__":
    main()
