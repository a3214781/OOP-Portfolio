from warrior_undead import WarriorUndead


class SkeletonWarrior(WarriorUndead):
    """A warrior undead with moderate health and low power."""

    # Only the limits that make this summon different are written here. The
    # rest is inherited.
    MIN_HEALTH = 60
    MAX_HEALTH = 200
    MIN_POWER = 10
    MAX_POWER = 40

    def __init__(self, unit_id, name, health, power):
        super().__init__(unit_id, name, health, power)
