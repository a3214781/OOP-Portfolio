from player import Player


class Outfield(Player):
    """A Player who plays anywhere except in goal."""

    def role(self):
        # Person makes role() abstract, so this class has to answer it. This
        # lets the program ask any person for their role without checking
        # what type they are.
        return "Outfield player"

    def __str__(self):
        # The position is added in front, and super() builds the rest of the
        # sentence so the shared wording is not repeated here.
        return f"[{self.position}] " + super().__str__()
