from club import Club
from player import Player, Goalkeeper, Outfield
from team import Team
from countries import *
from leagues import premier_league

# Club
man_united = Club("Manchester United", england)

# Players
lammens = Goalkeeper("Senne", "Lammens", 24, belgium, man_united, 25000000, 81)
dalot = Outfield("Diogo", "Dalot", 27, portugal,
                 "RB", man_united, 40000000, 80)
de_ligt = Outfield("Matthijs", "de Ligt", 27, netherlands,
                   "CB", man_united, 40000000, 86)
martinez = Outfield("Lisandro", "Martinez", 28, argentina,
                    "CB", man_united, 45000000, 84)
shaw = Outfield("Luke", "Shaw", 31, england, "LB", man_united, 15000000, 81)
mainoo = Outfield("Kobbie", "Mainoo", 21, england,
                  "CM", man_united, 60000000, 87)
mount = Outfield("Mason", "Mount", 27, england, "CM", man_united, 40000000, 81)
fernandes = Outfield("Bruno", "Fernandes", 32, portugal,
                     "CAM", man_united, 50000000, 94)
mbeumo = Outfield("Bryan", "Mbeumo", 27, cameroon,
                  "RW", man_united, 65000000, 86)
cunha = Outfield("Matheus", "Cunha", 27, brazil,
                 "LW", man_united, 70000000, 84)
sesko = Outfield("Benjamin", "Sesko", 23, slovenia,
                 "ST", man_united, 75000000, 81)

# Team
united_xi = Team(man_united)
united_xi.add_player(lammens)
united_xi.add_player(dalot)
united_xi.add_player(de_ligt)
united_xi.add_player(martinez)
united_xi.add_player(shaw)
united_xi.add_player(mainoo)
united_xi.add_player(mount)
united_xi.add_player(fernandes)
united_xi.add_player(mbeumo)
united_xi.add_player(cunha)
united_xi.add_player(sesko)

man_united.team = united_xi
premier_league.add_club(man_united)
