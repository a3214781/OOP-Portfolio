from inventory import Inventory


class Necromancer:
    MAX_UNDEAD = 10

    def __init__(self, name, ectoplasm=0, necrotic=0, spirit=0, bone=0, flesh=0):
        if isinstance(name, str):
            self.__name = name
        else:
            self.__name = ""

        # Inventory is created by and belongs to this Necromancer
        self.__inventory = Inventory(necrotic, spirit, bone, flesh, ectoplasm)
        self.__controlled_undead = []
        self.__next_id = 1

    # getters
    def get_name(self):
        return self.__name

    def get_inventory(self):
        return self.__inventory

    def get_controlled_undead(self):
        return list(self.__controlled_undead)
    
    def set_name(self, name):
        return name == self.__name

    # properties
    name = property(get_name, set_name)
    inventory = property(get_inventory)
    controlled_undead = property(get_controlled_undead)

    def collect_resources(self, necrotic=0, spirit=0, bone=0, flesh=0, ectoplasm=0):
        self.__inventory.collect_resource(necrotic, spirit, bone, flesh, ectoplasm)

    # sets ID to 3 numbers. etc 3 = 003
    def __generate_id(self):
        new_id = f"UND-{self.__next_id:03d}"
        self.__next_id += 1
        return new_id

    def __find_undead(self, unit_id):
        for undead in self.__controlled_undead:
            if undead.get_unit_id() == unit_id:
                return undead
        return None

    def summon_undead(self, ritual):
        if len(self.__controlled_undead) >= Necromancer.MAX_UNDEAD:
            print(f"{self.__name} cannot control any more undead")
            return None

        if not ritual.can_perform(self.__inventory):
            print(f"{self.__name} does not have enough resources for {ritual.get_ritual_name()}")
            return None

        ritual.consume_resources(self.__inventory)

        new_id = self.__generate_id()
        new_undead = ritual.create_summon(new_id)
        self.__controlled_undead.append(new_undead)
        print(f"{self.__name} summoned {new_undead.get_name()} (ID: {new_id})")
        return new_undead

    def dismiss_undead(self, unit_id):
        target = self.__find_undead(unit_id)
        if target is None:
            print(f"No controlled undead found with ID {unit_id}")
            return False

        self.__controlled_undead.remove(target)
        print(f"{target.get_name()} (ID: {unit_id}) has been dismissed")
        return True

    def level_undead(self, unit_id):
        target = self.__find_undead(unit_id)
        if target is None:
            print(f"No controlled undead found with ID {unit_id}")
            return False

        return target.level_up()

    def command_undead(self, unit_id):
        target = self.__find_undead(unit_id)
        if target is None:
            print(f"No controlled undead found with ID {unit_id}")
            return False

        target.command()
        return True

    def __str__(self):
        if self.__controlled_undead:
            undead_list = ", ".join(str(i) for i in self.__controlled_undead)
        else:
            undead_list = "None"

        return (f"Necromancer: {self.__name}\n"
                f"Resources: {self.__inventory}\n"
                f"Controlled Undead ({len(self.__controlled_undead)}/{Necromancer.MAX_UNDEAD}): {undead_list}")