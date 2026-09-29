from country import Country
from club import Club
from league import League
from player import Player

# Making the country and league
england = Country("England")
premier_league = League("Premier League", england, 1)

# creating teams
arsenal = Club("Arsenal", england)
aston_villa = Club("Aston Villa", england)
bournemouth = Club("Bournemouth", england)
brentford = Club("Brentford", england)
brighton = Club("Brighton", england)
burnley = Club("Burnley", england)
chelsea = Club("Chelsea", england)
crystal_palace = Club("Crystal Palace", england)
everton = Club("Everton", england)
fulham = Club("Fulham", england)
leeds_united = Club("Leeds United", england)
liverpool = Club("Liverpool", england)
man_city = Club("Manchester City", england)
man_united = Club("Manchester United", england)
newcastle = Club("Newcastle United", england)
nottingham_forest = Club("Nottingham Forest", england)
sunderland = Club("Sunderland", england)
tottenham = Club("Tottenham", england)
west_ham = Club("West Ham", england)
wolves = Club("Wolverhampton", england)

# adding teams to league
premier_league.add_club(arsenal)
premier_league.add_club(aston_villa)
premier_league.add_club(bournemouth)
premier_league.add_club(brentford)
premier_league.add_club(brighton)
premier_league.add_club(burnley)
premier_league.add_club(chelsea)
premier_league.add_club(crystal_palace)
premier_league.add_club(everton)
premier_league.add_club(fulham)
premier_league.add_club(leeds_united)
premier_league.add_club(liverpool)
premier_league.add_club(man_city)
premier_league.add_club(man_united)
premier_league.add_club(newcastle)
premier_league.add_club(nottingham_forest)
premier_league.add_club(sunderland)
premier_league.add_club(tottenham)
premier_league.add_club(west_ham)
premier_league.add_club(wolves)

print(len(premier_league.clubs))  # 20
print(arsenal.league.name)        # Premier League
print(str(premier_league))
