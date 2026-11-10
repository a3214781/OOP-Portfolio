from warrior_undead import WarriorUndead
from cursed_undead import CursedUndead


class DeathKnight(WarriorUndead, CursedUndead):
    """An undead that is both a warrior and cursed, both
    parents lead back to Undead, which Python only uses once."""

    # The strongest summon, with the highest limits and its own growth.
    MIN_HEALTH = 200
    MAX_HEALTH = 600
    MIN_POWER = 25
    MAX_POWER = 75
    HEALTH_PER_LEVEL = 8
    POWER_PER_LEVEL = 3

    def __init__(self, unit_id, name, health=300, power=40):
        # super() follows the method resolution order (MRO), so both parents
        # and Undead are set up once each.
        super().__init__(unit_id, name, health, power)

    # Inherits WarriorUndead (direct martial combat)
    def combat_style(self):
        # WarriorUndead is listed first in the class line, so it comes first
        # in the MRO, and super() picks its answer.
        return super().combat_style()

    def compare_combat_styles(self):
        # Calling each parent class by name picks that exact version, instead
        # of letting the MRO choose. This is useful here because the point is
        # to compare both.
        return (
            f"{WarriorUndead.combat_style(self)} / "
            f"{CursedUndead.combat_style(self)}"
        )
