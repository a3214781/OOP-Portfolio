from player import Player


class Goalkeeper(Player):
    """A Player who plays in goal. Every team may only have one."""

    def __init__(
        self,
        name,
        surname,
        age,
        nationality,
        club,
        value=0,
        rating=Player.DEFAULT_RATING,
    ):
        # The position is always "GK" for a goalkeeper, so it is passed to
        # Player here instead of being asked for every time one is created.
        super().__init__(
            name, surname, age, nationality, "GK", club, value, rating
        )

    def role(self):
        # Person makes role() abstract, so this class has to answer it.
        return "Goalkeeper"

    def __str__(self):
        # "[GK]" is added in front, and super() builds the rest of the
        # sentence.
        return "[GK] " + super().__str__()
