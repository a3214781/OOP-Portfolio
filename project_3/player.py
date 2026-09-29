from country import Country
from club import Club


class Player:
    def __init__(self, name, surname, age, nationality, position, club, value=0):
        if isinstance(name, str):
            self.name = name
        if isinstance(surname, str):
            self.surname = surname
        if isinstance(age, int) and not isinstance(age, bool):
            self.age = age
        if isinstance(nationality, Country):
            self.nationality = nationality
        if isinstance(position, str):
            self.position = position

        self.club = None
        if isinstance(club, Club):
            self.club = club
        if isinstance(value, int) and not isinstance(value, bool):
            self.value = value

    def terminate_contract(self):
        self.club = None

    def __str__(self):
        if self.club is not None:
            return f"{self.name} {self.surname} is a {self.age} year old from {self.nationality}, playing {self.position}, currently playing for {self.club} with a transfer value of {self.value:,}"
        else:
            return f"{self.name} {self.surname} is a {self.age} year old from {self.nationality}, playing {self.position}, currently without a club and with a transfer value of {self.value:,}"
