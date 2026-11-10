from undead import Undead


class CursedUndead(Undead):
    """Undead specialised for curse-based commands."""

    def __init__(self, unit_id, name, health, power):
        super().__init__(unit_id, name, health, power)

    def combat_style(self):
        # Same method name as in WarriorUndead, with a different answer.
        return f"cursed or supernatural combat"

    def command(self):
        print(f"{self.name} unleashes a curse, sapping the target's strength.")
        super().command()
