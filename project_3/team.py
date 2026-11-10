from club import Club
from goalkeeper import Goalkeeper
from invalid_manager_error import InvalidManagerError
from manager import Manager
from outfield import Outfield
from too_many_goalkeepers_error import TooManyGoalkeepersError


class Team:
    """The 11 players and the manager(s) who play matches for a club.

    The players are kept in a list because order matters and the squad is
    filtered and counted often. The nationalities are kept in a set because
    each country only needs to be recorded once, however many players share
    it."""

    SQUAD_SIZE = 11  # A starting team always has exactly 11 players.

    def __init__(self, club):
        # The team belongs to one club, so the club must be a Club object.
        if isinstance(club, Club):
            self.club = club
        else:
            self.club = None
            print("Club is invalid.")

        # These are private so the only way to change the squad is through
        # the add and remove methods below, which check every change.
        self.__players = []
        self.__managers = []
        self.__nationalities = set()
        # A team can only have one goalkeeper, so this tracks whether the
        # goalkeeper spot is taken.
        self.__gk_count = 0

    @property
    def players(self):
        return list(self.__players)

    @property
    def managers(self):
        return list(self.__managers)

    @property
    def nationalities(self):
        return set(self.__nationalities)

    def add_player(self, player):
        # Each check below silently ignores a player who should not be added,
        # so a bad player can never get into the squad.
        # Only goalkeepers and outfield players can be added.
        if not isinstance(player, (Goalkeeper, Outfield)):
            return
        # The player must play for this club and must not already be in the
        # squad.
        if player.club != self.club or player in self.__players:
            return
        # The starting team is full once it has 11 players.
        if len(self.__players) >= Team.SQUAD_SIZE:
            return

        # A team can only have one goalkeeper. A second one is refused with an
        # exception before anything is changed, so the team is never left in
        # an invalid state.
        if isinstance(player, Goalkeeper):
            if self.__gk_count == 1:
                raise TooManyGoalkeepersError(
                    f"{self.club} already has a goalkeeper, so "
                    f"{player.name} {player.surname} cannot be added."
                )
            self.__gk_count = 1

        self.__players.append(player)
        # A set ignores repeats, so a second player from the same country
        # does not add a second entry.
        self.__nationalities.add(player.nationality)

    def add_manager(self, manager):
        # Each way a manager can be wrong has its own message, and all of them
        # are checked before the team is changed.
        if not isinstance(manager, Manager):
            raise InvalidManagerError(
                "Only a Manager can be added as a team's manager."
            )
        if manager.club != self.club:
            raise InvalidManagerError(
                f"{manager.name} {manager.surname} does not work for "
                f"{self.club}."
            )
        if manager in self.__managers:
            raise InvalidManagerError(
                f"{manager.name} {manager.surname} is already in this team."
            )

        self.__managers.append(manager)

    def remove_player(self, player):
        # Only a player who is really in this team's squad can be removed.
        if not isinstance(player, (Goalkeeper, Outfield)):
            return
        if player.club != self.club or player not in self.__players:
            return

        # Removing the goalkeeper frees the goalkeeper spot again.
        if isinstance(player, Goalkeeper):
            self.__gk_count = 0
        self.__players.remove(player)

        # Another player may share this nationality, so the set is rebuilt
        # from the players who are left instead of just removing one country.
        self.__nationalities = set()
        for remaining in self.__players:
            self.__nationalities.add(remaining.nationality)

    def players_in_position(self, position):
        # Collects every player in the squad who plays the given position,
        # for example "GK" or "CB".
        matching = []
        for player in self.__players:
            if player.position == position:
                matching.append(player)
        return matching

    def players_rated_above(self, rating):
        # Collects every player whose rating is higher than the given number.
        strong = []
        for player in self.__players:
            if player.rating > rating:
                strong.append(player)
        return strong

    def squad_value(self):
        # Adds up each player's transfer value to get the value of the squad.
        total = 0
        for player in self.__players:
            total += player.value
        return total

    def has_nationality(self, country):
        # A set checks this quickly without looping through every player.
        return country in self.__nationalities

    def shared_nationalities(self, other_team):
        # The other team must be a Team, otherwise there is nothing to
        # compare and an empty set is returned.
        if not isinstance(other_team, Team):
            return set()
        # The and operator keeps only the countries that are shared.
        return self.__nationalities & other_team.nationalities

    def game_ready(self):
        # A team can only play with a full squad of 11 and at least one
        # manager.
        return (
            len(self.__players) == Team.SQUAD_SIZE
            and len(self.__managers) >= 1
        )

    def rating(self):
        """
        The team rating is the average rating of its players, rounded to
        2 decimal places. The manager is not included yet.
        """
        if len(self.__players) == 0:
            return 0

        total = 0
        for player in self.__players:
            total += player.rating
        return round(total / len(self.__players), 2)

    def select_player(self, player):
        # Pick a player for the team.

        try:
            self.add_player(player)
        except TooManyGoalkeepersError as error:
            print(f"Could not select player: {error}")

    def select_manager(self, manager):
        # Pick a manager for the team.

        try:
            self.add_manager(manager)
        except InvalidManagerError as error:
            print(f"Could not select manager: {error}")

    def __str__(self):
        # Shows the club and how full the team is.

        return (
            f"{self.club}: {len(self.__players)}/{Team.SQUAD_SIZE} "
            f"players, {len(self.__managers)} manager(s), "
            f"ready to play = {self.game_ready()}"
        )
