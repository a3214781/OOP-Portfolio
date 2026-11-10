from countries import england, spain
from goalkeeper import Goalkeeper
from leagues import premier_league
from manager import Manager
from person import Person
from player import Player
from teams.arsenal import arsenal, arsenal_xi, raya, saliba
from teams.chelsea import chelsea, chelsea_xi
from teams.liverpool import liverpool, liverpool_xi
from teams.man_united import man_united, united_xi

# --- Managers ---------------------------------------------------------
# A team is only ready to play once it has 11 players and a manager, so each
# club gets a manager before the season starts.
arteta = Manager("Mikel", "Arteta", 44, spain, arsenal, 87)
alonso = Manager("Xabi", "Alonso", 44, spain, chelsea, 86)
iraola = Manager("Andoni", "Iraola", 44, spain, liverpool, 83)
carrick = Manager("Michael", "Carrick", 45, england, man_united, 79)


arsenal_xi.select_manager(arteta)
chelsea_xi.select_manager(alonso)
liverpool_xi.select_manager(iraola)
united_xi.select_manager(carrick)

# This section shows the chain League -> Club -> Team -> players, by printing
# each team's size, readiness and rating.
print("=== Soccer Game ===")
print("--- Objects and relationships ---")
print(premier_league.name, "has", len(premier_league.clubs), "clubs.")
for team in (arsenal_xi, chelsea_xi, liverpool_xi, united_xi):
    print(
        f"{team.club}: {len(team.players)} players, "
        f"ready to play = {team.game_ready()}, "
        f"rating = {team.rating()}"
    )
print()
print(arteta)
print(raya)
print()

print("--- Inheritance and abstraction ---")
# Goalkeeper -> Player -> Person, so one object is all three at once.
print("Raya is a Goalkeeper:", isinstance(raya, Goalkeeper))
print("Raya is a Player:", isinstance(raya, Player))
print("Raya is a Person:", isinstance(raya, Person))
print("Arteta is a Player:", isinstance(arteta, Player))
print()

print("--- Polymorphism ---")
# The loop never checks the type: each object answers role() in its own way.
for person in (raya, saliba, arteta):
    print(f"{person.name} {person.surname}: {person.role()}")
print()

# A list suits the squad because players are added and removed, and it can
# be filtered by position or rating.
print("--- Data structure 1: list of players ---")
goalkeepers = arsenal_xi.players_in_position("GK")
centre_backs = arsenal_xi.players_in_position("CB")
top_rated = arsenal_xi.players_rated_above(85)
print("Goalkeepers:")
for player in goalkeepers:
    print("  ", player.surname)
print("Centre backs:")
for player in centre_backs:
    print("  ", player.surname)
print("Rated above 85:")
for player in top_rated:
    print("  ", player.surname)
print(f"Squad value: {arsenal_xi.squad_value():,}")
# Removing a player shrinks the list, which makes the team not ready.
arsenal_xi.remove_player(saliba)
print(
    "After removing Saliba:",
    len(arsenal_xi.players),
    "players, ready =",
    arsenal_xi.game_ready(),
)
arsenal_xi.select_player(saliba)
print(
    "After adding him back:",
    len(arsenal_xi.players),
    "players, ready =",
    arsenal_xi.game_ready(),
)
print()

# A set suits nationalities because each country is only stored once, so its
# length counts different countries and two teams' sets can be compared.
print("--- Data structure 2: set of nationalities ---")
print("Arsenal players:", len(arsenal_xi.players))
print("Arsenal nationalities:", len(arsenal_xi.nationalities))
print("Includes Spain:", arsenal_xi.has_nationality(spain))
shared = arsenal_xi.shared_nationalities(chelsea_xi)
print("Arsenal and Chelsea both have players from:")
for country in shared:
    print("  ", country)
print()

print("--- Exceptions ---")
# A team can only have one goalkeeper.
# A player is removed first to make room, because a full team
# is refused before the goalkeeper check is reached.
arsenal_xi.remove_player(saliba)
kepa = Goalkeeper("Kepa", "Arrizabalaga", 30, spain, arsenal, 1000000, 70)
arsenal_xi.select_player(kepa)

# A manager from another club cannot manage this team.
# backup manager
holland = Manager("Steve", "Holland", 56, england, man_united, 83)
arsenal_xi.select_manager(holland)

# A team that is not ready cannot play.
# Arsenal has 10 players right now, so the league
# skips its matches and the rest of the season carries on.
print("Playing a season while Arsenal is not ready:")
premier_league.play_season()
arsenal_xi.select_player(saliba)
print("Arsenal ready again:", arsenal_xi.game_ready())
print()

# The league plays every club against every other club,
# then prints the table.
print("--- Season simulation ---")
table = premier_league.play_season()
premier_league.print_table(table)
