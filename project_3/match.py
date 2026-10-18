from club import Club
from league import League
from team import Team
import math
import random


class Match:
    HOME_AVG = 1.4  # average goals for the home side (home advantage)
    AWAY_AVG = 1.2  # average goals for the away side

    def poisson(average_goals):
        limit = math.exp(-average_goals)
        goals = 0
        product = 1
        while product > limit:
            goals += 1
            product *= random.random()
        return goals - 1

    def __init__(self, home, away, league):
        if isinstance(home, Club):
            self.home = home
        if isinstance(away, Club):
            self.away = away
        if isinstance(league, League):
            self.league = league

    def play(self, home_team, away_team):
        if isinstance(home_team, Team) and (home_team.game_ready()):
            self.home_team = home_team
        if isinstance(away_team, Team) and (away_team.game_ready()):
            self.away_team = away_team

        # Finding how much better or worse home team is to away team
        # **3 to give a bigger edge to the better team
        strength = (home_team.rating() / away_team.rating()) ** 3

        self.home_score = self.poisson(self.HOME_AVG * strength)
        self.away_score = self.poisson(self.AWAY_AVG / strength)

        '''
        mu = 1.1
        sigma = 1.2
        self.home_score = max(0, math.floor(random.normalvariate(mu, sigma)))
        self.away_score = max(0, math.floor(random.normalvariate(mu, sigma)))
        '''
        if self.home_score > self.away_score:
            return f"{self.home} wins {self.home_score} - {self.away_score}"
        elif self.away_score > self.home_score:
            return f"{self.away} wins {self.home_score} - {self.away_score}"
        else:
            return f"The result was a tie {self.home_score} - {self.away_score}"
