from club import Club
from player import Goalkeeper, Outfield
from team import Team
from countries import *
from leagues import premier_league

arsenal = Club("Arsenal", england)

raya = Goalkeeper("David", "Raya", 31, spain, arsenal, 35000000, 84)
timber = Outfield("Jurrien", "Timber", 25, netherlands,
                  "RB", arsenal, 60000000, 83)
saliba = Outfield("William", "Saliba", 25, france, "CB", arsenal, 90000000, 88)
gabriel = Outfield("Gabriel", "Magalhaes", 28, brazil,
                   "CB", arsenal, 75000000, 86)
calafiori = Outfield("Riccardo", "Calafiori", 24,
                     italy, "LB", arsenal, 50000000, 82)
rice = Outfield("Declan", "Rice", 27, england, "CM", arsenal, 100000000, 88)
zubimendi = Outfield("Martin", "Zubimendi", 27, spain,
                     "CM", arsenal, 60000000, 84)
odegaard = Outfield("Martin", "Odegaard", 27, norway,
                    "CAM", arsenal, 70000000, 87)
saka = Outfield("Bukayo", "Saka", 25, england, "RW", arsenal, 120000000, 88)
gyokeres = Outfield("Viktor", "Gyokeres", 28, sweden,
                    "ST", arsenal, 70000000, 85)
martinelli = Outfield("Gabriel", "Martinelli", 25,
                      brazil, "LW", arsenal, 60000000, 83)


arsenal_xi = Team(arsenal)
arsenal_xi.add_player(raya)
arsenal_xi.add_player(timber)
arsenal_xi.add_player(saliba)
arsenal_xi.add_player(gabriel)
arsenal_xi.add_player(calafiori)
arsenal_xi.add_player(rice)
arsenal_xi.add_player(zubimendi)
arsenal_xi.add_player(odegaard)
arsenal_xi.add_player(saka)
arsenal_xi.add_player(gyokeres)
arsenal_xi.add_player(martinelli)

arsenal.team = arsenal_xi
premier_league.add_club(arsenal)
