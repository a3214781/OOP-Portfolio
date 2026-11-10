import pytest
from club import Club
from country import Country
from goalkeeper import Goalkeeper
from invalid_manager_error import InvalidManagerError
from manager import Manager
from outfield import Outfield
from team import Team
from too_many_goalkeepers_error import TooManyGoalkeepersError


def make_outfield(england, club, number):
    # Each test player gets a different surname so they are easy to tell apart.
    return Outfield("Player", str(number), 25, england, "CM", club, 1000, 80)


def fill_squad(team, england, club):
    # A full squad needs one goalkeeper and ten outfield players.
    team.add_player(Goalkeeper("David", "Raya", 31, england, club, 1000, 84))
    for number in range(1, 11):
        team.add_player(make_outfield(england, club, number))


class TestTeam:
    """Tests for the Team class, checking how players and managers are
    added and removed, and when a team is ready to play."""

    # Each test gets a new country, club and team so tests can't affect each
    # other.
    @pytest.fixture
    def england(self):
        return Country("England")

    @pytest.fixture
    def club(self, england):
        return Club("Arsenal", england)

    @pytest.fixture
    def team(self, club):
        return Team(club)

    @pytest.fixture
    def manager(self, england, club):
        return Manager("Mikel", "Arteta", 44, england, club, 87)

    def test_add_player(self, team, england, club):
        # A player from the right club should join the squad.
        team.add_player(make_outfield(england, club, 1))
        assert len(team.players) == 1

    def test_player_from_other_club_is_not_added(self, team, england, club):
        # A player who plays for a different club must be refused.
        other = Club("Chelsea", england)
        player = Outfield("Player", "1", 25, england, "CM", other, 1000, 80)
        team.add_player(player)
        assert len(team.players) == 0

    def test_same_player_not_added_twice(self, team, england, club):
        # Adding the same player again should not work.
        player = make_outfield(england, club, 1)
        team.add_player(player)
        team.add_player(player)
        assert len(team.players) == 1

    def test_second_goalkeeper_raises(self, team, england, club):
        # Ensure a team only has one goalkeeper.
        team.add_player(
            Goalkeeper("David", "Raya", 31, england, club, 1000, 84)
        )
        second = Goalkeeper(
            "Kepa", "Arrizabalaga", 30, england, club, 1000, 70
        )
        with pytest.raises(TooManyGoalkeepersError):
            team.add_player(second)
        assert len(team.players) == 1

    def test_select_player_prints_goalkeeper_error(
        self, team, england, club, capsys
    ):
        # select_player should catch the error and print a message instead.
        team.select_player(
            Goalkeeper("David", "Raya", 31, england, club, 1000, 84)
        )
        second = Goalkeeper(
            "Kepa", "Arrizabalaga", 30, england, club, 1000, 70
        )
        team.select_player(second)
        assert "Could not select player" in capsys.readouterr().out
        assert len(team.players) == 1

    def test_manager_from_other_club_raises(self, team, england):
        # A manager who works for a different club must be refused.
        other = Club("Chelsea", england)
        outsider = Manager("Xabi", "Alonso", 44, england, other, 86)
        with pytest.raises(InvalidManagerError):
            team.add_manager(outsider)

    def test_game_ready_needs_eleven_players_and_manager(
        self, team, england, club, manager
    ):
        # The team is ready only with a full squad.
        fill_squad(team, england, club)
        assert not team.game_ready()
        team.add_manager(manager)
        assert team.game_ready()

    def test_twelfth_player_is_ignored(self, team, england, club):
        # A full squad of eleven should not accept another player.
        fill_squad(team, england, club)
        team.add_player(make_outfield(england, club, 11))
        assert len(team.players) == 11

    def test_remove_player(self, team, england, club):
        # A removed player should no longer be in the squad.
        player = make_outfield(england, club, 1)
        team.add_player(player)
        team.remove_player(player)
        assert len(team.players) == 0

    def test_removing_goalkeeper_frees_the_spot(self, team, england, club):
        # Once the goalkeeper leaves, a new one should be allowed in.
        keeper = Goalkeeper("David", "Raya", 31, england, club, 1000, 84)
        team.add_player(keeper)
        team.remove_player(keeper)
        team.add_player(
            Goalkeeper("Kepa", "Arrizabalaga", 30, england, club, 1000, 70)
        )
        assert len(team.players) == 1

    def test_squad_value_adds_up(self, team, england, club):
        # The squad value should be the total of every player's value.
        team.add_player(make_outfield(england, club, 1))
        team.add_player(make_outfield(england, club, 2))
        assert team.squad_value() == 2000

    def test_rating_is_average(self, team, england, club):
        # The team rating should be the average of the players' ratings.
        team.add_player(
            Outfield("Ann", "One", 25, england, "CM", club, 1000, 80)
        )
        team.add_player(
            Outfield("Ben", "Two", 25, england, "CM", club, 1000, 90)
        )
        assert team.rating() == 85.0

    def test_rating_of_empty_team_is_zero(self, team):
        # An empty team should not crash when its rating is asked for.
        # This test only passes after you add the empty-team check to rating().
        assert team.rating() == 0

    def test_nationalities_are_counted_once(self, team, england, club):
        # Two players from the same country should count as one nationality.
        team.add_player(make_outfield(england, club, 1))
        team.add_player(make_outfield(england, club, 2))
        assert len(team.nationalities) == 1
