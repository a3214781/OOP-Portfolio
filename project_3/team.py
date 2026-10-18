from player import Goalkeeper, Outfield
from manager import Manager
from club import Club


class Team:

    def __init__(self, club):
        if isinstance(club, Club):
            self.club = club

        self.players = []
        self.managers = []
        self.gk_count = 0

    def add_player(self, player):
        if isinstance(player, Goalkeeper) and player.club == self.club and player not in self.players and len(self.players) < 11:
            if self.gk_count == 0:
                self.gk_count = 1
                self.players.append(player)
            else:
                raise ValueError("too many keepers")

        if isinstance(player, Outfield) and player.club == self.club and player not in self.players and len(self.players) < 11:
            self.players.append(player)

    def add_manager(self, manager):
        if isinstance(manager, Manager) and manager.club == self.club and manager not in self.managers:
            self.managers.append(manager)
        else:
            return f"This is not a manager"

    def remove_player(self, player):
        if isinstance(player, Goalkeeper) and player.club == self.club and player in self.players:
            self.gk_count = 0
            self.players.remove(player)

        if isinstance(player, Outfield) and player.club == self.club and player in self.players:
            self.players.remove(player)

    def game_ready(self):
        return len(self.players) == 11 and len(self.managers) >= 1

    def rating(self):
        total = 0
        for player in self.players:
            total += player.rating
        return round(total / len(self.players), 5)
