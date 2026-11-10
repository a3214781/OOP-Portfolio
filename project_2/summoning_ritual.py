from death_knight import DeathKnight
from inventory import Inventory
from phantom_guardian import PhantomGuardian
from putrid_zombie import PutridZombie
from skeleton_warrior import SkeletonWarrior
from undead import Undead
from vengeful_ghost import VengefulGhost


class SummoningRitual:
    """A ritual identifies which specialised Undead subclass
    it summons, so create_summon() always produces the right type.

    A ritual describes what a summon costs and what it creates,
    and dosen't hold any resources itself, because spending
    them is the job of the Inventory."""

    def __init__(
        self,
        ritual_name,
        undead_name,
        undead_class,
        starting_health,
        starting_power,
        ectoplasm_cost=1,
        necrotic_cost=0,
        spirit_cost=0,
        bone_cost=0,
        flesh_cost=0,
    ):

        # The names go through the same helper so a bad name becomes an empty
        # string instead of repeating the check twice.
        self.__ritual_name = self.check_inventory_name(ritual_name)
        self.__undead_name = self.check_inventory_name(undead_name)

        # The class must be a subclass of Undead, so create_summon() can
        # always build it the same way, if not it falls back to Undead.
        if isinstance(undead_class, type) and issubclass(undead_class, Undead):
            self.__undead_class = undead_class
        else:
            self.__undead_class = Undead
            print("Undead class is invalid. Defaulting to Undead.")

        # The starting health must fit inside the limits of the undead this:
        if (
            isinstance(starting_health, int)
            and not isinstance(starting_health, bool)
            and self.__undead_class.MIN_HEALTH
            <= starting_health
            <= self.__undead_class.MAX_HEALTH
        ):
            self.__starting_health = starting_health
        else:
            self.__starting_health = self.__undead_class.MIN_HEALTH

        # The same applies to the starting power.
        if (
            isinstance(starting_power, int)
            and not isinstance(starting_power, bool)
            and self.__undead_class.MIN_POWER
            <= starting_power
            <= self.__undead_class.MAX_POWER
        ):
            self.__starting_power = starting_power
        else:
            self.__starting_power = self.__undead_class.MIN_POWER

        # The rune costs may be 0 because different rituals use different
        # combinations of runes.
        self.__necrotic_cost = self.check_inventory_cost(necrotic_cost)
        self.__spirit_cost = self.check_inventory_cost(spirit_cost)
        self.__bone_cost = self.check_inventory_cost(bone_cost)
        self.__flesh_cost = self.check_inventory_cost(flesh_cost)

        # Every ritual requires Ectoplasm, so this can never be 0
        if (
            isinstance(ectoplasm_cost, int)
            and not isinstance(ectoplasm_cost, bool)
            and ectoplasm_cost > 0
        ):
            self.__ectoplasm_cost = ectoplasm_cost
        else:
            self.__ectoplasm_cost = 1

    # Checkers
    # The static method only checks that the value they are given
    # and do not need any data from a SummoningRitual object.
    @staticmethod
    def check_inventory_cost(qty):
        # A cost must be a positive whole number or becomes 0,
        # meaning the ritual does not need that rune.
        # Bool is also rejected because.
        if isinstance(qty, int) and not isinstance(qty, bool) and qty > 0:
            return qty
        else:
            return 0

    @staticmethod
    def check_inventory_name(name):
        # A name must be a string, otherwise it becomes an empty string.
        if isinstance(name, str):
            return name
        else:
            return ""

    @property
    def ritual_name(self):
        return self.__ritual_name

    @property
    def undead_name(self):
        return self.__undead_name

    @property
    def undead_class(self):
        return self.__undead_class

    @property
    def starting_health(self):
        return self.__starting_health

    @property
    def starting_power(self):
        return self.__starting_power

    @property
    def necrotic_cost(self):
        return self.__necrotic_cost

    @property
    def spirit_cost(self):
        return self.__spirit_cost

    @property
    def bone_cost(self):
        return self.__bone_cost

    @property
    def flesh_cost(self):
        return self.__flesh_cost

    @property
    def ectoplasm_cost(self):
        return self.__ectoplasm_cost

    def __get_costs(self):
        # The costs are returned as a list in the order the Inventory expects:
        # necrotic, spirit, bone, flesh, ectoplasm. This method is private
        # because only the ritual's methods below need to build the list.
        return [
            self.__necrotic_cost,
            self.__spirit_cost,
            self.__bone_cost,
            self.__flesh_cost,
            self.__ectoplasm_cost,
        ]

    def can_perform(self, inventory):
        # Only a real Inventory can be checked. The Inventory does the
        # checking itself, because it is the one that knows what it holds.
        if not isinstance(inventory, Inventory):
            return False
        return inventory.resource_requirements(self.__get_costs())

    def consume_resources(self, inventory):
        # The ritual passes its costs to the Inventory and lets it change its
        # own amounts, so the ritual never edits another object's data, and
        # it returns True or False so the caller knows if the spend worked.
        if not isinstance(inventory, Inventory):
            return False
        return inventory.spend_resource(self.__get_costs())

    def create_summon(self, unit_id):
        # The ritual builds the right type of undead from its own class and
        # starting stats. The identifier is supplied by the Necromancer so
        # every summon gets a unique one.
        return self.__undead_class(
            unit_id,
            self.__undead_name,
            self.__starting_health,
            self.__starting_power,
        )

    def __str__(self):
        # Shows what the ritual creates and everything it costs, so a ritual
        # can be inspected during a demonstration.
        return (
            f"{self.__ritual_name} -> {self.__undead_name} "
            f"(Health: {self.__starting_health}, "
            f"Power: {self.__starting_power}) | "
            f"Costs - Necrotic: {self.__necrotic_cost}, "
            f"Spirit: {self.__spirit_cost}, "
            f"Bone: {self.__bone_cost}, "
            f"Flesh: {self.__flesh_cost}, "
            f"Ectoplasm: {self.__ectoplasm_cost}"
        )


# ritual instances
# Each ritual uses a different mix of runes, and the stronger summons cost
# more. Every ritual needs Ectoplasm.

skeleton_warrior_ritual = SummoningRitual(
    "Skeleton Rising",
    "Undead Skeleton Warrior",
    SkeletonWarrior,
    80,
    15,
    necrotic_cost=5,
    bone_cost=15,
    ectoplasm_cost=10,
)

vengeful_ghost_ritual = SummoningRitual(
    "Spectral Binding",
    "Vengeful Ghost",
    VengefulGhost,
    50,
    25,
    necrotic_cost=5,
    spirit_cost=20,
    ectoplasm_cost=15,
)

putrid_zombie_ritual = SummoningRitual(
    "Corpse Reanimation",
    "Putrid Zombie",
    PutridZombie,
    120,
    10,
    necrotic_cost=5,
    flesh_cost=20,
    ectoplasm_cost=10,
)

phantom_guardian_ritual = SummoningRitual(
    "Guardian's Vigil",
    "Phantom Guardian",
    PhantomGuardian,
    150,
    30,
    necrotic_cost=10,
    spirit_cost=15,
    bone_cost=10,
    flesh_cost=10,
    ectoplasm_cost=30,
)

death_knight_ritual = SummoningRitual(
    "Skeleton King",
    "Death Knight",
    DeathKnight,
    220,
    30,
    necrotic_cost=20,
    spirit_cost=25,
    ectoplasm_cost=40,
    bone_cost=5,
    flesh_cost=10,
)
