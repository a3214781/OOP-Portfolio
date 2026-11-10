# Project 3: Football League Simulation

## What the program represents
This program models a football league, where the league has clubs, clubs have teams, and teams are made up of players and manager(s). Every player, manager, and league also comes from a country.

This program can play out a full season between any teams and works with any number of clubs, able to print out a final table, and can also play matchups between 2 unique teams.

## What the objects can do
- **League:** this plays a season where every club hosts every other club, and prints the table.
- **Club:** belongs to a league and has one team. Its players and managers are held by that team.
- **Team:** holds players and managers that are in the starting 11 and are playing, and can check if it is ready to play (11 players, one goalkeeper and a manager). It can also work out its rating, squad value, and which nationalities its players share with another team.
- **Match:** plays a game between two teams and works out the score from their ratings and other random variance.
- **Player, Goalkeeper, Outfield and Manager:** all inherit from Person. Each one describes its own role, so the program does not need to check what type of person it has.
- **Country:** the nationality of a person, and the country of a league.

## Areas to extend
- Keep history of league tables so past seasons can be looked up. At the moment, the table is returned and not stored.
- Add more depth to player statistics such as goal scorers, clean sheets, etc.
- Use the league's division for promotion and relegation.
- A Cup class that inherits from a shared competition class.
- Add more variation in player statistics, such as an attack and defence score for individual players and managers, which impacts playstyle and in-turn results.