from undead import Undead


class WarriorUndead(Undead):
    """Undead specialised for direct combat commands."""

    def __init__(self, unit_id, name, health, power):
        # The shared state is set up by Undead, so it is not repeated here.
        super().__init__(unit_id, name, health, power)

    def combat_style(self):
        # CursedUndead has a method with the same name. This is deliberate,
        # because DeathKnight inherits from both and has to choose.
        return f"direct martial combat"

    def command(self):
        # The warrior-specific line comes first, then super() adds the
        # general command line from Undead.
        print(
            f"{self.name} charges forward, striking with {self._power} power."
        )
        super().command()
