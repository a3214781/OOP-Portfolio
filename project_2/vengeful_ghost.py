from cursed_undead import CursedUndead


class VengefulGhost(CursedUndead):
    """A cursed undead with low health and high power."""

    MIN_HEALTH = 30
    MAX_HEALTH = 120
    MIN_POWER = 25
    MAX_POWER = 80

    def __init__(self, unit_id, name, health, power):
        super().__init__(unit_id, name, health, power)
