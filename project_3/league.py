from country import Country
from club import Club


class League:
    def __init__(self, name, country, division):
        if isinstance(name, str):
            self.name = name
        if isinstance(country, Country):
            self.country = country
        if isinstance(division, int) and not isinstance(division, bool):
            self.division = division

        self.clubs = []

    def add_club(self, club):
        if isinstance(club, Club):
            self.clubs.append(club)
            club.league = self

    def remove_club(self, club):
        if club in self.clubs:
            self.clubs.remove(club)
            club.league = None

    def play_season(self):
        # need to import here to not create a loop
        from match import Match
        # making a scoreboard for every club, everything starts at 0
        table = {}
        for club in self.clubs:
            table[club] = {"played": 0, "won": 0, "drawn": 0, "lost": 0,
                           "gf": 0, "ga": 0, "points": 0}

        # every club hosts every other club
        for home in self.clubs:          # pick a home club
            for away in self.clubs:      # pick an away club
                if home == away:         # a club can not play itself
                    continue

                # play the match between their teams
                match = Match(home, away, self)
                match.play(home.team, away.team)

                h = table[home]          # home club's row
                a = table[away]          # away club's row

                # both clubs played one more game
                h["played"] += 1
                a["played"] += 1

                # goals scored and conceded
                h["gf"] += match.home_score
                h["ga"] += match.away_score
                a["gf"] += match.away_score
                a["ga"] += match.home_score

                if match.home_score > match.away_score:      # home won
                    h["won"] += 1
                    h["points"] += 3
                    a["lost"] += 1
                elif match.home_score < match.away_score:    # away won
                    a["won"] += 1
                    a["points"] += 3
                    h["lost"] += 1
                else:                                        # draw
                    h["drawn"] += 1
                    a["drawn"] += 1
                    h["points"] += 1
                    a["points"] += 1

        return table

    def print_table(self, table):
        # make a plain list of rows, one per club
        rows = []
        for club in table:
            r = table[club]
            gd = r["gf"] - r["ga"]
            rows.append([r["points"], gd, r["gf"], str(club), r])

        # sort: highest points first (then goal difference, then goals scored)
        rows.sort(reverse=True)

        print("-----------------------------------------------")
        print("| #  | Team              | P | W | D | L | Pts |")
        print("-----------------------------------------------")

        place = 1
        for row in rows:
            name = row[3]
            r = row[4]
            print(
                f"| {place}  | {name:<17} | {r['played']} | {r['won']} | {r['drawn']} | {r['lost']} | {r['points']}   |")
            place += 1

        print("-----------------------------------------------")

    def __str__(self):
        output = ""
        for team in self.clubs:
            output += team.name + ", "
        return output
