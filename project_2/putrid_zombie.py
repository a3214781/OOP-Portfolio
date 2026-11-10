from undead import Undead


class PutridZombie(Undead):
    """An undead that is neither a warrior nor cursed, so it inherits
    straight from Undead."""

    MIN_HEALTH = 80
    MAX_HEALTH = 250
    MIN_POWER = 5
    MAX_POWER = 30

    def __init__(self, unit_id, name, health, power):
        super().__init__(unit_id, name, health, power)
