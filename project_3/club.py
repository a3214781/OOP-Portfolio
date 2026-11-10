from country import Country


class Club:
    """A football club. It belongs to a country, joins a league and has
    one team that plays its matches."""

    def __init__(self, name, country):
        # The name must be a string, otherwise a default is used so the club
        # can still be created.
        if isinstance(name, str):
            self.name = name
        else:
            self.name = "No Name"
            print("Club name is invalid.")

        # The club keeps every player and manager it has signed
        # The team only holds the ones chosen to play.
        self.__players = []
        self.__managers = []

        # The country must be a Country object so a club is always linked to
        # a real country or to nothing at all.
        if isinstance(country, Country):
            self.country = country
        else:
            self.country = None
            print("Club country is invalid.")

        # These are filled in later by the league and the team.
        self.league = None
        self.team = None

    @property
    def players(self):
        return list(self.__players)

    @property
    def managers(self):
        return list(self.__managers)

    def sign_player(self, player):
        """Sign a player to this club's squad, which has no size limit.
        Returns True if the player was signed."""
        # Player is imported here instead of at the top to avoid a circular
        # import, because player.py imports Club.
        from player import Player

        if not isinstance(player, Player):
            print("Only a Player can be signed.")
            return False
        if player.club != self:
            print(
                f"{player.name} {player.surname} does not belong to "
                f"{self.name}."
            )
            return False
        if player in self.__players:
            print(f"{player.name} {player.surname} is already signed.")
            return False

        self.__players.append(player)
        return True

    def sign_manager(self, manager):
        """Sign a manager to this club. Returns True if they were signed."""
        from manager import Manager

        if not isinstance(manager, Manager):
            print("Only a Manager can be signed.")
            return False
        if manager.club != self:
            print(
                f"{manager.name} {manager.surname} does not belong to "
                f"{self.name}."
            )
            return False
        if manager in self.__managers:
            print(f"{manager.name} {manager.surname} is already signed.")
            return False

        self.__managers.append(manager)
        return True

    def __str__(self):
        # Only the name is returned so a club prints cleanly inside other
        # sentences, like a player's "currently playing for [club_name]".
        return self.name
