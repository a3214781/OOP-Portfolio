from leagues import premier_league

import teams.man_united
import teams.liverpool
import teams.arsenal
import teams.chelsea

table = premier_league.play_season()
premier_league.print_table(table)
