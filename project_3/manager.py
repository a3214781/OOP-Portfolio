from club import Club
from person import Person


class Manager(Person):
    """A person who manages a club. Their rating adds to the team rating.
    Inherits attributes from Person class"""

    # A manager is rated from 1 to 99
    MIN_RATING = 1
    MAX_RATING = 99

    def __init__(
        self,
        name,
        surname,
        age,
        nationality,
        club,
        rating=Person.DEFAULT_RATING,
    ):
        # The shared details (name, surname, age, nationality) are set up by
        # Person, so they are not repeated here.
        super().__init__(name, surname, age, nationality)

        # The club starts as None so the manager is still created if the club
        # is invalid, and the club can be set later with transfer().
        self.club = None
        if isinstance(club, Club):
            self.club = club
        else:
            print("Club is invalid.")

        # The rating must be a whole number within the allowed range. Bool is
        # rejected because Python treats True as the number 1.
        if (
            isinstance(rating, int)
            and not isinstance(rating, bool)
            and Manager.MIN_RATING <= rating <= Manager.MAX_RATING
        ):
            self.rating = rating
        else:
            self.rating = Person.DEFAULT_RATING
            print("Rating is invalid.")

    def role(self):
        # Person makes this method abstract, so every kind of person has to
        # describe its own role. This lets the program ask any person for
        # their role without checking what type they are.
        return "Manager"

    def terminate_contract(self):
        # The manager is left without a club, which stops them from counting
        # as a club's manager.
        self.club = None
        return "Termination Complete"

    def transfer(self, club):
        # Only a Club object is accepted, so the manager is never moved to
        # something that is not a club.
        if isinstance(club, Club):
            self.club = club

    def __str__(self):
        # The wording depends on whether the manager has a club, so the
        # sentence is always correct.
        if self.club is not None:
            return (
                f"{self.name} {self.surname} is a {self.age} year old "
                f"from {self.nationality}, currently managing "
                f"{self.club}"
            )
        else:
            return (
                f"{self.name} {self.surname} is a {self.age} year old "
                f"from {self.nationality}, currently without a club"
            )
