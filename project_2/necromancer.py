from inventory import Inventory
from summoning_ritual import SummoningRitual


class Necromancer:
    """A necromancer coordinates the summoning system. It owns an Inventory
    and the undead it controls, and it asks other objects to do the work.
    It does not change their private data itself."""

    # A necromancer can only control a limited number of undead at once.
    MAX_UNDEAD = 10

    def __init__(
        self, name, ectoplasm=0, necrotic=0, spirit=0, bone=0, flesh=0
    ):
        # The name must be a string, otherwise an empty string is used so the
        # necromancer can still be created.
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = ""

        # Inventory is created by and belongs to this Necromancer
        # (composition), so the starting resources are passed straight in.
        self.__inventory = Inventory(necrotic, spirit, bone, flesh, ectoplasm)
        # The undead list is private so undead can only be added or removed
        # through summon_undead() and dismiss_undead().
        self.__controlled_undead = []
        # Counts up so every new summon gets a different identifier.
        self.__next_id = 1

    @property
    def name(self):
        return self.__name

    @property
    def inventory(self):
        return self.__inventory

    @property
    def controlled_undead(self):
        # A copy is returned so the caller cannot change the real list.
        return list(self.__controlled_undead)

    def collect_resources(
        self, ectoplasm=0, necrotic=0, spirit=0, bone=0, flesh=0
    ):
        # The Inventory changes its own amounts, because it is the class that
        # manages resources. The necromancer only passes the request on.
        self.__inventory.collect_resource(
            ectoplasm=ectoplasm,
            necrotic=necrotic,
            spirit=spirit,
            bone=bone,
            flesh=flesh,
        )

    # sets ID to 3 numbers. etc 3 = 003.
    def __generate_id(self):
        # This is private because only the necromancer decides what the next
        # identifier is. The counter goes up after each use so an identifier
        # is never given out twice no matter what.
        new_id = f"UND-{self.__next_id:03d}"
        self.__next_id += 1
        return new_id

    def __find_undead(self, unit_id):
        # One private helper finds an undead by identifier, so dismissing,
        # levelling and commanding do not each repeat the same loop. It
        # returns None when nothing matches.
        for undead in self.__controlled_undead:
            if undead.unit_id == unit_id:
                return undead
        return None

    def summon_undead(self, ritual):
        # The ritual must be a real SummoningRitual, otherwise the calls
        # below would crash.
        if not isinstance(ritual, SummoningRitual):
            print("A summoning ritual is required.")
            return None

        # The limit is checked first so a full army never spends resources.
        if len(self.__controlled_undead) >= Necromancer.MAX_UNDEAD:
            print(f"{self.__name} cannot control any more undead")
            return None

        # The resources are checked before anything is spent,
        # therefore a failed summon leaves the inventory unchanged.
        if not ritual.can_perform(self.__inventory):
            print(
                f"{self.__name} does not have enough resources for "
                f"{ritual.ritual_name}"
            )
            return None

        ritual.consume_resources(self.__inventory)

        # The necromancer supplies the identifier and the ritual builds the
        # correct type of undead, so the necromancer never creates a
        # specialised undead itself.
        new_id = self.__generate_id()
        new_undead = ritual.create_summon(new_id)
        self.__controlled_undead.append(new_undead)
        print(f"{self.__name} summoned {new_undead.name} (ID: {new_id})")
        return new_undead

    def dismiss_undead(self, unit_id):
        # Returns True or False so the caller knows if the undead was found
        # and removed.
        target = self.__find_undead(unit_id)
        if target is None:
            print(f"No controlled undead found with ID {unit_id}")
            return False

        self.__controlled_undead.remove(target)
        print(f"{target.name} (ID: {unit_id}) has been dismissed")
        return True

    def level_undead(self, unit_id):
        # The levelling itself is given to the undead, because it owns
        # its own level, health and power.
        target = self.__find_undead(unit_id)
        if target is None:
            print(f"No controlled undead found with ID {unit_id}")
            return False

        return target.level_up()

    def command_undead(self, unit_id):
        # Each type of undead answers command() in its own way, so the
        # necromancer does not need to check what type it is commanding.
        target = self.__find_undead(unit_id)
        if target is None:
            print(f"No controlled undead found with ID {unit_id}")
            return False

        target.command()
        return True

    def __str__(self):
        # The undead are joined into one line, with "None" shown when the
        # necromancer has not summoned any yet.
        undead_list = ""
        for undead in self.__controlled_undead:
            # A comma is only needed between undead, not before the first.
            if undead_list != "":
                undead_list += ", "
            undead_list += str(undead)

        # The text is still empty when there are no undead.
        if undead_list == "":
            undead_list = "None"

        return (
            f"Necromancer: {self.__name}\n"
            f"Resources: {self.__inventory}\n"
            f"Controlled Undead "
            f"({len(self.__controlled_undead)}/"
            f"{Necromancer.MAX_UNDEAD}): {undead_list}"
        )
