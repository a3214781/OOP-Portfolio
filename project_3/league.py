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

    def __str__(self):
        output = ""
        for team in self.clubs:
            output += team.name + ", "
        return output
