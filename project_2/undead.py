class Undead:
    """Represents the common state and behaviour shared by every summoned
    undead creature.

    Subclasses may override MIN_HEALTH, MAX_HEALTH, MIN_POWER, and MAX_POWER
    with their own class-level constants. __init__ and level_up() read these
    through self.CONSTANT so an overridden value in a subclass is respected."""

    # These are the default CONSTs for the undead creatures.
    MIN_HEALTH = 10
    MAX_HEALTH = 500
    MIN_POWER = 1
    MAX_POWER = 100
    MAX_LEVEL = 20

    # How much health and power an undead gains each time it levels up.
    HEALTH_PER_LEVEL = 10
    POWER_PER_LEVEL = 2

    def __init__(self, unit_id, name, health, power):
        # The identifier and name must be strings, otherwise an empty string
        # is used so the undead can still be created. They are private
        # because subclasses dont need to change them.
        if isinstance(unit_id, str):
            self.__unit_id = unit_id
        else:
            self.__unit_id = ""

        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = ""

        # Health and power are protected because subclasses use them in
        # their own methods, such as command(). They must be whole numbers
        # inside the limits, and self is used instead of Undead so each
        # subclass is checked against its own limits. Bool is rejected
        # because Python treats True as the number 1.
        if (
            isinstance(health, int)
            and not isinstance(health, bool)
            and self.MIN_HEALTH <= health <= self.MAX_HEALTH
        ):
            self._health = health
        else:
            self._health = self.MIN_HEALTH
            print(f"Health is invalid. Defaulting to {self.MIN_HEALTH}.")

        if (
            isinstance(power, int)
            and not isinstance(power, bool)
            and self.MIN_POWER <= power <= self.MAX_POWER
        ):
            self._power = power
        else:
            self._power = self.MIN_POWER
            print(f"Power is invalid. Defaulting to {self.MIN_POWER}.")

        # Every undead starts at level 1. It is not a parameter, so a summon
        # cannot start at a higher level.
        self.__level = 1

    @property
    def unit_id(self):
        return self.__unit_id

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self._health

    @property
    def power(self):
        return self._power

    @property
    def level(self):
        return self.__level

    def level_up(self):
        # Returns True or False so the caller knows if the level went up.
        if self.__level >= self.MAX_LEVEL:
            print(f"{self.__name} is already at maximum level")
            return False

        self.__level += 1

        # Health and power are capped at the maximum for this type of undead,
        # so levelling never pushes them past their limit.
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
        # The general behaviour that suits any undead. Subclasses override
        # this and call super().command() so this line is still printed.
        print(f"{self.__name} obeys the necromancer's command.")

    def __str__(self):
        # The maximums are shown next to the current values so the player can
        # see how close the undead is to its limit.
        return (
            f"{self.__name} (ID: {self.__unit_id}) - Level {self.__level}, "
            f"Health: {self._health}/{self.MAX_HEALTH}, "
            f"Power: {self._power}/{self.MAX_POWER}"
        )

    def __repr__(self):
        # type(self).__name__ gives the real class, so a DeathKnight shows as
        # DeathKnight and not as Undead.
        return (
            f"{type(self).__name__}(unit_id={self.__unit_id}, "
            f"name={self.__name}, "
            f"level={self.__level}, health={self._health}, "
            f"power={self._power})"
        )
