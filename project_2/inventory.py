class Inventory:
    """Holds the five resources a necromancer collects and spends. It
    protects the amounts so they can only change by collecting or spending
    through its own methods."""

    # No resource can ever go below zero.
    MIN_QUANTITY = 0

    def __init__(self, ectoplasm, necrotic, spirit, bone, flesh):
        # Each amount is checked by the same helper, so an invalid amount is
        # replaced by 0 instead of being repeated five times.
        self.__ectoplasm = Inventory.check_inventory(ectoplasm)
        self.__necrotic = Inventory.check_inventory(necrotic)
        self.__spirit = Inventory.check_inventory(spirit)
        self.__bone = Inventory.check_inventory(bone)
        self.__flesh = Inventory.check_inventory(flesh)

    @staticmethod
    def check_inventory(qty):
        # This is a static method because it only checks the number it is
        # given and does not need any data from an Inventory object.
        # Bool is rejected because Python treats True as the number 1.
        if (
            isinstance(qty, int)
            and not isinstance(qty, bool)
            and qty >= Inventory.MIN_QUANTITY
        ):
            return qty
        else:
            return Inventory.MIN_QUANTITY

    @property
    def necrotic(self):
        return self.__necrotic

    @property
    def spirit(self):
        return self.__spirit

    @property
    def bone(self):
        return self.__bone

    @property
    def flesh(self):
        return self.__flesh

    @property
    def ectoplasm(self):
        return self.__ectoplasm

    def collect_resource(
        self, ectoplasm, necrotic=0, spirit=0, bone=0, flesh=0
    ):
        # Only positive whole numbers are added, so collecting can never
        # lower an amount or add something invalid. The other resources
        # default to 0 so a caller can collect just one kind.
        # Ectoplasm also must be set as everything has ectoplasm.
        if (
            isinstance(ectoplasm, int)
            and not isinstance(ectoplasm, bool)
            and ectoplasm > 0
        ):
            self.__ectoplasm += ectoplasm
        if (
            isinstance(necrotic, int)
            and not isinstance(necrotic, bool)
            and necrotic > 0
        ):
            self.__necrotic += necrotic
        if (
            isinstance(spirit, int)
            and not isinstance(spirit, bool)
            and spirit > 0
        ):
            self.__spirit += spirit
        if isinstance(bone, int) and not isinstance(bone, bool) and bone > 0:
            self.__bone += bone
        if (
            isinstance(flesh, int)
            and not isinstance(flesh, bool)
            and flesh > 0
        ):
            self.__flesh += flesh

    def resource_requirements(self, requirements: list) -> bool:
        # Checks if there is enough of every resource without spending
        # anything. The requirements are a list of five amounts
        # in a fixed order: necrotic, spirit, bone, flesh, ectoplasm.
        # A list with any other length can never be met.
        if not isinstance(requirements, list) or len(requirements) != 5:
            return False

        # The current amounts are listed in the same order as the
        # requirements, so the same position in each list is the same resource.
        current = [
            self.__ectoplasm,
            self.__necrotic,
            self.__spirit,
            self.__bone,
            self.__flesh,
        ]

        for position in range(len(current)):
            if requirements[position] > current[position]:
                return False

        return True

    def spend_resource(self, requirements: list) -> bool:
        # Everything is checked first, so a failed spend takes nothing and
        # never leaves the inventory half spent.
        if not self.resource_requirements(requirements):
            print("You do not have the required resources")
            return False

        # The check above passed, so every amount is available. The order is
        # the same as in resource_requirements().
        self.__ectoplasm -= requirements[0]
        self.__necrotic -= requirements[1]
        self.__spirit -= requirements[2]
        self.__bone -= requirements[3]
        self.__flesh -= requirements[4]

        print(
            f"You spent (necrotic, spirit, bone, flesh, ectoplasm): "
            f"{requirements}"
        )
        return True

    def __str__(self):
        # Shows all five amounts on one line so the inventory can be
        # inspected during a demonstration.
        return (
            f"Necrotic Runes: {self.__necrotic}, "
            f"Spirit Runes: {self.__spirit}, "
            f"Bone Runes: {self.__bone}, "
            f"Flesh Runes: {self.__flesh}, "
            f"Ectoplasm: {self.__ectoplasm}"
        )
