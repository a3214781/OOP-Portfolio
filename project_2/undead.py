class Undead:
    """Represents the common state and behaviour shared by every summoned
    undead creature (identifier, name, health, power, level).

    Subclasses may override MIN_HEALTH / MAX_HEALTH / MIN_POWER / MAX_POWER
    with their own class-level constants. __init__ and level_up() read these
    through self.<CONST> so an overridden value in a
    subclass is actually respected instead of being silently ignored.
    """

    MIN_HEALTH = 10
    MAX_HEALTH = 500
    MIN_POWER = 1
    MAX_POWER = 100
    MAX_LEVEL = 20

    HEALTH_PER_LEVEL = 10
    POWER_PER_LEVEL = 2

    def __init__(self, unit_id, name, health, power):
        if isinstance(unit_id, str):
            self.__unit_id = unit_id
        else:
            self.__unit_id = ""

        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = ""

        if isinstance(health, int) and not isinstance(health, bool) and self.MIN_HEALTH <= health <= self.MAX_HEALTH:
            self._health = health
        else:
            self._health = self.MIN_HEALTH
            print(f"Health is invalid. Defaulting to {self.MIN_HEALTH}.")

        if isinstance(power, int) and not isinstance(power, bool) and self.MIN_POWER <= power <= self.MAX_POWER:
            self._power = power
        else:
            self._power = self.MIN_POWER
            print(f"Power is invalid. Defaulting to {self.MIN_POWER}.")

        self.__level = 1

    # getters
    def get_unit_id(self):
        return self.__unit_id

    def get_name(self):
        return self.__name

    def get_health(self):
        return self._health

    def get_power(self):
        return self._power

    def get_level(self):
        return self.__level

    unit_id = property(get_unit_id)
    name = property(get_name)
    health = property(get_health)
    power = property(get_power)
    level = property(get_level)

    def level_up(self):
        if self.__level >= self.MAX_LEVEL:
            print(f"{self.__name} is already at maximum level")
            return False

        self.__level += 1

        new_health = self._health + self.HEALTH_PER_LEVEL
        if new_health > self.MAX_HEALTH:
            new_health = self.MAX_HEALTH
        self._health = new_health

        new_power = self._power + self.POWER_PER_LEVEL
        if new_power > self.MAX_POWER:
            new_power = self.MAX_POWER
        self._power = new_power

        print(f"{self.__name} levelled up to level {self.__level}")
        return True

    def command(self):
        print(f"{self.__name} obeys the necromancer's command.")

    def __str__(self):
        return (f"{self.__name} (ID: {self.__unit_id}) - Level {self.__level}, "
                f"Health: {self._health}, Power: {self._power}")

    def __repr__(self):
        return (f"{type(self).__name__}(unit_id={self.__unit_id}, name={self.__name}, "
                f"level={self.__level}, health={self._health}, power={self._power})")


class WarriorUndead(Undead):
    """Undead specialised for direct combat commands."""

    def __init__(self, unit_id, name, health, power):
        super().__init__(unit_id, name, health, power)

    def combat_style(self):
        return f"direct martial combat"

    def command(self):
        print(f"{self.get_name()} charges forward, striking with {self._power} power.")
        super().command()


class CursedUndead(Undead):
    """Undead specialised for draining, curse-based commands."""

    def __init__(self, unit_id, name, health, power):
        super().__init__(unit_id, name, health, power)

    def combat_style(self):
        return f"cursed or supernatural combat"

    def command(self):
        print(f"{self.get_name()} unleashes a curse, sapping the target's strength.")
        super().command()


class SkeletonWarrior(WarriorUndead):

    MIN_HEALTH = 60
    MAX_HEALTH = 200
    MIN_POWER = 10
    MAX_POWER = 40

    def __init__(self, unit_id, name, health, power):
        super().__init__(unit_id, name, health, power)


class PhantomGuardian(WarriorUndead):

    MIN_HEALTH = 150
    MAX_HEALTH = 400
    MIN_POWER = 20
    MAX_POWER = 60

    def __init__(self, unit_id, name, health, power):
        super().__init__(unit_id, name, health, power)


class VengefulGhost(CursedUndead):

    MIN_HEALTH = 30
    MAX_HEALTH = 120
    MIN_POWER = 25
    MAX_POWER = 80

    def __init__(self, unit_id, name, health, power):
        super().__init__(unit_id, name, health, power)


class PutridZombie(Undead):
    MIN_HEALTH = 80
    MAX_HEALTH = 250
    MIN_POWER = 5
    MAX_POWER = 30

    def __init__(self, unit_id, name, health, power):
        super().__init__(unit_id, name, health, power)


class DeathKnight(WarriorUndead, CursedUndead):
    MIN_HEALTH = 200
    MAX_HEALTH = 600
    MIN_POWER = 25
    MAX_POWER = 75
    HEALTH_PER_LEVEL = 8
    POWER_PER_LEVEL = 3

    def __init__(self, unit_id, name, health=300, power=40):
        super().__init__(unit_id, name, health, power)

    # inherits WarriorUndead (direct martial combat)
    def combat_style(self):
        return super().combat_style()

    def compare_combat_styles(self):
        print(WarriorUndead.combat_style(self))
        print(CursedUndead.combat_style(self))

    def level_up(self):
        if self.__level >= self.MAX_LEVEL:
            print(f"{self.__name} is already at maximum level")
            return False

        self.__level += 1

        new_health = self._health + self.HEALTH_PER_LEVEL
        if new_health > self.MAX_HEALTH:
            new_health = self.MAX_HEALTH
        self._health = new_health

        new_power = self._power + self.POWER_PER_LEVEL
        if new_power > self.MAX_POWER:
            new_power = self.MAX_POWER
        self._power = new_power

        print(f"{self.__name} levelled up to level {self.__level}")
        return True


undead_1 = DeathKnight(1, "al", 300, 30)
print(undead_1.combat_style())
print(undead_1.compare_combat_styles())
