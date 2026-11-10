from warrior_undead import WarriorUndead


class PhantomGuardian(WarriorUndead):
    """A warrior undead with very high health."""

    MIN_HEALTH = 150
    MAX_HEALTH = 400
    MIN_POWER = 20
    MAX_POWER = 60

    def __init__(self, unit_id, name, health, power):
        super().__init__(unit_id, name, health, power)
