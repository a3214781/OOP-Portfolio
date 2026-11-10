from abc import ABC

from club import Club
from person import Person


class Player(Person, ABC):
    """A person who plays for a club. It stays abstract because every
    player is either a Goalkeeper or an Outfield player."""

    # A player is rated from 1 to 99, so no player can be perfect or have no
    # ability at all.
    MIN_RATING = 1
    MAX_RATING = 99

    def __init__(
        self,
        name,
        surname,
        age,
        nationality,
        position,
        club,
        value=0,
        rating=Person.DEFAULT_RATING,
    ):
        # The shared details (name, surname, age, nationality) are set up by
        # Person, so they are not repeated here.
        super().__init__(name, surname, age, nationality)

        # The position must be a string, otherwise a default is used so the
        # player can still be created.
        if isinstance(position, str):
            self.position = position
        else:
            self.position = "No Position"
            print("Position is invalid.")

        # The club starts as None so the player is still created if the club
        # is invalid, and the club can be set later with transfer().
        self.club = None
        if isinstance(club, Club):
            self.club = club
        else:
            print("Club is invalid.")

        # The transfer value must be a whole number that is not negative.
        # Bool is rejected.
        if (
            isinstance(value, int)
            and not isinstance(value, bool)
            and value >= 0
        ):
            self.value = value
        else:
            self.value = 0
            print("Value is invalid.")

        # The rating must be a whole number within the allowed range.
        if (
            isinstance(rating, int)
            and not isinstance(rating, bool)
            and Player.MIN_RATING <= rating <= Player.MAX_RATING
        ):
            self.rating = rating
        else:
            self.rating = Person.DEFAULT_RATING
            print("Rating is invalid.")

    def terminate_contract(self):
        # The player is left without a club, so they no longer count as part
        # of that club's team.
        self.club = None

    def transfer(self, club):
        # Only a Club object is accepted, so the player is never moved to
        # something that is not a club.
        if isinstance(club, Club):
            self.club = club

    def __str__(self):
        # The wording depends on whether the player has a club, so the
        # sentence is always correct. The value is shown with commas (for
        # example 35,000,000) to make large numbers easier to read.
        if self.club is not None:
            return (
                f"{self.name} {self.surname} is a {self.age} year old "
                f"from {self.nationality}, playing {self.position}, "
                f"currently playing for {self.club} with a transfer "
                f"value of {self.value:,}"
            )
        else:
            return (
                f"{self.name} {self.surname} is a {self.age} year old "
                f"from {self.nationality}, playing {self.position}, "
                f"currently without a club and with a transfer value "
                f"of {self.value:,}"
            )
