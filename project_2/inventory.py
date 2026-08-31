class Inventory:
    def __init__(self: int, necrotic: int, spirit: int, bone: int, flesh: int, ectoplasm: int):
        if isinstance(necrotic, int) and necrotic > 0:
            self.__necrotic = necrotic
        if isinstance(spirit, int) and spirit > 0:
            self.__spirit = spirit
        if isinstance(bone, int) and bone > 0:
            self.__bone = bone
        if isinstance(flesh, int) and flesh > 0:
            self.__flesh = flesh
        if isinstance(ectoplasm, int) and ectoplasm > 0:
            self.__ectoplasm = ectoplasm
   
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
        
    necrotic = property(get_necrotic())
    spirit = property(get_spirit())
    bone = property(get_bone())
    flesh = property(get_flesh())
    ectoplasm = property(get_ectoplasm())
    
    def collect_resource(self, necrotic, spirit, bone, flesh, ectoplasm):
        if isinstance(necrotic, int) and necrotic > 0:
            self.__necrotic = necrotic
        if isinstance(spirit, int) and spirit > 0:
            self.__spirit = spirit
        if isinstance(bone, int) and bone > 0:
            self.__bone = bone
        if isinstance(flesh, int) and flesh > 0:
            self.__flesh = flesh
        if isinstance(ectoplasm, int) and ectoplasm > 0:
            self.__ectoplasm = ectoplasm