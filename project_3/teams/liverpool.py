from club import Club
from player import Goalkeeper, Outfield
from team import Team
from countries import *
from countries import england
from leagues import premier_league

liverpool = Club("Liverpool", england)

alisson = Goalkeeper("Alisson", "Becker", 34, brazil, liverpool, 20000000, 88)
frimpong = Outfield("Jeremie", "Frimpong", 25, netherlands,
                    "RB", liverpool, 40000000, 83)
konate = Outfield("Ibrahima", "Konate", 27, france,
                  "CB", liverpool, 50000000, 84)
van_dijk = Outfield("Virgil", "van Dijk", 35, netherlands,
                    "CB", liverpool, 20000000, 86)
kerkez = Outfield("Milos", "Kerkez", 22, hungary,
                  "LB", liverpool, 40000000, 79)
mac_allister = Outfield("Alexis", "Mac Allister", 27,
                        argentina, "CM", liverpool, 70000000, 85)
szoboszlai = Outfield("Dominik", "Szoboszlai", 25,
                      hungary, "CM", liverpool, 80000000, 85)
gravenberch = Outfield("Ryan", "Gravenberch", 24,
                       netherlands, "CM", liverpool, 70000000, 84)
salah = Outfield("Mohamed", "Salah", 34, egypt, "RW", liverpool, 40000000, 89)
isak = Outfield("Alexander", "Isak", 27, sweden, "ST", liverpool, 90000000, 86)
wirtz = Outfield("Florian", "Wirtz", 23, germany,
                 "CAM", liverpool, 120000000, 87)

liverpool_xi = Team(liverpool)
liverpool_xi.add_player(alisson)
liverpool_xi.add_player(frimpong)
liverpool_xi.add_player(konate)
liverpool_xi.add_player(van_dijk)
liverpool_xi.add_player(kerkez)
liverpool_xi.add_player(mac_allister)
liverpool_xi.add_player(szoboszlai)
liverpool_xi.add_player(gravenberch)
liverpool_xi.add_player(salah)
liverpool_xi.add_player(isak)
liverpool_xi.add_player(wirtz)

liverpool.team = liverpool_xi
premier_league.add_club(liverpool)
