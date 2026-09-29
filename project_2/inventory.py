class Inventory:

    MIN_QUANTITY = 0

    def __init__(self, necrotic, spirit, bone, flesh, ectoplasm):
        self.__ectoplasm = Inventory.check_inventory(ectoplasm)
        self.__necrotic = Inventory.check_inventory(necrotic)
        self.__spirit = Inventory.check_inventory(spirit)
        self.__bone = Inventory.check_inventory(bone)
        self.__flesh = Inventory.check_inventory(flesh)

    def check_inventory(qty):
        if isinstance(qty, int) and not isinstance(qty, bool) and qty >= Inventory.MIN_QUANTITY:
            return qty
        else:
            return Inventory.MIN_QUANTITY

    # getters
    def get_necrotic(self):
        return self.__necrotic

    def get_spirit(self):
        return self.__spirit

    def get_bone(self):
        return self.__bone

    def get_flesh(self):
        return self.__flesh

    def get_ectoplasm(self):
        return self.__ectoplasm

    necrotic = property(get_necrotic)
    spirit = property(get_spirit)
    bone = property(get_bone)
    flesh = property(get_flesh)
    ectoplasm = property(get_ectoplasm)

    def collect_resource(self, necrotic=0, spirit=0, bone=0, flesh=0, ectoplasm=0):
        if isinstance(ectoplasm, int) and not isinstance(ectoplasm, bool) and ectoplasm > 0:
            self.__ectoplasm += ectoplasm
        if isinstance(necrotic, int) and not isinstance(necrotic, bool) and necrotic > 0:
            self.__necrotic += necrotic
        if isinstance(spirit, int) and not isinstance(spirit, bool) and spirit > 0:
            self.__spirit += spirit
        if isinstance(bone, int) and not isinstance(bone, bool) and bone > 0:
            self.__bone += bone
        if isinstance(flesh, int) and not isinstance(flesh, bool) and flesh > 0:
            self.__flesh += flesh

    def resource_requirements(self, requirements: dict) -> bool:
        for resource, amount in requirements.items():
            if resource == "ectoplasm":
                current = self.__ectoplasm
            elif resource == "necrotic":
                current = self.__necrotic
            elif resource == "spirit":
                current = self.__spirit
            elif resource == "bone":
                current = self.__bone
            elif resource == "flesh":
                current = self.__flesh
            else:
                return False

            if amount > current:
                return False

        return True

    def spend_resource(self, requirements: dict) -> bool:
        if not self.resource_requirements(requirements):
            print("You do not have the required resources")
            return False

        for resource, amount in requirements.items():
            if resource == "ectoplasm":
                self.__ectoplasm -= amount
            elif resource == "necrotic":
                self.__necrotic -= amount
            elif resource == "spirit":
                self.__spirit -= amount
            elif resource == "bone":
                self.__bone -= amount
            elif resource == "flesh":
                self.__flesh -= amount

        print(f"You spent: {requirements}")
        return True

    def __str__(self):
        return (f"Necrotic Runes: {self.__necrotic}, Spirit Runes: {self.__spirit}, "
                f"Bone Runes: {self.__bone}, Flesh Runes: {self.__flesh}, "
                f"Ectoplasm: {self.__ectoplasm}")