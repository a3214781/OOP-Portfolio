from club import Club
from person import Person


class Player(Person):
    def __init__(self, name, surname, age, nationality, position, club, value=0, rating=50):
        super().__init__(name, surname, age, nationality)

        if isinstance(position, str):
            self.position = position
        self.club = None
        if isinstance(club, Club):
            self.club = club
        if isinstance(value, int) and not isinstance(value, bool):
            self.value = value
        if isinstance(rating, int) and not isinstance(rating, bool) and (0 < rating < 100):
            self.rating = rating

    def terminate_contract(self):
        self.club

    def transfer(self, club):
        if isinstance(club, Club):
            self.club = club

    def __str__(self):
        if self.club is not None:
            return f"{self.name} {self.surname} is a {self.age} year old from {self.nationality}, playing {self.position}, currently playing for {self.club} with a transfer value of {self.value:,}"
        else:
            return f"{self.name} {self.surname} is a {self.age} year old from {self.nationality}, playing {self.position}, currently without a club and with a transfer value of {self.value:,}"


class Goalkeeper(Player):
    def __init__(self, name, surname, age, nationality, club, value=0, rating=50):
        super().__init__(name, surname, age, nationality, "GK", club, value, rating)

    def __str__(self):
        return "[GK] " + super().__str__()


class Outfield(Player):
    def __str__(self):
        return f"[{self.position}] " + super().__str__()
