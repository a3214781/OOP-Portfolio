from country import Country
from club import Club
from team_not_ready_error import TeamNotReadyError


class League:
    """A League holds the clubs that compete against each other. It is
    responsible for running a season between its clubs and building the
    results table. It does not play individual matches itself, because that
    job belongs to the Match class."""

    def __init__(self, name, country, division):
        # The name must be a string, otherwise a default is used so the
        # league can still be created.
        if isinstance(name, str):
            self.name = name
        else:
            self.name = "No Name"
            print("League name is invalid.")

        # The country must be a Country object so the league is always
        # linked to a real country or to nothing at all.
        if isinstance(country, Country):
            self.country = country
        else:
            self.country = None
            print("League country is invalid.")

        # Division must be a positive whole number. Bool is rejected because
        # Python treats True as the number 1.
        if (
            isinstance(division, int)
            and not isinstance(division, bool)
            and division > 0
        ):
            self.division = division
        else:
            self.division = 1
            print("Division is invalid.")

        # A league starts with no clubs, which are added with add_club().
        self.clubs = []

    def add_club(self, club):
        # Only Club objects are accepted so the season loop can rely on
        # every item in the list having a team.
        if isinstance(club, Club):
            self.clubs.append(club)
            # The club is told which league it is in so both sides of the
            # relationship stay in sync.
            club.league = self

    def remove_club(self, club):
        # Removing a club that is not in the league does nothing.
        if club in self.clubs:
            self.clubs.remove(club)
            # The club no longer belongs to a league, so the link is cleared.
            club.league = None

    def play_season(self):
        """Play every club against every other club at home and away, and
        return the results table."""
        # Imported here instead of at the top to avoid a loop import
        # where match needs team adn team needs match.
        from match import Match

        table = self.new_table()

        # Every club hosts every other club once, so each pair of clubs
        # plays twice in a season (one home game and one away game).
        for home in self.clubs:
            for away in self.clubs:
                # A club cannot play against itself.
                if home == away:
                    continue

                # The Match class plays the game and works out the score, and
                # the league only records the result.
                match = Match(home, away, self)
                # A team that is not ready cannot play, so that fixture is
                # skipped with a message and the rest of the season carries on.
                try:
                    match.play(home.team, away.team)
                except TeamNotReadyError as error:
                    print(f"Match skipped: {error}")
                    continue
                self.record_result(table, home, away, match)

        return table

    def new_table(self):
        """Build the starting scoreboard for the season."""
        # Each club gets its own row, stored in a dictionary so a club's row
        # can be found quickly while recording results.
        table = {}
        for club in self.clubs:
            table[club] = {
                "played": 0,
                "won": 0,
                "drawn": 0,
                "lost": 0,
                "gf": 0,
                "ga": 0,
                "points": 0,
            }
        return table

    def record_result(self, table, home, away, match):
        """Update both clubs' rows in the table after one match."""
        home_row = table[home]
        away_row = table[away]

        # Both clubs have played one more game, no matter the result.
        home_row["played"] += 1
        away_row["played"] += 1

        # One club's goals scored are the other club's goals conceded.
        home_row["gf"] += match.home_score
        home_row["ga"] += match.away_score
        away_row["gf"] += match.away_score
        away_row["ga"] += match.home_score

        # A win gives 3 points, a draw gives 1 point each, and a loss gives
        # no points.
        if match.home_score > match.away_score:
            home_row["won"] += 1
            home_row["points"] += 3
            away_row["lost"] += 1
        elif match.home_score < match.away_score:
            away_row["won"] += 1
            away_row["points"] += 3
            home_row["lost"] += 1
        else:
            home_row["drawn"] += 1
            away_row["drawn"] += 1
            home_row["points"] += 1
            away_row["points"] += 1

    def print_table(self, table):
        """Print the table with the best club at the top."""
        # Each club gets a list: [points, goal difference, goals scored,
        # name, row]. Python sorts lists one item at a time, so putting the
        # points first means clubs are ordered by points, then by goal
        # difference if points are equal, then by goals scored.
        rows = []
        for club in table:
            row = table[club]
            goal_difference = row["gf"] - row["ga"]
            rows.append(
                [row["points"], goal_difference, row["gf"], str(club), row]
            )

        # reverse=True puts the highest numbers at the top of the table.
        rows.sort(reverse=True)

        print("-----------------------------------------------")
        print("| #  | Team              | P | W | D | L | Pts |")
        print("-----------------------------------------------")

        # The place is a counter because the sorted list does not store it.
        place = 1
        for item in rows:
            name = item[3]
            row = item[4]
            print(
                f"| {place}  | {name:<17} | {row['played']} | "
                f"{row['won']} | {row['drawn']} | {row['lost']} | "
                f"{row['points']}   |"
            )
            place += 1

        print("-----------------------------------------------")

    def __str__(self):
        # Lists the club names so printing a league shows who is in it.
        output = ""
        for team in self.clubs:
            output += team.name + ", "
        return output
