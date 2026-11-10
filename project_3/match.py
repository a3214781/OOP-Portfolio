import math
import random

from club import Club
from league import League
from team import Team
from team_not_ready_error import TeamNotReadyError


class Match:
    """A Match plays one game between a home club and away club and works
    out the score from the strength of their teams. It does not keep a table
    of results, because that responsibility belongs to the League class."""

    # The home side scores a little more on average than the away side, which
    # models home advantage.
    HOME_AVG = 1.4  # average goals for the home side (home advantage)
    AWAY_AVG = 1.2  # average goals for the away side

    @staticmethod
    def poisson(average_goals):
        """Return a random number of goals that follows a Poisson
        distribution with the given average."""
        # A Poisson distribution is used because goals in football are rare,
        # random events, so most games have 0 to 3 goals and a few have more.
        # This is a static method because it only uses its input and does not
        # need any data from a Match object.

        # Random numbers between 0 and 1 are multiplied together until the
        # result drops below this limit. The number of multiplications this
        # takes follows a Poisson distribution, so it becomes the goal count.
        limit = math.exp(-average_goals)
        goals = 0
        product = 1
        while product > limit:
            goals += 1
            product *= random.random()

        # The loop always runs one time too many, so one is subtracted.
        return goals - 1

    def __init__(self, home, away, league):
        # The home and away clubs must be Club objects, otherwise they are set
        # to None so the match can still be created.
        if isinstance(home, Club):
            self.home = home
        else:
            self.home = None
            print("Home club is invalid.")

        if isinstance(away, Club):
            self.away = away
        else:
            self.away = None
            print("Away club is invalid.")

        # The league the match belongs to must be a League object.
        if isinstance(league, League):
            self.league = league
        else:
            self.league = None
            print("League is invalid.")

    @staticmethod
    def check_ready(team):
        """Raise TeamNotReadyError unless the team is able to play."""
        # This is a static method because it only looks at the team it is
        # given and does not need any data from a Match object.
        if not isinstance(team, Team):
            raise TeamNotReadyError(
                "A match needs a Team, but something else was given."
            )
        if not team.game_ready():
            raise TeamNotReadyError(
                f"{team.club} is not ready to play: it has "
                f"{len(team.players)} players and {len(team.managers)} "
                f"manager(s)."
            )

    def play(self, home_team, away_team):
        """Play the match, store the score, and return a sentence describing
        the result. Raises TeamNotReadyError if either team cannot play."""
        # Both teams are checked before anything else happens, so a match that
        # cannot be played never produces a score.
        Match.check_ready(home_team)
        Match.check_ready(away_team)

        # Finding how much better or worse the home team is than the away
        # team. A number above 1 means the home team is stronger. The ratio
        # is cubed to give a bigger edge to the better team, because a plain
        # ratio makes the results too close together.
        strength = (home_team.rating() / away_team.rating()) ** 3

        # A stronger home team raises its own average goals and lowers the
        # away team's average, so the same strength value is used both ways.
        self.home_score = self.poisson(self.HOME_AVG * strength)
        self.away_score = self.poisson(self.AWAY_AVG / strength)

        # The result is returned as text so the caller can print it, and the
        # scores stay stored on the match so the league can read them.
        if self.home_score > self.away_score:
            return f"{self.home} wins {self.home_score} - {self.away_score}"
        elif self.away_score > self.home_score:
            return f"{self.away} wins {self.home_score} - {self.away_score}"
        else:
            return (
                f"The result was a tie {self.home_score} - {self.away_score}"
            )
