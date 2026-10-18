from club import Club
from person import Person


class Manager(Person):
    def __init__(self, name, surname, age, nationality, club, rating=50):
        super().__init__(name, surname, age, nationality)

        self.club = None
        if isinstance(club, Club):
            self.club = club
        if isinstance(rating, int) and not isinstance(rating, bool) and (0 < rating < 100):
            self.rating = rating

    def terminate_contract(self):
        self.club = None

    def transfer(self, club):
        if isinstance(club, Club):
            self.club = club

    def __str__(self):
        if self.club is not None:
            return f"{self.name} {self.surname} is a {self.age} year old from {self.nationality}, currently managing {self.club}"
        else:
            return f"{self.name} {self.surname} is a {self.age} year old from {self.nationality}, currently without a club"
