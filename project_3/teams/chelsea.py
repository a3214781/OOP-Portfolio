from club import Club
from player import Goalkeeper, Outfield
from team import Team
from countries import *
from leagues import premier_league

chelsea = Club("Chelsea", england)

sanchez = Goalkeeper("Robert", "Sanchez", 28, spain, chelsea, 25000000, 79)
james = Outfield("Reece", "James", 26, england, "RB", chelsea, 50000000, 83)
colwill = Outfield("Levi", "Colwill", 23, england, "CB", chelsea, 50000000, 80)
chalobah = Outfield("Trevoh", "Chalobah", 27, england,
                    "CB", chelsea, 35000000, 79)
cucurella = Outfield("Marc", "Cucurella", 28, spain,
                     "LB", chelsea, 40000000, 82)
caicedo = Outfield("Moises", "Caicedo", 25, ecuador,
                   "CM", chelsea, 80000000, 84)
enzo = Outfield("Enzo", "Fernandez", 25, argentina,
                "CM", chelsea, 80000000, 84)
palmer = Outfield("Cole", "Palmer", 24, england, "CAM", chelsea, 100000000, 87)
neto = Outfield("Pedro", "Neto", 26, portugal, "RW", chelsea, 55000000, 82)
estevao = Outfield("Estevao", "Willian", 19, brazil,
                   "LW", chelsea, 60000000, 80)
joao_pedro = Outfield("Joao", "Pedro", 25, brazil, "ST", chelsea, 60000000, 82)

chelsea_xi = Team(chelsea)
chelsea_xi.add_player(sanchez)
chelsea_xi.add_player(james)
chelsea_xi.add_player(colwill)
chelsea_xi.add_player(chalobah)
chelsea_xi.add_player(cucurella)
chelsea_xi.add_player(caicedo)
chelsea_xi.add_player(enzo)
chelsea_xi.add_player(palmer)
chelsea_xi.add_player(neto)
chelsea_xi.add_player(estevao)
chelsea_xi.add_player(joao_pedro)

chelsea.team = chelsea_xi
premier_league.add_club(chelsea)
