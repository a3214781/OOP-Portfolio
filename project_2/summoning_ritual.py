from inventory import Inventory
from undead import Undead, SkeletonWarrior, VengefulGhost, PutridZombie, PhantomGuardian, DeathKnight


class SummoningRitual:
    """A ritual identifies which specialised Undead subclass it summons
    (undead_class), so create_summon() always produces the right type
    instead of a plain Undead."""

    def __init__(self, ritual_name, undead_name, undead_class, starting_health, starting_power,
                 ectoplasm_cost=1, necrotic_cost=0, spirit_cost=0, bone_cost=0, flesh_cost=0):

        self.__ritual_name = self.check_inventory_name(ritual_name)
        self.__undead_name = self.check_inventory_name(undead_name)

        if isinstance(undead_class, type) and issubclass(undead_class, Undead):
            self.__undead_class = undead_class
        else:
            self.__undead_class = Undead
            print("Undead class is invalid. Defaulting to Undead.")

        if (isinstance(starting_health, int) and not isinstance(starting_health, bool)
                and self.__undead_class.MIN_HEALTH <= starting_health <= self.__undead_class.MAX_HEALTH):
            self.__starting_health = starting_health
        else:
            self.__starting_health = self.__undead_class.MIN_HEALTH

        if (isinstance(starting_power, int) and not isinstance(starting_power, bool)
                and self.__undead_class.MIN_POWER <= starting_power <= self.__undead_class.MAX_POWER):
            self.__starting_power = starting_power
        else:
            self.__starting_power = self.__undead_class.MIN_POWER

        self.__necrotic_cost = self.check_inventory_cost(necrotic_cost)
        self.__spirit_cost = self.check_inventory_cost(spirit_cost)
        self.__bone_cost = self.check_inventory_cost(bone_cost)
        self.__flesh_cost = self.check_inventory_cost(flesh_cost)

        # every ritual requires Ectoplasm, so this can never be 0
        if isinstance(ectoplasm_cost, int) and not isinstance(ectoplasm_cost, bool) and ectoplasm_cost > 0:
            self.__ectoplasm_cost = ectoplasm_cost
        else:
            self.__ectoplasm_cost = 1
            
    # checkers
    def check_inventory_cost(qty):
        if isinstance(qty, int) and not isinstance(qty, bool) and qty > 0:
            return qty
        else:
            return 0

    def check_inventory_name(name):
        if isinstance(name, str):
            return name
        else:
            return ""

    # getters
    def get_ritual_name(self):
        return self.__ritual_name

    def get_undead_name(self):
        return self.__undead_name

    def get_undead_class(self):
        return self.__undead_class

    def get_starting_health(self):
        return self.__starting_health

    def get_starting_power(self):
        return self.__starting_power

    def get_necrotic_cost(self):
        return self.__necrotic_cost

    def get_spirit_cost(self):
        return self.__spirit_cost

    def get_bone_cost(self):
        return self.__bone_cost

    def get_flesh_cost(self):
        return self.__flesh_cost

    def get_ectoplasm_cost(self):
        return self.__ectoplasm_cost
    
    def __get_costs(self):
        return {
            "necrotic": self.__necrotic_cost,
            "spirit": self.__spirit_cost,
            "bone": self.__bone_cost,
            "flesh": self.__flesh_cost,
            "ectoplasm": self.__ectoplasm_cost,
        }

    # read-only properties
    ritual_name = property(get_ritual_name)
    undead_name = property(get_undead_name)
    undead_class = property(get_undead_class)
    starting_health = property(get_starting_health)
    starting_power = property(get_starting_power)
    necrotic_cost = property(get_necrotic_cost)
    spirit_cost = property(get_spirit_cost)
    bone_cost = property(get_bone_cost)
    flesh_cost = property(get_flesh_cost)
    ectoplasm_cost = property(get_ectoplasm_cost)

    # methods
    def can_perform(self, inventory):
        if not isinstance(inventory, Inventory):
            return False
        return inventory.resource_requirements(self.__get_costs())

    def consume_resources(self, inventory):
        if not isinstance(inventory, Inventory):
            return False
        return inventory.spend_resource(self.__get_costs())

    def create_summon(self, unit_id):
        return self.__undead_class(unit_id, self.__undead_name, self.__starting_health, self.__starting_power)

    def __str__(self):
        return (f"{self.__ritual_name} -> {self.__undead_name} "
                f"(Health: {self.__starting_health}, Power: {self.__starting_power}) | "
                f"Costs - Necrotic: {self.__necrotic_cost}, Spirit: {self.__spirit_cost}, "
                f"Bone: {self.__bone_cost}, Flesh: {self.__flesh_cost}, "
                f"Ectoplasm: {self.__ectoplasm_cost}")


# ritual instances
skeleton_warrior_ritual = SummoningRitual(
    "Skeleton Rising", "Undead Skeleton Warrior", SkeletonWarrior, 80, 15,
    necrotic_cost=5, bone_cost=15, ectoplasm_cost=10
)

vengeful_ghost_ritual = SummoningRitual(
    "Spectral Binding", "Vengeful Ghost", VengefulGhost, 50, 25,
    necrotic_cost=5, spirit_cost=20, ectoplasm_cost=15
)

putrid_zombie_ritual = SummoningRitual(
    "Corpse Reanimation", "Putrid Zombie", PutridZombie, 120, 10,
    necrotic_cost=5, flesh_cost=20, ectoplasm_cost=10
)

phantom_guardian_ritual = SummoningRitual(
    "Guardian's Vigil", "Phantom Guardian", PhantomGuardian, 150, 30,
    necrotic_cost=10, spirit_cost=15, bone_cost=10, flesh_cost=10, ectoplasm_cost=30
)

death_knight_ritual = SummoningRitual(
    "Skeleton King", "Death Knight", DeathKnight, 220, 30, 
    necrotic_cost=20, spirit_cost=25, ectoplasm_cost=40, bone_cost=5, flesh_cost=10      
)
